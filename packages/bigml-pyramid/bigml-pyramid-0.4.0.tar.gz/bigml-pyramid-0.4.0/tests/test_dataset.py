import os

from sensenet.constants import NUMERIC, CATEGORICAL, MEAN, STANDARD_DEVIATION

import pyramid.importers

np = pyramid.importers.import_numpy()

from pyramid.settings.job_settings import JobSettings
from pyramid.data.numpy import shape_data, read_numpy_arrays
from pyramid.data.dataset import make_dataset

from .utils import clean_temp, TEST_DATA_FILE

DATASET_INFO = [
    {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
    {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
    {"type": CATEGORICAL, "values": ["a", "b", "c"]},
    {"type": CATEGORICAL, "values": ["a", "b", "c", "d", "e", "f"]},
    {"type": CATEGORICAL, "values": ["a", "b"]},
    {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
    {"type": CATEGORICAL, "values": ["a", "b", "c"]},
]


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def make_data(nrows, settings):
    X = None

    for i, info in enumerate(settings.info_list):
        if info["type"] == CATEGORICAL:
            nvals = len(info["values"])
            categories = np.random.randint(0, nvals, (nrows,))
            vals = np.eye(nvals)[categories]
        else:
            vals = np.random.random((nrows, 1))

            if i == len(settings.info_list) - 1:
                vals = vals - 100

        if X is None:
            X = vals
        else:
            X = np.hstack((X, vals))

    return X


def check_data(tensors, nrows, nclasses, has_weights):
    X, y, w = tensors

    for t in [X, y]:
        assert len(t.shape) == 2
        assert t.shape[0] == nrows, str((t.shape, nrows))

    assert len(w.shape) == 1, w.shape
    assert w.shape == (nrows,)
    assert y.shape[1] == nclasses, str((y.shape, nclasses))

    if nclasses > 1:
        assert np.all(np.isin(y, [0, 1]))
    else:
        assert np.all(y < 0)

    if not has_weights:
        assert np.all(w == 1), w
    else:
        assert not np.all(w == 1), w


def check_dataset(nrows, batch_rows, ds_info):
    if ds_info[-1]["type"] == CATEGORICAL:
        nclasses = len(ds_info[-1]["values"])
    else:
        nclasses = 1

    for wts in [False, True]:
        js = JobSettings(
            {
                "info_list": ds_info,
                "objective_type": ds_info[-1]["type"],
                "instance_weights": wts,
                "batch_size": batch_rows,
                "seed": 5,
            }
        )

        data = make_data(nrows, js)
        np.save(TEST_DATA_FILE, data)
        js.cache_file = TEST_DATA_FILE

        tensors = read_numpy_arrays(js)
        check_data(tensors, nrows, nclasses, wts and nrows > 1)

        dataset = make_dataset(js, tensors)

        for batch in dataset.take(256).as_numpy_iterator():
            assert len(batch) == 3
            check_data(batch, batch_rows, nclasses, wts and nrows > 1)


def test_dataset_sanity():
    check_dataset(128, 11, DATASET_INFO)


def test_single_row():
    check_dataset(1, 50, DATASET_INFO)


def test_single_column():
    reg_list = [
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
    ]

    check_dataset(10, 11, reg_list)
    check_dataset(1, 11, reg_list)

    cat_list = [
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": CATEGORICAL, "values": ["a", "b", "c", "d", "e", "f"]},
    ]

    check_dataset(20, 21, cat_list)


def test_balanced_dataset():
    ds_info = [
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": CATEGORICAL, "values": ["yes", "no"]},
    ]

    data = np.array(
        [
            [1, 2, 0, 1],
            [3, 4, 0, 1],
            [5, 6, 0, 1],
            [7, 8, 0, 1],
            [9, 0, 0, 1],
            [0, 1, 0, 1],
            [2, 3, 0, 1],
            [4, 5, 0, 1],
            [6, 7, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=np.float32,
    )

    js = JobSettings(
        {
            "info_list": ds_info,
            "objective_type": CATEGORICAL,
            "batch_size": 100,
            "seed": 3,
        }
    )

    np.save(TEST_DATA_FILE, data)
    js.cache_file = TEST_DATA_FILE
    tensors = read_numpy_arrays(js)

    dataset = make_dataset(js, tensors)
    nrare = 0

    for batch in dataset.take(100).as_numpy_iterator():
        nrare += np.sum(batch[1][:, 0])

    assert 980 < nrare < 1020, nrare

    js.balance_objective = True
    bal_dataset = make_dataset(js, tensors)
    nrare = 0

    for batch in bal_dataset.take(100).as_numpy_iterator():
        nrare += np.sum(batch[1][:, 0])

    assert 4900 < nrare < 5100, nrare


def test_mixup_dataset():
    ds_info = [
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": NUMERIC, MEAN: 0, STANDARD_DEVIATION: 1},
        {"type": CATEGORICAL, "values": ["yes", "no"]},
    ]

    data = np.array(
        [
            [100, 2, 0, 1],
            [300, 4, 0, 1],
            [500, 6, 0, 1],
            [700, 8, 0, 1],
            [900, 0, 0, 1],
            [1000, 1, 0, 1],
            [2000, 3, 0, 1],
            [400, 5, 0, 1],
            [600, 7, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=np.float32,
    )

    js = JobSettings(
        {
            "info_list": ds_info,
            "objective_type": CATEGORICAL,
            "instance_weights": False,
            "batch_size": 100,
            "seed": 2,
        }
    )

    np.save(TEST_DATA_FILE, data)
    js.cache_file = TEST_DATA_FILE
    tensors = read_numpy_arrays(js)

    nclasses = len(ds_info[-1]["values"])
    nrows = js.batch_size

    for alpha, bounds in zip([0.1, 0.2, 0.3], [(10, 30), (30, 50), (50, 70)]):
        js.mixup_alpha = alpha
        dataset = make_dataset(js, tensors)

        mixmin, mixmax = bounds
        nbatches = 20
        nmixed = 0
        nsmall = 0
        nlarge = 0

        for batch in dataset.take(nbatches):
            X, y, w = batch

            for t in [X, y]:
                assert len(t.shape) == 2
                assert t.shape[0] == nrows, str((t.shape, nrows))

            assert len(w.shape) == 1, w.shape
            assert w.shape == (nrows,)
            assert y.shape[1] == nclasses, str((y.shape, nclasses))

            assert np.all((y >= 0) & (y <= 1))
            assert np.all(np.sum(y, axis=1) == 1), np.sum(y, axis=1)
            assert np.any((y > 0) & (y < 1))

            for i in range(X.shape[0]):
                if y[i, 1] > 0.7:
                    assert X[i, 0] > 70, X[i, 0]
                    nlarge += 1
                elif y[i, 1] < 0.1:
                    assert X[i, 0] < 200, X[i, 0]
                    nsmall += 1

            nmixed += np.sum((y >= 0.2) & (y <= 0.8))

        assert nlarge > 100
        assert nsmall > 100

        assert mixmin < nmixed // nbatches < mixmax
