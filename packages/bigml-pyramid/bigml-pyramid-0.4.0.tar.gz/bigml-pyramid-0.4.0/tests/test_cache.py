# -*- coding: utf-8 -*-

import time
import sys

import pyramid.importers

np = pyramid.importers.import_numpy()

from sensenet.constants import CATEGORICAL, NUMERIC

from shapsplain.represent import representatives

from pyramid.cache.read import data_to_numpy
from pyramid.cache.write import create_cache, choose_representatives
from pyramid.data.numpy import read_numpy_arrays, array_hash
from pyramid.data.stratify import numpy_split
from pyramid.settings.base_settings import IMG_FINE_TUNE, IMG_SCRATCH
from pyramid.settings.base_settings import IMAGE_TRAINING, DATA_CACHING
from pyramid.settings.job_settings import JobSettings
from pyramid.trainer import make_top_layers

from .utils import clean_temp, load_data, read_data, TEST_OUTPUT
from .test_image_dataset import SERIALIZED_IMAGE_INFO_LIST

TABULAR_DATA_SETTINGS = {
    "info_list": [
        {"index": 0, "type": "categorical", "values": ["val1", "val2"]},
        {"index": 1, "mean": 6.0, "type": "numeric", "stdev": 1.0},
        {"index": 2, "mean": 2.0, "type": "numeric", "stdev": -2.0},
        {"index": 3, "mean": 4.166667, "stdev": 6.38139, "type": "numeric"},
        {"index": 4, "mean": -0.333333, "stdev": 3.29983, "type": "numeric"},
        {"index": 5, "mean": -0.083333, "stdev": 4.08418, "type": "numeric"},
        {"index": 6, "type": "categorical", "values": ["ç我", "∫çƑ", "我"]},
        {"index": 7, "mean": 3.0, "stdev": 1.63299, "type": "numeric"},
        {"index": 8, "mean": 4.0, "stdev": 6.28490, "type": "numeric"},
    ],
    "tree_embedding": False,
    "max_data_size": 1024000,
    "cache_file": "tests/data/tabular.ser",
    "cache_rows": 3,
    "job_id": "test_caching_job",
}

IMAGE_DATA_SETTINGS = {
    "info_list": SERIALIZED_IMAGE_INFO_LIST,
    "cache_file": "tests/data/image.ser",
    "cache_rows": 5,
    "base_image_network": "mobilenet",
    "layers": make_top_layers(3, True),
    "input_image_shape": [32, 32, 3],
    "job_type": IMAGE_TRAINING,
    "image_training_type": IMG_FINE_TUNE,
    "max_data_size": 1024000,
    "tree_embedding": False,
    "output_directory": TEST_OUTPUT,
    "image_root": "tests/data/images/serialization",
    "objective_type": CATEGORICAL,
    "job_id": "test_caching_job",
}


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def test_tabular_caching():
    data = data_to_numpy(JobSettings(TABULAR_DATA_SETTINGS))

    assert data.shape == (3, 12)
    # Poor man's hash
    assert 10.999999985098839 == sum(data.flatten()), sum(data.flatten())


def test_image_caching():
    js = JobSettings(IMAGE_DATA_SETTINGS)
    image_model = js.make_image_model(False)
    js.write_network(image_model, None, None)

    js.job_type = DATA_CACHING
    data = data_to_numpy(js)

    assert np.abs(np.sum(np.abs(data)) - 193.05423) < 1e-4, np.sum(np.abs(data))

    # From the info_list above...
    nfeatures = 1024 + 1 + 1 + 1 + 1024 + 1024 + 3 + 3
    assert data.shape == (5, nfeatures), data.shape


def test_simple_image_networks():
    settings = dict(IMAGE_DATA_SETTINGS)
    settings["base_image_network"] = "simple"
    settings["image_training_type"] = IMG_SCRATCH
    js = JobSettings(settings)

    image_model = js.make_image_model(False)
    assert len(image_model.layers) == 43, len(image_model.layers)
    js.write_network(image_model, None, None)

    js.job_type = DATA_CACHING
    data = data_to_numpy(js)

    assert np.abs(np.sum(np.abs(data)) - 467.8597) < 1e-4, np.sum(np.abs(data))

    # From the info_list above...
    nfeatures = 128 + 1 + 1 + 1 + 128 + 128 + 3 + 3
    assert data.shape == (5, nfeatures), data.shape


def test_image_model_reading():
    image_path = "3/111.png"

    js = JobSettings(
        {
            "output_directory": TEST_OUTPUT,
            "image_root": "tests/data/images/digits/",
            "base_image_network": "mobilenetv2",
            "layers": make_top_layers(8, True),
            "input_image_shape": [32, 32, 3],
            "image_training_type": IMG_FINE_TUNE,
            "job_type": IMAGE_TRAINING,
            "objective_type": NUMERIC,
        }
    )

    image_model = js.make_image_model(False)
    image = np.expand_dims(js.image_file_reader()(image_path).numpy(), axis=0)
    pred = image_model(image)

    image.shape == (1, 32, 32, 3)
    assert np.sum(image) > 32 * 32 * 3

    start = time.time()
    js.write_network(image_model, None, None)
    write_time = time.time() - start
    sys.stdout.write("write %.2f / " % write_time)
    sys.stdout.flush()

    start = time.time()
    new_model = js.make_image_model(True)
    read_time = time.time() - start
    sys.stdout.write("read %.2f ..." % read_time)
    sys.stdout.flush()

    assert len(pred[0]) == 8
    assert 0.99999 < np.sum(np.abs(pred)) < 1.000001, np.sum(np.abs(pred))
    assert np.sum(np.abs(pred - new_model(image))) == 0


def test_cache_create():
    data, info_list = load_data("yacht.json.gz")

    settings = JobSettings(
        {
            "info_list": info_list,
            "tree_embedding": True,
            "logging_level": 3,
            "seed": 42,
            "max_data_size": 1024,
            "objective_type": NUMERIC,
            "parallelism": 4,
            "output_directory": TEST_OUTPUT,
        }
    )

    create_cache(data, settings)


def test_singleton_class_cache():
    data, info_list = load_data("singleton_class.json.gz")

    settings = JobSettings(
        {
            "info_list": info_list,
            "tree_embedding": True,
            "logging_level": 3,
            "seed": 42,
            "max_data_size": 1024,
            "objective_type": CATEGORICAL,
            "parallelism": 4,
            "output_directory": TEST_OUTPUT,
        }
    )

    message = create_cache(data, settings)
    settings.cache_file = message["datasets"][0]
    settings.tree_inputs = message["tree_inputs"]

    X, y, w = read_numpy_arrays(settings)
    assert X.shape[1] == settings.number_of_inputs()


def test_cache_repeatability():
    X1 = np.random.random((16384, 32))
    X2 = np.random.randint(0, 10, (16384, 32))

    y = np.eye(2)[np.random.randint(0, 2, (16384,))]
    w = np.ones((16384, 1))

    for X in [X2, X1]:
        data = np.concatenate([X, y, w], axis=1)
        check_evaluation = None
        check_importance = None

        for i in range(8):
            splits = numpy_split((data, y, w), None, rate=0.2, max_size=4096)
            evaluation_data = splits["validation"][0]

            eX = evaluation_data[:, :32]
            ey = evaluation_data[:, 32:34]
            importance_data = representatives(eX, ey, 128, False, 4242)

            if check_evaluation is None:
                check_evaluation = evaluation_data
                check_importance = importance_data
            else:
                assert np.all(evaluation_data == check_evaluation)
                assert np.all(importance_data == check_importance)


def test_games():
    data = np.load("tests/data/games.npy")
    settings = JobSettings(read_data("games_settings.json.gz"))
    last_reps = None

    for i in range(8):
        reps = choose_representatives(data, settings)
        reps = reps[:, :-1]
        reps = settings.select_data(reps)
        # print(array_hash(reps))

        if last_reps is None:
            last_reps = reps
        else:
            assert np.all(last_reps == reps)
