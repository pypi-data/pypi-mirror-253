import os
import time

from sensenet.constants import CATEGORICAL, NUMERIC, MEAN
from sensenet.models.image import (
    image_model,
    get_image_layers,
    io_for_extractor,
)

import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

from pyramid.data.numpy import read_numpy_arrays
from pyramid.data.image import read_images
from pyramid.pyramid import holdout_image_predictions
from pyramid.settings.base_settings import (
    IMAGE_TRAINING,
    IMG_SCRATCH,
    IMG_PRETRAINED,
)
from pyramid.settings.job_settings import JobSettings
from pyramid.train.finalize import finalize
from pyramid.train.model import fit
from pyramid.train.metrics import safe_r2, safe_auc
from pyramid.trainer import make_top_layers

from .test_train import check_format, check_layers, match_layers, make_model_dir
from .utils import (
    image_rows_from_directory,
    cache_data,
    clean_temp,
    TEST_OUTPUT,
)
from .utils import TEST_DATA_FILE, TEST_MODEL_FILE, DIGIT_ROOT, ANIMAL_ROOT


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def make_rows(otype, root_dir, classes):
    image_rows = image_rows_from_directory(root_dir)

    if otype == CATEGORICAL:
        objective = "crossentropy"
        noutputs = len(classes)
    else:
        objective = "mean_squared_error"
        noutputs = 1

        for row in image_rows:
            if row["label"] == 0:
                row["label"] = -0.5
            elif row["label"] == 1:
                row["label"] = 0.5
            else:
                raise ValueError(
                    "What on earth is this %s?" % str(row["label"])
                )

    return image_rows, objective, noutputs


def make_job_settings(otype, classes, extra):
    img_root = extra.get("image_root", DIGIT_ROOT)

    if classes is not None and len(classes) == 1:
        img_root = os.path.join(img_root, classes[0])

    image_rows, objective, noutputs = make_rows(otype, img_root, classes)
    info_list = cache_data(image_rows, classes)

    settings = {
        "seed": 42,
        "max_data_size": 1024000,
        "max_iterations": 768,
        "cache_file": TEST_DATA_FILE + ".json",
        "base_image_network": "mobilenetv2",
        "input_image_shape": [32, 32, 3],
        "job_type": IMAGE_TRAINING,
        "output_directory": TEST_OUTPUT,
        "image_training_type": IMG_SCRATCH,
        "return_holdout_images": True,
        "image_augmentations": ["zoom"],
        "image_root": img_root,
        "info_list": info_list,
        "is_search": False,
        "job_id": "test_image_model",
        "descent_algorithm": "adam",
        "batch_size": 32,
        "learning_rate": 1e-3,
        "loss_function": objective,
        "objective_type": info_list[-1]["type"],
        "logging_level": None,
        "layers": make_top_layers(noutputs, classes is not None),
    }

    settings.update(extra)
    return JobSettings(settings)


def try_modeling(otype, classes, extra={}, tune=False):
    js = make_job_settings(otype, classes, extra)
    js.start_time = time.time()

    make_model_dir(js)

    try:
        os.mkdir(os.path.join(TEST_OUTPUT, js.model_directory(None)))
    except FileExistsError:
        pass

    model = js.make_model(False)
    fit_info, _ = fit(model, js)

    X, y_true, _ = read_images(js, read_numpy_arrays(js))
    y_score1 = model.predict(X)

    js.write_network(model, fit_info, None)
    joutput = finalize(js)
    preds = holdout_image_predictions(js)

    if MEAN in fit_info["output_exposition"]:
        for pred in preds:
            truth = pred[1]
            assert int(round(float(truth))) in [3, 8]

    assert len(set([p[0] for p in preds])) == len(preds)
    assert len(preds) == len(fit_info["holdout_images"])
    check_format(joutput, js.info_list)

    remodel = js.make_model(True)
    y_score2 = remodel.predict(X)

    match_layers(model.layers, remodel.layers)
    match_layers(get_image_layers(model), get_image_layers(remodel))
    # The fitted model and the reconstituted model should be different
    # in some way
    assert model != remodel

    # But predictions should be the same
    # (aside - I can't believe they're exactly equal in all cases)
    assert np.array_equal(y_score1, y_score2), (y_score1, y_score2)

    # Write out model
    js.write_json(joutput, TEST_MODEL_FILE, pretty=True)
    check_layers(joutput["layers"])

    if tune:
        assert "holdout_images" in fit_info
        assert len(fit_info["holdout_images"]) == 32

        next_settings = dict(vars(js))
        next_settings.pop("training_options")
        next_settings["base_image_network"] = "initial_model"
        next_settings["initial_model"] = os.path.join(
            TEST_OUTPUT, TEST_MODEL_FILE
        )
        next_settings["max_iterations"] = js.max_iterations / 8

        next_js = JobSettings(next_settings)
        model = next_js.make_model(False)
        fit_info, _ = fit(model, next_js)

        X, y_true, _ = read_images(js, read_numpy_arrays(js))
        y_score1 = model.predict(X)

    return model, y_true, y_score1


def test_categorical():
    model, y_true, y_score = try_modeling(CATEGORICAL, ["3", "8"], tune=True)

    assert safe_auc(y_true, y_score) > 0.9, safe_auc(y_true, y_score)


def test_numeric():
    extra = {"base_image_network": "simple", "max_iterations": 512}
    model, y_true, y_score = try_modeling(NUMERIC, None, extra=extra, tune=True)

    assert safe_r2(y_true, y_score) > 0.9, safe_r2(y_true, y_score)


def test_rotate_shear():
    extra = {"image_augmentations": ["rotation", "shear", "glare"]}
    model, y_true, y_score = try_modeling(CATEGORICAL, ["3", "8"], extra=extra)

    assert safe_auc(y_true, y_score) > 0.9, safe_auc(y_true, y_score)


def test_simple_residual_dropblock():
    extra = {"base_image_network": "simple_residual", "max_iterations": 128}
    model, y_true, y_score = try_modeling(CATEGORICAL, ["3", "8"], extra=extra)

    assert safe_auc(y_true, y_score) > 0.9, safe_auc(y_true, y_score)


def test_strictly_pretrained():
    extra = {
        "image_training_type": IMG_PRETRAINED,
        "base_image_network": "mobilenetv2",
        "input_image_shape": [256, 192, 3],
        "image_root": ANIMAL_ROOT,
        "learning_rate": 1e-2,
        "max_iterations": 16,
        "layers": make_top_layers(2, True),
        "rescale_type": "crop",
    }

    classes = ["gorilla", "horse"]
    model, y_true, y_score = try_modeling(CATEGORICAL, classes, extra=extra)

    resettings = make_job_settings(CATEGORICAL, classes, extra)
    X, y_true, _ = read_images(resettings, read_numpy_arrays(resettings))
    bad_model = resettings.make_model(use_trained_weights=False)
    y_score_bad = bad_model.predict(X)

    assert safe_auc(y_true, y_score) > 0.9, safe_auc(y_true, y_score)
    assert safe_auc(y_true, y_score_bad) < 0.9, safe_auc(y_true, y_score_bad)

    inputs, features = io_for_extractor(model)
    model = tf.keras.Model(inputs=inputs, outputs=features)
    proj_good = model.predict(X)

    base_model = resettings.create_base_image_model(True)
    inputs, features = io_for_extractor(model)
    base_model = tf.keras.Model(inputs=inputs, outputs=features)
    proj_base = base_model.predict(X)

    assert np.sum(np.abs(proj_good - proj_base)) == 0


def test_one_class():
    extra = {"base_image_network": "simple", "max_iterations": 64}
    model, y_true, y_score = try_modeling(CATEGORICAL, ["3"], extra=extra)
    ref = y_score.copy()
    assert np.allclose(y_score, np.where(np.isnan(ref), 1, ref))
