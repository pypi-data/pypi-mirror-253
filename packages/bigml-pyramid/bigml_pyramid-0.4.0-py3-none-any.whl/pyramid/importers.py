"""Namespace just for importing other namespaces to avoid spamming of
various messages on import.

"""
import sys
import os
import logging
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Errors only

logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.WARNING)

warnings.filterwarnings("ignore", message=".*_learning_phase` is deprecated.*")

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message=".*as a synonym of type.*")
    import tensorflow

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", message=".*binary incompatibility.*")
    import numpy
    import scipy
    import sklearn

    import scipy.stats
    import scipy.special

    import sklearn.tree
    import sklearn.ensemble
    import sklearn.cluster
    import sklearn.metrics

gpus = tensorflow.config.list_physical_devices("GPU")

if gpus:
    tensorflow.config.experimental.set_memory_growth(gpus[0], True)


def import_tensorflow():
    return tensorflow


def import_numpy():
    return numpy


def import_scipy_stats():
    return scipy.stats


def import_scipy_special():
    return scipy.special


def import_sk_metrics():
    return sklearn.metrics


def import_sklearn_tree():
    return sklearn.tree


def import_sklearn_ensemble():
    return sklearn.ensemble


def import_sklearn_cluster():
    return sklearn.cluster
