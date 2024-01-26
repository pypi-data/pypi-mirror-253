import os
import json
import time

import pyramid.importers

np = pyramid.importers.import_numpy()

from nose import with_setup

from sensenet.constants import CATEGORICAL, NUMERIC
from sensenet.models.wrappers import create_model

from pyramid.cache.write import write_datasets, create_cache
from pyramid.data.numpy import read_numpy_arrays
from pyramid.settings.base_settings import SEARCH_SUBMODEL
from pyramid.settings.job_settings import JobSettings
from pyramid.settings.job_settings import EVALUATION_DATASET, FULL_DATASET
from pyramid.train.finalize import finalize
from pyramid.train.model import fit
from pyramid.train.model import N_EVALUATION_SAMPLES
from pyramid.train.metrics import exp_log_loss, safe_auc, safe_r2

from .utils import TEST_DATA_FILE, TEST_MODEL_FILE, TEST_OUTPUT
from .utils import clean_temp, cache_data, read_data, load_data


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def make_model_dir(settings):
    try:
        os.mkdir(os.path.join(TEST_OUTPUT, settings.model_directory(None)))
    except FileExistsError:
        pass


def check_format(jout, info_list):
    assert jout["class_index"] == len(info_list) - 1
    assert len(jout["preprocess"]) == len(info_list) - 1
    assert len(jout["optypes"]) == len(info_list)
    assert len(jout["importances"]) == len(info_list) - 1, jout["importances"]

    for key in ["weight_index", "training_options", "iterations"]:
        assert key in jout


def check_layers(layers):
    for layer in layers:
        if "weights" in layer:
            assert type(layer["weights"]) == list
            assert type(layer["offset"]) == list
            assert type(layer["weights"][0][0]) == float
            assert type(layer["offset"][0]) == float

        assert "seed" not in layer
        assert "number_of_nodes" not in layer
        assert "number_of_filters" not in layer
        assert "kernel_dimensions" not in layer


def check_evaluation(settings, all_evals):
    assert len(all_evals) == N_EVALUATION_SAMPLES
    assert any([e != all_evals[0] for e in all_evals])

    if settings.job_id != "skip_eval":
        if settings.objective_type == CATEGORICAL:
            for e in all_evals:
                assert 0.9 <= e["accuracy"] <= 1.0, e
                assert 0.7 <= e["likelihood"] <= 1.0, e
        elif settings.objective_type == NUMERIC:
            for e in all_evals:
                assert 0.9 <= e["r_squared"] <= 1.0, e
                assert 0.8 <= e["spearman_r"] <= 1.0, e
        else:
            raise ValueError(settings.objective_type)


def match_layers(layers1, layers2):
    for layer, olayer in zip(layers1, layers2):
        assert type(layer) == type(olayer), (type(layer), type(olayer))
        assert len(layer.get_weights()) == len(olayer.get_weights())

        for w, jw in zip(layer.get_weights(), olayer.get_weights()):
            assert np.sum(w - jw) == 0


def objective(info_list):
    if info_list[-1]["type"] == CATEGORICAL:
        return "crossentropy"
    else:
        return "mean_squared_error"


def make_layers(noutputs, use_dropout):
    layers = [
        {
            "type": "dense",
            "number_of_nodes": 16,
            "seed": 0,
            "weights": "glorot_uniform",
            "offset": "zeros",
            "activation_function": "relu",
        },
        {
            "beta": "zeros",
            "gamma": "ones",
            "mean": "zeros",
            "type": "batch_normalization",
            "variance": "ones",
        },
        {
            "type": "dense",
            "number_of_nodes": noutputs,
            "seed": 0,
            "weights": "glorot_uniform",
            "offset": "zeros",
            "activation_function": "softmax" if noutputs > 1 else "identity",
        },
    ]

    if use_dropout:
        layers = [
            layers[0],
            layers[1],
            {"type": "dropout", "dropout_type": "zero", "rate": 0.5},
            layers[2],
        ]

    return layers


def model_settings(cache_file, info_list, noutputs, use_dropout=False):
    otype = info_list[-1]["type"]

    settings = {
        "seed": 420,
        "max_iterations": 256,
        "cache_file": cache_file,
        "info_list": info_list,
        "learning_rate_warmup_iterations": 8,
        "descent_algorithm": "adam",
        "job_id": "test_model",
        "tree_embedding": False,
        "is_search": False,
        "batch_size": 32,
        "output_directory": TEST_OUTPUT,
        "learning_rate": 1e-2,
        "loss_function": objective(info_list),
        "objective_type": otype,
        "logging_level": None,
        "layers": make_layers(noutputs, use_dropout),
        "job_type": SEARCH_SUBMODEL,
    }

    return settings


def model_dropout(data_file, noutputs):
    raw_data = read_data(data_file)
    info_list = cache_data(data_file)

    cache_file = TEST_DATA_FILE
    settings = model_settings(cache_file, info_list, noutputs, use_dropout=True)

    js = JobSettings(settings)
    js.start_time = time.time()
    make_model_dir(js)

    if cache_file == TEST_DATA_FILE:
        write_datasets(np.load(cache_file), js)

    layers = js.layers
    model = js.make_model(False)
    fit_info, evaluations = fit(model, js)

    js.label_smoothing_factor = 0.0
    arrays = read_numpy_arrays(js)
    X, y_true, _ = arrays
    y_score1 = model.predict(X)

    js.write_network(model, fit_info, evaluations)
    joutput = finalize(js)

    assert len(js.layers) == 4
    assert len(joutput["layers"]) == 3
    assert any([l["type"] == "dropout" for l in js.layers])
    assert not any([l["type"] == "dropout" for l in joutput["layers"]])

    created_model = create_model(joutput, {"regression_normalize": True})
    y_score2 = created_model(raw_data)

    assert np.sum(np.abs(y_score1 - y_score2)) == 0, np.abs(y_score1 - y_score2)


def model_and_check(cache_file, info_list, noutputs, extra):
    settings = model_settings(cache_file, info_list, noutputs)
    settings.update(extra)

    js = JobSettings(settings)
    js.start_time = time.time()
    make_model_dir(js)

    if cache_file == TEST_DATA_FILE:
        write_datasets(np.load(cache_file), js)

    layers = js.layers
    model = js.make_model(False)
    fit_info, evaluations = fit(model, js)
    importances = fit_info["importances"]

    assert abs(np.sum(importances) - 1.0) < 1e-6

    js.label_smoothing_factor = 0.0
    arrays = read_numpy_arrays(js)
    X, y_true, _ = arrays
    y_score1 = model.predict(X)

    js.write_network(model, fit_info, evaluations)
    joutput = finalize(js)
    check_format(joutput, info_list)

    remodel = js.make_model(True)
    y_score2 = remodel.predict(X)
    match_layers(model.layers, remodel.layers)

    # The fitted model and the reconstituted model should be different
    # in some way
    assert model != remodel

    # But predictions should be the same
    # (aside - I can't believe they're exactly equal in all cases)
    assert np.array_equal(y_score1, y_score2)

    read_evaluations = js.read_evaluation(js.job_id)
    check_layers(joutput["layers"])
    check_evaluation(js, read_evaluations)

    return joutput, y_true, y_score1


def try_modeling(data_file, extra):
    noutputs = 1
    info_list = cache_data(data_file)

    if info_list[-1]["type"] == CATEGORICAL:
        noutputs = len(info_list[-1]["values"])

    return model_and_check(TEST_DATA_FILE, info_list, noutputs, extra)


def try_replication(data_file, metric, threshold, extra):
    model, y_true, y_score = try_modeling(data_file, extra)
    _, _, y_score_replicate = try_modeling(data_file, extra)

    assert np.sum(np.abs(y_score - y_score_replicate)) == 0
    assert metric(y_true, y_score) > threshold, metric(y_true, y_score)

    return model, y_true, y_score


@with_setup(clean_temp, clean_temp)
def test_good_old_iris():
    model, y_true, y_score = try_modeling("iris.json.gz", {})
    _, _, y_score_replicate = try_modeling("iris.json.gz", {})
    _, _, y_score_different = try_modeling("iris.json.gz", {"seed": 0})

    assert np.sum(np.abs(y_score - y_score_replicate)) == 0
    assert np.sum(np.abs(y_score - y_score_different)) > 0

    assert exp_log_loss(y_true, y_score) > 0.9, exp_log_loss(y_true, y_score)


@with_setup(clean_temp, clean_temp)
def test_good_old_yacht():
    settings = {"max_iterations": 512}
    try_replication("yacht.json.gz", safe_r2, 0.9, settings)


@with_setup(clean_temp, clean_temp)
def test_wide():
    settings = {"max_iterations": 256, "job_id": "skip_eval"}
    try_replication("wide.json.gz", exp_log_loss, -1, settings)


@with_setup(clean_temp, clean_temp)
def test_balanced_iris():
    settings = {"balance_objective": True}
    try_replication("iris.json.gz", exp_log_loss, 0.9, settings)


@with_setup(clean_temp, clean_temp)
def test_mixup_iris():
    settings = {"mixup_alpha": 0.2, "max_iterations": 384}
    try_replication("iris.json.gz", exp_log_loss, 0.8, settings)


@with_setup(clean_temp, clean_temp)
def test_mixup_yacht():
    settings = {"mixup_alpha": 0.2, "max_iterations": 512}
    try_replication("yacht.json.gz", safe_r2, 0.9, settings)


@with_setup(clean_temp, clean_temp)
def test_tiny():
    settings = {"max_iterations": 512}
    try_replication("singleton_class.json.gz", exp_log_loss, 0.9, settings)


@with_setup(clean_temp, clean_temp)
def test_label_smoothing():
    settings = {"label_smoothing_factor": 0.03, "max_iterations": 512}
    _, y_, scores1 = try_replication("iris.json.gz", safe_auc, 0.9, settings)
    sum1 = np.sum(scores1[np.arange(len(scores1)), np.argmax(y_, axis=-1)])

    settings = {"label_smoothing_factor": 0.3, "max_iterations": 512}
    _, y_, scores2 = try_replication("iris.json.gz", safe_auc, 0.9, settings)
    sum2 = np.sum(scores2[np.arange(len(scores2)), np.argmax(y_, axis=-1)])

    # probabilities of the correct class should be closer to zero in
    # the smoothed model
    assert (sum1 - sum2) > 20, sum1 - sum2


@with_setup(clean_temp, clean_temp)
def test_nan_loss():
    # Change logging level to 1 to see NaN warning
    settings = {
        "learning_rate": 1e10,
        "logging_level": None,
        "job_id": "skip_eval",
    }

    _, y_, scores1 = try_replication("yacht.json.gz", safe_auc, -1, settings)


@with_setup(clean_temp, clean_temp)
def test_dropout_categorical():
    model_dropout("iris.json.gz", 3)


@with_setup(clean_temp, clean_temp)
def test_dropout_numeric():
    model_dropout("yacht.json.gz", 1)


@with_setup(clean_temp, clean_temp)
def test_treeified_yacht():
    data, info_list = load_data("yacht.json.gz")

    settings = JobSettings(
        {
            "info_list": info_list,
            "tree_embedding": True,
            "logging_level": 3,
            "seed": 42,
            "max_data_size": 1024000000,
            "objective_type": NUMERIC,
            "parallelism": 4,
            "output_directory": TEST_OUTPUT,
        }
    )

    cache_message = create_cache(data, settings)
    cache_file = os.path.join(settings.output_directory, FULL_DATASET)

    for embed in [True, False]:
        amap = {
            "tree_embedding": embed,
            "max_iterations": 512,
            "tree_inputs": cache_message["tree_inputs"],
        }

        model_and_check(cache_file, info_list, 1, amap)
