"""Functions for learning tree embeddings

The functions herein are able to learn a quick tree-based
representation of the input data, based on slices of the feature
space.  The learned features are likely to have a montonic
relationship with the objective, and so using these features as input
to the network may significantly simplify gradient descent and speed
up training.

"""
import pyramid.importers

np = pyramid.importers.import_numpy()
sktree = pyramid.importers.import_sklearn_tree()
sken = pyramid.importers.import_sklearn_ensemble()

from sensenet.constants import NUMERIC, CATEGORICAL

from pyramid.data.stratify import to_class_list, split_raw_data
from pyramid.data.numpy import shape_data

MAX_TREE_POINTS = 1024
MIN_TREE_FEATURES = 3
MIN_LEAF_SAMPLES = 16
N_TREES = 8


def learn_ensemble(X, y, settings):
    if settings.objective_type == CATEGORICAL:
        ensemble = sken.RandomForestClassifier(
            n_estimators=N_TREES,
            min_samples_leaf=MIN_LEAF_SAMPLES,
            n_jobs=-1,
            class_weight="balanced",
            random_state=settings.seed,
        )
    else:
        ensemble = sken.RandomForestRegressor(
            n_estimators=N_TREES,
            min_samples_leaf=MIN_LEAF_SAMPLES,
            n_jobs=-1,
            random_state=settings.seed,
        )

    ensemble.fit(X, y)
    return ensemble


def combine_forests(rf_a, rf_b):
    half = int(len(rf_a.estimators_) / 2)
    a_est = rf_a.estimators_[:half]
    b_est = rf_b.estimators_[half:]

    rf_a.estimators_ = a_est + b_est
    rf_a.n_estimators = len(rf_a.estimators_)

    return rf_a


def get_embedding(X, model):
    if isinstance(model, sken.RandomForestClassifier):
        return model.predict_proba(X).astype(np.float32)
    elif isinstance(model, sken.RandomForestRegressor):
        return model.predict(X).astype(np.float32)
    else:
        raise ValueError("Model is unknown type!")


def tree_transform(trees, data):
    outdata = None

    for feature_range, model in trees:
        sidx, eidx = feature_range
        inputs = data[:, sidx:eidx]
        outarray = get_embedding(inputs, model)

        if outdata is not None:
            outdata = np.c_[outdata, outarray]
        else:
            outdata = outarray

    if outdata is None:
        return data
    else:
        if len(outdata.shape) == 1:
            outdata = outdata.reshape(-1, 1)

        return np.c_[outdata, data]


def get_windows(settings):
    n_features = settings.number_of_inputs(original_only=True)
    n_mods = int(settings.tree_features() / settings.number_of_classes())

    stride = float(n_features) / n_mods
    stride_features = max(MIN_TREE_FEATURES, int(np.ceil(stride)))

    starts = [
        min(n_features - 1, int(round(i * stride))) for i in range(n_mods)
    ]
    ends = [min(n_features, s + stride_features) for s in starts]

    return starts, ends


def objective_column(data1, data2, settings):
    y1 = shape_data(data1, settings)[1]
    y2 = shape_data(data2, settings)[1]

    if settings.objective_type == CATEGORICAL:
        y1 = np.array(to_class_list(y1)).reshape(-1)
        y2 = np.array(to_class_list(y2)).reshape(-1)

        # Check to make sure the two subsets have the same classes
        classes1 = set(y1)
        classes2 = set(y2)

        if classes1 == classes2:
            return data1, y1, data2, y2
        else:
            joint = np.array(list(classes1 & classes2))
            idxs1 = np.isin(y1, joint)
            idxs2 = np.isin(y2, joint)

            return data1[idxs1], y1[idxs1], data2[idxs2], y2[idxs2]
    else:
        return data1, y1.reshape(-1), data2, y2.reshape(-1)


def learn_embedding(data, settings):
    trees1 = []
    trees2 = []

    starts, ends = get_windows(settings)
    split1, split2 = split_raw_data(data, settings, 0.5, MAX_TREE_POINTS)

    if split1.shape[0] > 0 and split2.shape[0] > 0:
        data1, y1, data2, y2 = objective_column(split1, split2, settings)

        if data1.shape[0] > 0 and data2.shape[0] > 0:
            for sidx, eidx in zip(starts, ends):
                eX1 = data1[:, sidx:eidx]
                eX2 = data2[:, sidx:eidx]

                ens1 = learn_ensemble(eX1, y1, settings)
                ens2 = learn_ensemble(eX2, y2, settings)

                trees1.append([[sidx, eidx], ens1])
                trees2.append([[sidx, eidx], ens2])

    tdata1 = tree_transform(trees2, split1)
    tdata2 = tree_transform(trees1, split2)
    tdata = np.vstack([tdata1, tdata2])

    all_trees = []
    for t1, t2 in zip(trees1, trees2):
        all_trees.append([t1[0], combine_forests(t1[1], t2[1])])

    return {
        "trees": all_trees,
        "data": tdata,
        "tree_features": tdata.shape[1] - data.shape[1],
    }


def treeify_data(data, settings):
    heldout, train = split_raw_data(data, settings, 0.5, 2 * MAX_TREE_POINTS)

    embedding = learn_embedding(train, settings)
    transformed = tree_transform(embedding["trees"], heldout)
    newdata = np.vstack([embedding["data"], transformed])

    embedding["data"] = newdata

    return embedding
