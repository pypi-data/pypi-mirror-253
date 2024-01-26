import json
import hashlib

import pyramid.importers

np = pyramid.importers.import_numpy()

from sensenet.constants import CATEGORICAL, IMAGE

from pyramid.serialize.data import lazy_rows


def maybe_apply_smoothing(y, settings):
    smoothing = settings.label_smoothing_factor

    if smoothing and settings.objective_type == CATEGORICAL:
        nclasses = settings.number_of_classes()

        new_y = np.array(y, copy=True)
        new_y[new_y == 1] = 1 - smoothing
        new_y += smoothing / nclasses

        return new_y
    else:
        return y


def shape_data(data, settings):
    nrows = data.shape[0]
    nclasses = settings.number_of_classes()

    X = data[:, :-nclasses].reshape(nrows, -1)
    y = data[:, -nclasses:].reshape(nrows, nclasses)

    if settings.instance_weights:
        w = np.abs(X[:, -1].reshape((nrows,)))
        X = X[:, :-1].reshape(nrows, -1)
    else:
        w = np.ones((nrows,))

    return X, y, w / np.max(w)


def array_hash(anarray):
    carray = np.ascontiguousarray(anarray)
    return hashlib.sha224(carray.data).hexdigest()


def label_matrix(labels, settings):
    if settings.objective_type == CATEGORICAL:
        n_values = int(np.max(labels) + 1)
        y_matrix = np.eye(n_values)[labels.astype(np.int32)]

        return maybe_apply_smoothing(y_matrix, settings)
    else:
        return labels


def image_dicts_to_numpy(rows, settings):
    nrows = len(rows)
    dkeys = ["file", "label", "weight"]
    X, labels, w = [np.array([r[k] for r in rows]) for k in dkeys]

    X = np.reshape(X, (nrows, -1))
    y = label_matrix(labels, settings)
    y = np.reshape(y, (nrows, -1)).astype(np.float32)
    w = np.abs(w.astype(np.float32))

    return X, y, w / np.max(w)


def image_rows_from_cache(settings):
    types = [f["type"] for f in settings.info_list]
    image_indexes = [i for i, v in enumerate(types) if v == IMAGE]
    nrows = len(image_indexes) * settings.cache_rows

    names = []
    row_idx = 0
    labels = np.zeros((nrows,), dtype=np.float32)
    w = np.zeros((nrows,), dtype=np.float32)

    with open(settings.cache_file, "rb") as fin:
        for row in lazy_rows(fin, settings.info_list, None):
            label = row[-1]
            weight = abs(row[-2]) if settings.instance_weights else 1.0

            for i in image_indexes:
                names.append(str(row[i], "utf-8"))
                labels[row_idx] = label
                w[row_idx] = weight

                row_idx += 1

    X = np.array(names).reshape(nrows, 1)
    y = label_matrix(labels, settings)
    y = np.reshape(y, (nrows, -1)).astype(np.float32)

    return X, y, w / np.max(w)


def read_numpy_arrays(settings):
    if settings.cache_file.endswith(".npy"):
        data = np.load(settings.cache_file)
        X, y, w = shape_data(data, settings)

        X = settings.select_data(X)
        y = maybe_apply_smoothing(y, settings)

        return X, y, w
    elif settings.is_image_training_job():
        if settings.image_training_data is not None:
            return image_dicts_to_numpy(settings.image_training_data, settings)
        elif settings.cache_file.endswith(".json"):
            with open(settings.cache_file, "r") as fin:
                rows = json.load(fin)

            return image_dicts_to_numpy(rows, settings)
        elif settings.cache_file.endswith(".ser"):
            return image_rows_from_cache(settings)
        else:
            raise ValueError(
                "Not sure what to do with cache file %s" % settings.cache_file
            )
    else:
        raise ValueError("Invalid cache file %s" % settings.cache_file)
