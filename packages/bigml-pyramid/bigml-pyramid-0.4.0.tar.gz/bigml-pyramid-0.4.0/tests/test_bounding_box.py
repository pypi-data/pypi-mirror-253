import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import os
import json
import time
import random
import shutil

from PIL import Image, ImageDraw

from sensenet.accessors import yolo_outputs
from sensenet.constants import IMAGE, BOUNDING_BOX
from sensenet.models.wrappers import create_model, convert

from pyramid.constants import ANCHORS_PER_SIZE, MAX_BOXES
from pyramid.constants import CONF_FORMAT, PROB_FORMAT, CIOU_FORMAT
from pyramid.constants import LOG_VERBOSE, DEFAULT_EXPORT_SETTINGS
from pyramid.data.bounding_box import box_dataset, read_bounding_box_data
from pyramid.data.bounding_box import from_xywh, to_xywh
from pyramid.data.generate import SHAPE_METHODS, draw_random_shape
from pyramid.data.generate import random_location, random_color
from pyramid.data.visualize import show_bounding_box_batch
from pyramid.pyramid import holdout_image_predictions
from pyramid.settings.base_settings import IMAGE_TRAINING, IMG_FINE_TUNE
from pyramid.settings.base_settings import IMG_SCRATCH, FINALIZING
from pyramid.settings.bounding_box_loss import recover_tensors
from pyramid.settings.image import trainable_yolo, make_anchors
from pyramid.settings.job_settings import JobSettings
from pyramid.train.finalize import finalize
from pyramid.train.model import fit
from pyramid.trainer import rescale_boxes

from .test_train import check_format
from .utils import TEST_IMAGE_ROOT, TEST_OUTPUT, TEST_MODEL_FILE, clean_temp

TINY_ANCHORS = [[23, 29], [37, 58], [81, 82], [81, 83], [135, 169], [344, 319]]
BOX_COLORS = ["red", "blue", "green", "yellow", "black", "purple", "orange"]


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def draw_truth(draw, shape, image_shape, w, h, rng):
    max_w, max_h = image_shape
    coords = random_location(max_w, max_h, w, h, rng)
    fill_color = random_color(rng)
    outline_color = random_color(rng)

    SHAPE_METHODS[shape](draw, coords, fill_color, outline_color)

    return [coords[0] - 2, coords[1] - 2, coords[2] + 2, coords[3] + 2]


def make_example(image_shape, n_false, true_shapes, w, h, seed):
    rng = random.Random(seed)
    image = Image.new("RGB", image_shape, (128, 128, 128))
    draw = ImageDraw.Draw(image)

    false_shapes = sorted(set(SHAPE_METHODS.keys()) - set(true_shapes))

    for _ in range(n_false):
        shape = rng.choice(false_shapes)
        draw_random_shape(draw, shape, image_shape, rng)

    all_true = []

    for shape in true_shapes:
        true_coords = draw_truth(draw, shape, image_shape, w, h, rng)
        all_true.append(list(true_coords) + [shape])

    # Put in a box located off the image, just to see what happens
    all_true.append(
        [
            image_shape[0] - 50,
            image_shape[1] + 20,
            image_shape[0] + 5,
            image_shape[1] + 50,
            true_shapes[0],
        ]
    )

    return {"image": image, "boxes": all_true}


def create_box_dataset(n_images, image_shape, n_false, true_shapes, w, h):
    training_data = []

    for i in range(n_images):
        example = make_example(image_shape, n_false, true_shapes, w, h, i)
        fname = "%08d.png" % i

        example["image"].save(os.path.join(TEST_IMAGE_ROOT, fname))
        training_data.append({"file": fname, "boxes": example["boxes"]})

    return training_data


def make_box_dataset(n_images, image_shape, in_size, true_shapes, extra):
    w = 30
    h = 30
    n_false = 25
    shapes = sorted(true_shapes)

    data = create_box_dataset(n_images, image_shape, n_false, shapes, w, h)

    settings = {
        "image_augmentations": ["brightness"],
        "image_root": TEST_IMAGE_ROOT,
        "image_training_type": IMG_FINE_TUNE,
        "objective_type": BOUNDING_BOX,
        "output_directory": TEST_OUTPUT,
        "descent_algorithm": "adam",
        "is_search": False,
        "strict_boxes": False,
        "return_holdout_images": True,
        "input_image_shape": [in_size, in_size, 3],
        "learning_rate": 1e-2,
        "logging_level": None,
        "batch_size": 16,
        "seed": 42,
        "layers": [],
        "max_iterations": 128,
        "start_time": time.time(),
        "job_type": IMAGE_TRAINING,
        "base_image_network": "tinyyolov4",
        "info_list": [
            {"type": IMAGE, "index": 0},
            {"type": BOUNDING_BOX, "index": 1, "values": shapes},
        ],
    }

    if extra:
        settings.update(extra)

    new_settings, new_data = rescale_boxes(settings, data)
    new_settings["image_training_data"] = new_data

    if "bounding_box_anchors" not in settings:
        anchors = make_anchors(None, settings["base_image_network"], new_data)
        new_settings["bounding_box_anchors"] = anchors

    return JobSettings(new_settings)


def test_dataset():
    shape = (256, 256)
    classes = ["ellipse"]
    extras = {"bounding_box_anchors": TINY_ANCHORS}

    settings = make_box_dataset(64, shape, shape[0], classes, extras)
    instances = read_bounding_box_data(settings)
    tf_dataset = box_dataset(settings, instances, False)

    for batch in tf_dataset.take(4):
        # show_batch(batch)

        X, outputs = batch
        y = []

        for i in range(2):
            grid = shape[0] // ((i + 1) * 16)
            labels_boxes = outputs[CONF_FORMAT % i]
            y.append(recover_tensors(grid, 1, labels_boxes))

        assert X.shape == (16, shape[0], shape[1], 3), X.shape
        assert len(outputs) == 6

        assert np.all(outputs[PROB_FORMAT % 0] == y[0][0])
        assert np.all(outputs[CIOU_FORMAT % 0] == y[0][0])
        assert np.all(outputs[PROB_FORMAT % 1] == y[1][0])
        assert np.all(outputs[CIOU_FORMAT % 1] == y[1][0])

        assert y[0][0].shape == (16, 16, 16, ANCHORS_PER_SIZE, 6), y[0][0].shape
        assert y[0][1].shape == (16, MAX_BOXES, 5), y[1][1].shape
        assert y[1][0].shape == (16, 8, 8, ANCHORS_PER_SIZE, 6), y[1][0].shape
        assert y[1][1].shape == (16, MAX_BOXES, 5), y[1][1].shape

        for img in y[0][0]:
            assert np.sum(img[:, :, :, -1]) == 2, np.sum(img[:, :, :, -1])
            assert np.sum(img[:, :, :, -2]) == 2, np.sum(img[:, :, :, -2])
            assert np.all(img[img[:, :, :, -1] == 1][:, 2:4] == 34)

        for boxes in y[0][1]:
            assert np.sum(boxes[0, 0:2]) > 0
            assert np.all(boxes[0, 2:4] == 34)
            assert np.sum(boxes[1:, :]) == 0

        for img in y[1][0]:
            assert np.sum(img) == 0

        for boxes in y[1][1]:
            assert np.sum(boxes) == 0

    anchors = make_anchors(None, "tinyyolov4", settings.image_training_data)

    assert len(anchors) == 6, anchors
    assert all(a == [34, 34] or a == [55, 30] for a in anchors), anchors


def test_upscale():
    shape = (128, 64)
    in_size = 256
    classes = ["ellipse"]
    settings = make_box_dataset(64, shape, in_size, classes, None)
    instances = read_bounding_box_data(settings)
    tf_dataset = box_dataset(settings, instances, True)

    for batch in tf_dataset.take(4):
        # show_batch(batch)
        X, outputs = batch
        column = np.sum(X, axis=(0, 2, 3))
        row = np.sum(X, axis=(0, 1, 3))

        # Should have padding on the vertical axis, but not the horizontal
        assert np.all(column[128:] == column[128])
        assert np.all(row > 0)


def test_yolo_training_outputs():
    shape = (256, 256)
    classes = ["ellipse", "line"]
    settings = make_box_dataset(64, shape, shape[0], classes, None)
    pre_model = settings.make_model(False)
    model = trainable_yolo(settings, pre_model, True)

    read = settings.image_file_reader()
    img_px = np.expand_dims(read("00000000.png").numpy(), axis=0)
    imgs = np.tile(img_px, (2, 1, 1, 1))

    outputs = model.predict(imgs)

    assert len(outputs) == 6, outputs.keys()

    for k in outputs:
        assert len(outputs[k].shape) == 5
        assert outputs[k].shape[0] == 2

    assert outputs[CONF_FORMAT % 0].shape[-1] == 6
    assert outputs[CONF_FORMAT % 1].shape[-1] == 6
    assert outputs[PROB_FORMAT % 0].shape[-1] == 7
    assert outputs[PROB_FORMAT % 1].shape[-1] == 7
    assert outputs[CIOU_FORMAT % 0].shape[-1] == 7
    assert outputs[CIOU_FORMAT % 1].shape[-1] == 7

    assert outputs[PROB_FORMAT % 0].shape == outputs[CIOU_FORMAT % 0].shape
    assert outputs[PROB_FORMAT % 1].shape == outputs[CIOU_FORMAT % 1].shape


def iou(b1, b2):
    box1 = np.array(b1)
    box2 = np.array(b2)

    box1_xywh = to_xywh(b1, 0)
    box2_xywh = to_xywh(b2, 0)
    box1_area = box1_xywh[2] * box1_xywh[3]
    box2_area = box2_xywh[2] * box2_xywh[3]

    left_up = np.maximum(box1[:2], box2[:2])
    right_down = np.minimum(box1[2:], box2[2:])

    isect_wh = np.maximum(right_down - left_up, 0.0)
    isect_area = isect_wh[0] * isect_wh[1]
    union_area = box1_area + box2_area - isect_area

    assert isect_area <= union_area

    return isect_area / union_area


def model_and_check(settings):
    model = settings.make_model(False)
    fit_info, _ = fit(model, settings)

    assert "holdout_images" in fit_info
    assert len(fit_info["holdout_images"]) == int(round(0.2 * 256))

    settings.write_network(model, fit_info, None)

    settings.job_type = FINALIZING
    preds = holdout_image_predictions(settings)

    assert len(preds) == len(fit_info["holdout_images"])

    joutput = finalize(settings)
    check_format(joutput, settings.info_list)
    settings.write_json(joutput, TEST_MODEL_FILE)

    settings.job_type = IMAGE_TRAINING

    return joutput


def check_box_detector(settings, joutput):
    ntest = 64
    instances = read_bounding_box_data(settings)
    read = settings.image_file_reader()

    bbox_model = create_model(joutput, None)
    correct = 0

    for instance in instances[:ntest]:
        pred = bbox_model([os.path.join(TEST_IMAGE_ROOT, instance[0])])
        point = from_xywh(instance[1][0], None)

        if len(pred) > 0:
            if iou(point[:4], pred[0]["box"]) > 0.5:
                correct += 1

    assert 0.9 <= correct / ntest <= 1.0, correct / ntest


def try_exports(joutput):
    for aformat in ["tflite", "tfjs", "smbundle", "h5"]:
        outpath = TEST_MODEL_FILE + "." + aformat
        convert(joutput, DEFAULT_EXPORT_SETTINGS, outpath, aformat)

        if aformat == "tfjs":
            shutil.rmtree(outpath)
        else:
            os.remove(outpath)


def test_tinyyolo():
    shape = (256, 256)
    classes = ["ellipse"]

    extra = {
        "base_image_network": "tinyyolov4",
        "bounding_box_anchors": TINY_ANCHORS,
    }

    settings = make_box_dataset(256, shape, shape[0], classes, extra)
    joutput1 = model_and_check(settings)

    next_settings = dict(vars(settings))
    next_settings.pop("training_options")
    next_settings["base_image_network"] = "initial_model"
    next_settings["initial_model"] = os.path.join(TEST_OUTPUT, TEST_MODEL_FILE)
    next_settings["max_iterations"] = settings.max_iterations

    next_js = JobSettings(next_settings)
    joutput2 = model_and_check(next_js)

    for joutput in [joutput1, joutput2]:
        out_branches = yolo_outputs(joutput)
        anchors1 = out_branches[0]["anchors"]
        anchors2 = out_branches[1]["anchors"]

        assert anchors1 == TINY_ANCHORS[:3], str(anchors1)
        assert anchors2 == TINY_ANCHORS[3:], str(anchors2)

    check_box_detector(next_js, joutput2)
    try_exports(joutput2)


def test_yolo():
    shape = (64, 64)
    classes = ["ellipse"]

    extra = {"base_image_network": "yolov4"}
    settings = make_box_dataset(256, shape, shape[0], classes, extra)
    joutput = model_and_check(settings)

    out_branches = yolo_outputs(joutput)
    assert len(out_branches) == 3

    for branch in out_branches:
        anchors = branch["anchors"]
        assert all(a == [34, 34] or a == [55, 30] for a in anchors), anchors

    check_box_detector(settings, joutput)
