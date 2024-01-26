import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import random

from pyramid.constants import CONF_FORMAT, PROB_FORMAT, CIOU_FORMAT
from pyramid.constants import MAX_BOXES, ANCHORS_PER_SIZE, BOX_LABEL_SMOOTHING
from pyramid.constants import FEATURES_FORMAT, BOXES_FORMAT, BACKGROUND_IOU
from pyramid.constants import MAX_INT_32, NON_BOX_AUGMENTATIONS

from pyramid.data.image import read_image, make_training_image_generator

AUTOTUNE = tf.data.experimental.AUTOTUNE


def to_xywh(box, box_class):
    return [
        (box[0] + box[2]) * 0.5,
        (box[1] + box[3]) * 0.5,
        box[2] - box[0],
        box[3] - box[1],
        box_class if box_class is not None else box[4],
    ]


def from_xywh(box, box_class):
    return [
        box[0] - (box[2] * 0.5),
        box[1] - (box[3] * 0.5),
        box[0] + (box[2] * 0.5),
        box[1] + (box[3] * 0.5),
        box_class if box_class is not None else box[4],
    ]


def bbox_iou(boxes1, boxes2):
    boxes1_area = boxes1[..., 2] * boxes1[..., 3]
    boxes2_area = boxes2[..., 2] * boxes2[..., 3]

    coor1 = tf.concat(
        [
            boxes1[..., :2] - boxes1[..., 2:] * 0.5,
            boxes1[..., :2] + boxes1[..., 2:] * 0.5,
        ],
        axis=-1,
    )
    coor2 = tf.concat(
        [
            boxes2[..., :2] - boxes2[..., 2:] * 0.5,
            boxes2[..., :2] + boxes2[..., 2:] * 0.5,
        ],
        axis=-1,
    )

    left_up = tf.maximum(coor1[..., :2], coor2[..., :2])
    right_down = tf.minimum(coor1[..., 2:], coor2[..., 2:])

    intersection = tf.maximum(right_down - left_up, 0.0)
    isect_area = intersection[..., 0] * intersection[..., 1]
    union_area = boxes1_area + boxes2_area - isect_area

    return tf.math.divide_no_nan(isect_area, union_area)


def read_bounding_box_data(settings):
    if settings.image_training_data is not None:
        data = settings.image_training_data
    else:
        with open(settings.cache_file, "r") as fin:
            data = json.read(fin)

    classes = settings.get_classes()
    instances = []

    for d in data:
        instance = [d["file"], []]

        for box in d["boxes"]:
            # x1, y1, x2, y2, class -> x, y, w, h, class
            instance[1].append(to_xywh(box, classes.index(box[4])))

        instances.append(instance)

    return instances


class BoxMaker(object):
    def __init__(self, settings):
        self._n_classes = settings.number_of_classes()
        self._input_size = settings.input_image_shape[1]
        self._strict_boxes = settings.strict_boxes

        metadata = settings.image_network()["image_network"]["metadata"]
        assert len(metadata["outputs"]) > 1

        strides = [b["strides"] for b in metadata["outputs"]]
        anchors = [b["anchors"] for b in metadata["outputs"]]

        self._output_sizes = [self._input_size // int(s) for s in strides]
        self._all_strides = np.array(strides, dtype=np.float32)[:, np.newaxis]
        self._anchors = [
            np.array(a, dtype=np.float32) / np.float32(s)
            for a, s in zip(anchors, strides)
        ]

        uniform = np.full(self._n_classes, 1.0 / self._n_classes)
        sfactor = settings.label_smoothing_factor
        smoothing = sfactor if sfactor is not None else BOX_LABEL_SMOOTHING

        self._true_label_weight = 1 - smoothing
        self._label_smooth = uniform * smoothing

    def preprocess_true_boxes(self, bboxes):
        label = []
        bboxes_xywhc = []

        for size in self._output_sizes:
            lsize = (size, size, ANCHORS_PER_SIZE, self._n_classes + 5)
            label.append(np.zeros(lsize, dtype=np.float32))
            bboxes_xywhc.append(np.zeros((MAX_BOXES, 5), dtype=np.float32))

        bbox_count = np.zeros((len(self._output_sizes),), dtype=np.int32)

        for bbox in bboxes:
            onehot = np.zeros(self._n_classes, dtype=np.float32)
            onehot[bbox[4]] = self._true_label_weight
            smooth_onehot = onehot + self._label_smooth

            bx_xywh = np.array(bbox[:4], dtype=np.float32)
            bx_xywh_scaled = 1.0 * bx_xywh[np.newaxis, :] / self._all_strides

            iou = []

            exist_positive = False
            in_any_grid = False

            for i in range(len(self._output_sizes)):
                scaled_i = bx_xywh_scaled[i]
                scaled_xy = np.floor(bx_xywh_scaled[i, 0:2]).astype(np.int32)

                anchors_xywh = np.zeros((ANCHORS_PER_SIZE, 4), dtype=np.float32)
                anchors_xywh[:, 0:2] = scaled_xy + 0.5
                anchors_xywh[:, 2:4] = self._anchors[i]

                iou_scale = bbox_iou(scaled_i[np.newaxis, :], anchors_xywh)
                iou_mask = iou_scale > BACKGROUND_IOU
                iou.append(iou_scale)

                xind, yind = scaled_xy
                in_grid = xind < label[i].shape[0] and yind < label[i].shape[1]

                if in_grid:
                    # If we're going to try to locate this box, we need
                    # to have the image sitting on at least one grid;
                    # we'll ignore it if it's not
                    in_any_grid = True

                    if np.any(iou_mask):
                        label[i][yind, xind, iou_mask, :] = 0
                        label[i][yind, xind, iou_mask, 0:4] = bx_xywh
                        label[i][yind, xind, iou_mask, 4:5] = 1.0
                        label[i][yind, xind, iou_mask, 5:] = smooth_onehot

                        bbox_ind = int(bbox_count[i] % MAX_BOXES)
                        bboxes_xywhc[i][bbox_ind, :4] = bx_xywh
                        bboxes_xywhc[i][bbox_ind, 4] = bbox[4]

                        bbox_count[i] += 1
                        exist_positive = True

            if not exist_positive and in_any_grid:
                iou_array = np.array(iou, dtype=np.float32)
                best_anchor_ind = np.argmax(iou_array.reshape(-1), axis=-1)
                best_detect = int(best_anchor_ind / ANCHORS_PER_SIZE)
                best_anchor = int(best_anchor_ind % ANCHORS_PER_SIZE)

                best_coords = bx_xywh_scaled[best_detect, 0:2]
                xind, yind = np.floor(best_coords).astype(np.int32)

                label[best_detect][yind, xind, best_anchor, :] = 0
                label[best_detect][yind, xind, best_anchor, 0:4] = bx_xywh
                label[best_detect][yind, xind, best_anchor, 4:5] = 1.0
                label[best_detect][yind, xind, best_anchor, 5:] = smooth_onehot

                bbox_ind = int(bbox_count[best_detect] % MAX_BOXES)
                bboxes_xywhc[best_detect][bbox_ind, :4] = bx_xywh
                bboxes_xywhc[best_detect][bbox_ind, 4] = bbox[4]

                bbox_count[best_detect] += 1
            elif not in_any_grid and self._strict_boxes:
                raise ValueError("Bounding box %s is out of bounds" % str(bbox))

        return label, bboxes_xywhc


def transform_boxes(box_list, image_shape, tfm):
    new_boxes = []

    # Match box dimension ordering: (width, height)
    shape = np.array([image_shape[1], image_shape[0]], dtype=np.float32)

    # Apparently, for the keras image data generator, x is "height" or
    # "vertical" and y is "width" or "horizontal" ...
    zoom = np.array([tfm["zy"], tfm["zx"]], dtype=np.float32)
    trans = np.array([tfm["ty"], tfm["tx"]], dtype=np.float32)

    # ... and the directions are reversed from what a (totally
    # unreasonable?) person might be expecting: These values look more
    # like what you have to do to get the *original image given the
    # homography*, not the other way around as I'd expect.  And of
    # course we're trying to go *to* the homography's coordinates with
    # the box, so these values have to be inverted.
    zoom = 1 / zoom
    trans = -trans

    # Zoomed images are centrally cropped (or symetically padded if
    # made smaller), and so this requires translation in that amount
    trans += (shape - zoom * shape) / 2.0

    for box in box_list:
        xy = np.array(box[:2]) * zoom + trans
        wh = np.array(box[2:4]) * zoom

        for idx, flip_type in enumerate(["flip_horizontal", "flip_vertical"]):
            if tfm[flip_type]:
                xy[idx] = shape[idx] - xy[idx]

        new_boxes.append(xy.tolist() + wh.tolist() + [box[4]])

    return new_boxes


def box_generator(settings, instances, is_holdout):
    box_maker = BoxMaker(settings)
    rng = random.Random(settings.seed)

    if not is_holdout:
        augmenter = make_training_image_generator(
            settings, NON_BOX_AUGMENTATIONS
        )
        more_augmentations = augmenter.preprocessing_function
        aug_rng = random.Random(settings.augmentation_seed or settings.seed)
    else:
        augmenter = None
        more_augmentations = None
        aug_rng = None

    image_size = settings.input_image_shape[1]
    output_sizes = box_maker._output_sizes
    n_outputs = box_maker._n_classes + 5

    image_shape = (None, image_size, image_size, 3)
    boxes_shape = (MAX_BOXES, 5)

    def gen():
        instance_index = 0

        while instance_index < len(instances):
            targets = {}

            if is_holdout:
                path, image_boxes = instances[instance_index]
                instance_index += 1
            else:
                path, image_boxes = rng.choice(instances)

            image = read_image(settings, image_shape, True, [path]).numpy()

            if augmenter:
                rseed = aug_rng.randint(0, MAX_INT_32 - 1)

                tfm = augmenter.get_random_transform(image.shape, seed=rseed)
                image = augmenter.apply_transform(image, tfm)
                image_boxes = transform_boxes(image_boxes, image.shape, tfm)

                if more_augmentations:
                    image = more_augmentations(image)

            labels, bboxes = box_maker.preprocess_true_boxes(image_boxes)

            for j, lb in enumerate(zip(labels, bboxes)):
                label, bbox = lb

                targets[FEATURES_FORMAT % j] = label
                targets[BOXES_FORMAT % j] = bbox

            outputs = {}

            for i, _ in enumerate(output_sizes):
                labels = tf.reshape(targets[FEATURES_FORMAT % i], [-1])
                bboxes = tf.reshape(targets[BOXES_FORMAT % i], [-1])

                outputs[CONF_FORMAT % i] = tf.concat([labels, bboxes], 0)
                outputs[PROB_FORMAT % i] = targets[FEATURES_FORMAT % i]
                outputs[CIOU_FORMAT % i] = targets[FEATURES_FORMAT % i]

            yield image, outputs

    boxes_length = int(np.prod(boxes_shape))

    out_types = {}
    out_shapes = {}

    for i, size in enumerate(output_sizes):
        labels_shape = (size, size, ANCHORS_PER_SIZE, n_outputs)
        labels_length = int(np.prod(labels_shape))

        out_types[CONF_FORMAT % i] = tf.float32
        out_types[PROB_FORMAT % i] = tf.float32
        out_types[CIOU_FORMAT % i] = tf.float32

        out_shapes[CONF_FORMAT % i] = (labels_length + boxes_length,)
        out_shapes[PROB_FORMAT % i] = labels_shape
        out_shapes[CIOU_FORMAT % i] = labels_shape

    return gen, (tf.float32, out_types), (image_shape[1:], out_shapes)


def box_dataset(settings, instances, randomize):
    generator, dtypes, dshapes = box_generator(settings, instances, randomize)
    dataset = tf.data.Dataset.from_generator(generator, dtypes, dshapes)

    return dataset.batch(settings.batch_size).prefetch(buffer_size=AUTOTUNE)
