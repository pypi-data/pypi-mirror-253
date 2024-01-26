import pyramid.importers

np = pyramid.importers.import_numpy()
sci_stats = pyramid.importers.import_scipy_stats()
skmets = pyramid.importers.import_sk_metrics()

import warnings

FLIPPED_SIGN_METRICS = [
    "mean_squared_error",
    "mean_absolute_error",
    "median_absolute_error",
]


def flip_signs(metrics):
    for m in metrics:
        if m in FLIPPED_SIGN_METRICS:
            metrics[m] = float(-metrics[m])
        else:
            metrics[m] = float(metrics[m])

    return metrics


def regression_metrics(y_true, y_score):
    pass


def accuracy(y_true, y_score):
    maxes = np.max(y_score, axis=1).reshape(-1, 1)
    y_pred = y_score == np.tile(maxes, (1, y_score.shape[1]))

    return skmets.accuracy_score(y_true, y_pred)


def safe_auc(y_true, y_score):
    try:
        return skmets.roc_auc_score(y_true, y_score, multi_class="ovr")
    except ValueError:
        return 0.0


def exp_log_loss(y_true, y_score):
    log_loss = skmets.log_loss(y_true, y_score)
    # This is really just so this value scales more nicely.  This makes
    # it something like the harmonic mean of all probabilities for the
    # correct classes
    return np.exp(-log_loss)


def max_phi(truth, scores):
    pos_count = np.sum(truth == 1)
    neg_count = np.sum(truth == 0)

    # If there's a missing class in the evaluation set, a warning about
    # the meaninglessness of the curve is printed
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=".*value should be.*")
        fpr, tpr, threshold = skmets.roc_curve(truth, scores)

    tp = tpr * pos_count
    fp = fpr * neg_count
    tn = neg_count - fp
    fn = pos_count - tp

    denom = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    # This will always trigger, because either end of the curve is
    # all one class, so the denominator there is zero
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", message=".*true_divide.*")
        phis = (tp * tn - fp * fn) / denom

    phis = phis[np.isfinite(phis)]

    if len(phis) > 0:
        return np.max(phis)
    else:
        return None


def ndcg(truth, scores):
    return skmets.ndcg_score(truth.reshape(1, -1), scores.reshape(1, -1))


def macro_average(score_fn, y_true, y_score):
    values = []

    if y_score.shape[1] == 2:
        ivalues = [0, 1]
    elif y_score.shape[1] > 2:
        ivalues = list(range(y_score.shape[1]))
    else:
        raise ValueError("Shape of scores is %s" % str(y_score.shape))

    for i in ivalues:
        metric = score_fn(y_true[:, i], y_score[:, i])

        if metric is not None:
            values.append(metric)

    if len(values) > 0:
        return np.mean(values)
    else:
        return 0


def classification_metrics(y_true, y_score):
    nclasses = y_true.shape[1]

    if nclasses == 1:
        # Degenerate case
        metrics = ["max_phi", "ndcg", "accuracy", "likelihood", "auc"]
        return {k: 1.0 for k in metrics}
    else:
        classes = np.argmax(y_true, axis=-1)

        # In the case of label smoothing, we need to binarize the
        # labels, and if there is no smoothing, this returns y_true
        y_true_nosmooth = np.eye(nclasses)[classes]

        return {
            "max_phi": macro_average(max_phi, y_true_nosmooth, y_score),
            "ndcg": macro_average(ndcg, y_true_nosmooth, y_score),
            "accuracy": accuracy(y_true_nosmooth, y_score),
            "likelihood": exp_log_loss(y_true_nosmooth, y_score),
            "auc": safe_auc(y_true_nosmooth, y_score),
        }


def safe_spearman(y_true, y_score):
    n = len(y_true)

    if n > 1:
        r_true = sci_stats.rankdata(y_true)
        r_pred = sci_stats.rankdata(y_score)

        return 1 - (np.sum(np.square(r_true - r_pred)) * 6) / (n * (n * n - 1))
    else:
        return 0.0


def safe_r2(y_true, y_score):
    if len(y_true) > 1:
        return skmets.r2_score(y_true, y_score)
    else:
        return 0.0


def regression_metrics(y_true, y_score):
    metrics = {
        "mean_squared_error": skmets.mean_squared_error(y_true, y_score),
        "mean_absolute_error": skmets.mean_absolute_error(y_true, y_score),
        "median_absolute_error": skmets.median_absolute_error(y_true, y_score),
        "r_squared": safe_r2(y_true, y_score),
        "spearman_r": safe_spearman(y_true, y_score),
    }

    return flip_signs(metrics)
