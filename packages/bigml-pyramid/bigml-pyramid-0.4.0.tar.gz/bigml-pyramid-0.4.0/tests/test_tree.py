from sensenet.constants import CATEGORICAL, NUMERIC

import pyramid.importers

np = pyramid.importers.import_numpy()

from pyramid.data.numpy import shape_data
from pyramid.cache.tree import treeify_data
from pyramid.serialize.tree import trees_to_json
from pyramid.settings.job_settings import JobSettings

from .utils import clean_temp, cache_data, TEST_DATA_FILE


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def try_transform(data_file, otype, extra={}):
    info_list = cache_data(data_file)

    settings = {
        "seed": 420,
        "cache_file": TEST_DATA_FILE,
        "info_list": info_list,
        "objective_type": info_list[-1]["type"],
    }

    settings.update(extra)

    js = JobSettings(settings)
    data = np.load(js.cache_file)

    embedding = treeify_data(data, js)
    n_tf = embedding["tree_features"]

    assert data.shape[0] == embedding["data"].shape[0]
    assert n_tf == embedding["data"].shape[1] - data.shape[1]

    obj1 = shape_data(data, js)[1]
    obj2 = shape_data(embedding["data"], js)[1]

    assert obj1.shape == obj2.shape

    if js.objective_type == CATEGORICAL:
        assert np.all(np.sum(obj1, axis=0) == np.sum(obj2, axis=0))

        tree_features = embedding["data"][:, :n_tf]
        assert np.all(tree_features <= 1), tree_features
        assert np.all(tree_features >= 0)
    else:
        s1 = set(obj1.flatten().tolist())
        s2 = set(obj2.flatten().tolist())
        assert len(s1 & s1) == len(s1) == len(s2)

    jout = trees_to_json(embedding, js)
    assert len(jout["importances"]) == jout["tree_features"]

    return embedding, data


def test_iris():
    try_transform("iris.json.gz", CATEGORICAL)


def test_yacht():
    try_transform("yacht.json.gz", NUMERIC)


def test_unique_category():
    data = [
        [1.0, "a"],
        [2.0, "b"],
        [1.0, "c"],
        [2.0, "d"],
        [1.0, "e"],
        [2.0, "f"],
    ]
    embedding, original = try_transform(data, CATEGORICAL)

    assert embedding["data"].shape == original.shape
    assert embedding["tree_features"] == 0


def test_almost_unique_category():
    data = [
        [1.0, "a"],
        [2.0, "a"],
        [1.0, "a"],
        [2.0, "a"],
        [1.0, "e"],
        [2.0, "f"],
    ]
    embedding, original = try_transform(data, CATEGORICAL)

    assert embedding["tree_features"] == 1


def test_one_column():
    data = [
        [1.0, 0.1],
        [2.0, 0.2],
        [1.0, 0.1],
        [2.0, 0.22],
        [1.0, 0.11],
        [2.0, 0.19],
    ]
    embedding, original = try_transform(data, NUMERIC)

    assert embedding["tree_features"] == 1
