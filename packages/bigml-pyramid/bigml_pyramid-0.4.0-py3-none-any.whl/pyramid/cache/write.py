import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import json
import random

from shapsplain.represent import representatives

from pyramid.constants import LOG_PRODUCTION

from pyramid.cache.tree import treeify_data
from pyramid.data.numpy import shape_data
from pyramid.data.stratify import evaluation_set
from pyramid.serialize.tree import trees_to_json
from pyramid.serialize.utils import get_row_size

N_SETS = 8
MAX_DATA_CACHE = 512000000  # Graph limit in tensorflow
MAX_IMPORTANCE_SIZE = 128


def subsample_data(data, size, seed):
    np.random.seed(seed)
    return data[np.random.choice(data.shape[0], size, replace=False), :]


def write_subset(data, size, settings, i):
    sample = subsample_data(data, size, i)
    filename = settings.write_subdataset(sample, i)

    return filename


def choose_representatives(evaluation_data, settings):
    eX, ey, _ = shape_data(evaluation_data, settings)
    balanced = settings.balance_objective is True

    return representatives(eX, ey, MAX_IMPORTANCE_SIZE, balanced, settings.seed)


def write_datasets(data, settings):
    evaluation_data = evaluation_set(data, settings)
    importance_data = choose_representatives(evaluation_data, settings)

    settings.write_evaluation_data(evaluation_data)
    settings.write_importance_data(importance_data)

    if data.nbytes > MAX_DATA_CACHE:
        row_size = get_row_size(settings)
        size = int(max(1, np.floor(512000000 / row_size)))
        sample = subsample_data(data, size, 42)

        return settings.write_full_dataset(sample)
    else:
        return settings.write_full_dataset(data)


def create_cache(data, settings):
    if settings.tree_embedding or settings.is_search:
        embedding = treeify_data(data, settings)
        output_data = embedding["data"]
        tree_features = embedding["tree_features"]

        tree_json = trees_to_json(embedding, settings)
        settings.write_trees(tree_json)
    else:
        tree_features = 0
        output_data = data

    full_datafile = write_datasets(output_data, settings)

    # Memory limit for when we're working in parallel
    max_size = min(
        settings.max_data_size / settings.parallelism, MAX_DATA_CACHE
    )

    if output_data.nbytes > max_size:
        row_size = get_row_size(settings)
        size = int(max(1, np.floor(max_size / row_size)))
        subsets = [write_subset(data, size, settings, i) for i in range(N_SETS)]
    else:
        subsets = []

    return {
        "datasets": [full_datafile] + subsets,
        "full_data_size": int(output_data.nbytes),
        "full_data_shape": [int(s) for s in output_data.shape],
        "row_size": int(output_data[0].nbytes),
        "tree_inputs": tree_features,
    }
