import random

import pyramid.importers

np = pyramid.importers.import_numpy()

from sensenet.constants import BOUNDING_BOX

from pyramid.data.numpy import shape_data

MAX_HOLDOUT = 4096
DEFAULT_HOLDOUT_RATE = 0.2


def to_class_list(y):
    return np.squeeze(np.argmax(y, 1)).reshape(-1).tolist()


def class_index_arrays(class_list):
    classes = set(int(c) for c in class_list)
    class_lists = {cls: list() for cls in classes}

    for i, c in enumerate(class_list):
        class_lists[c].append(i)

    return class_lists


def class_indices(y):
    if y.shape[1] == 1:
        return {0: list(range(y.shape[0]))}
    else:
        class_list = to_class_list(y)
        return class_index_arrays(to_class_list(y))


def split_by_class(arrays):
    X, y, w = arrays
    class_lists = class_indices(y)

    splits = []

    for cls in sorted(class_lists.keys()):
        idxs = np.array(class_lists[cls])
        splits.append((X[idxs, :], y[idxs, :], w[idxs]))

    return splits


def get_holdout(class_lists, nrows, max_rate, limit, rng):
    rate = min(max_rate, limit / float(nrows))

    validation_idxs = []

    for cls in sorted(class_lists.keys()):
        rng.shuffle(class_lists[cls])
        # Assure at least one point from each class is in the validation set
        npoints = max(1, int(round(len(class_lists[cls]) * rate)))
        validation_idxs.extend(class_lists[cls][:npoints])

    return validation_idxs


def split_indices(class_lists, settings, nrows, rate, max_size):
    max_rate = rate or settings.holdout_rate or DEFAULT_HOLDOUT_RATE
    limit = max_size or settings.holdout_set_size or MAX_HOLDOUT

    seed = settings.seed if settings is not None else 0
    rng = random.Random(seed)

    validation_idxs = get_holdout(class_lists, nrows, max_rate, limit, rng)
    validation_set = set(validation_idxs)

    training_idxs = []

    for i in range(nrows):
        if i not in validation_set:
            training_idxs.append(i)

    return training_idxs, sorted(validation_idxs)


def numpy_split(arrays, settings, rate=None, max_size=None):
    """Split dataset into two sets, maintaining class distribution of each"""

    X, y, w = arrays
    nrows = X.shape[0]
    class_lists = class_indices(y)
    tidxs, vidxs = split_indices(class_lists, settings, nrows, rate, max_size)

    tis = np.array(tidxs)
    vis = np.array(vidxs)

    if tis.shape[0] > 0:
        return {
            "training": (arrays[0][tis, :], arrays[1][tis, :], arrays[2][tis]),
            "validation": (
                arrays[0][vis, :],
                arrays[1][vis, :],
                arrays[2][vis],
            ),
        }
    else:
        emptyX = np.zeros((0, arrays[0].shape[1]), dtype=np.float32)
        emptyy = np.zeros((0, arrays[1].shape[1]), dtype=np.float32)
        emptyw = np.zeros((0,), dtype=np.float32)

        return {"training": (emptyX, emptyy, emptyw), "validation": arrays}


def bounding_box_class_vector(arrays, settings):
    class_counts = [0] * settings.number_of_classes()

    for point in arrays:
        if len(point[1]) > 0:
            for box in point[1]:
                class_counts[box[4]] += 1

    y = []

    for point in arrays:
        if len(point[1]) == 0:
            y.append(-1)
        elif len(point[1]) == 1:
            y.append(box[4])
        else:
            min_class = None
            min_count = float("inf")

            for box in point[1]:
                if class_counts[box[4]] < min_count:
                    min_class = box[4]
                    min_count = class_counts[box[4]]

            y.append(min_class)

    return y


def split_bounding_box_data(arrays, settings):
    y = bounding_box_class_vector(arrays, settings)
    class_lists = class_index_arrays(y)
    tidxs, vidxs = split_indices(class_lists, settings, len(y), None, None)
    validation_indices = set(vidxs)

    training = []
    validation = []

    for i, point in enumerate(arrays):
        if i in validation_indices:
            validation.append(point)
        else:
            training.append(point)

    return {"training": training, "validation": validation}


def stratified_split(arrays, settings):
    if settings.objective_type == BOUNDING_BOX:
        return split_bounding_box_data(arrays, settings)
    else:
        return numpy_split(arrays, settings)


def split_raw_data(data, settings, rate, size):
    X, y, w = shape_data(data, settings)
    splits = numpy_split((data, y, w), settings, rate=rate, max_size=size)

    return splits["training"][0], splits["validation"][0]


def evaluation_set(data, settings):
    if data.shape[0] < MAX_HOLDOUT:
        return data
    else:
        max_rate = min(1.0, MAX_HOLDOUT / data.shape[0])
        return split_raw_data(data, settings, max_rate, MAX_HOLDOUT)[1]
