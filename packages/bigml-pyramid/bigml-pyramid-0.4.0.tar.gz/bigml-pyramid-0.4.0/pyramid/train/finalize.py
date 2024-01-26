import pyramid.importers

np = pyramid.importers.import_numpy()
scistats = pyramid.importers.import_scipy_stats()

from pyramid.serialize.extract import json_from_model_id, json_image_layers

ENSEMBLE_GLOBAL_KEYS = [
    "class_index",
    "optypes",
    "output_exposition",
    "preprocess",
    "weight_index",
]

ATTEMPT_KEYS = [
    "relative_value",
    "evaluation_metrics",
    "iterations",
    "elapsed_time",
]

SUBMODEL_KEYS = ["layers", "trees"]

SEARCH_CONFIGURATION_PARAMETERS = [
    "activation_function",
    "balance_objective",
    "batch_size",
    "descent_algorithm",
    "dropout_rate",
    "loss_function",
    "largest_layer_size",
    "learn_residuals",
    "learning_rate",
    "mixup_alpha",
    "number_of_layers",
    "seed",
    "topology",
    "tree_embedding",
]


def select_config_options(json_model):
    opts = json_model["training_options"]
    return {k: opts[k] for k in SEARCH_CONFIGURATION_PARAMETERS}


def to_submodel(json_model):
    return {k: json_model[k] for k in SUBMODEL_KEYS}


def to_attempt(json_model):
    output = {k: json_model[k] for k in ATTEMPT_KEYS}
    output["configuration_parameters"] = select_config_options(json_model)

    return output


def read_model(settings, id_and_score, as_attempt):
    mid, score = id_and_score

    if as_attempt:
        jmodel = settings.read_fit_info(mid)
    else:
        jmodel = json_from_model_id(settings, mid)

    jmodel["relative_value"] = score
    return jmodel


def read_evaluations(settings):
    model_ids = settings.list_submodels()
    all_jobs = {mid: settings.read_evaluation(mid) for mid in model_ids}

    return {k: v for k, v in all_jobs.items() if v is not None}


def sort_submodels(settings):
    evaluations = read_evaluations(settings)
    model_ids = sorted(evaluations.keys())
    first_evals = evaluations[model_ids[0]]

    metrics = sorted(first_evals[0].keys())
    results_shape = (len(model_ids), len(first_evals), len(metrics))
    ranks = np.zeros(results_shape, dtype=np.float32)

    for i, metric in enumerate(metrics):
        met_results = np.zeros(results_shape[:2], dtype=np.float32)
        for j, model_id in enumerate(model_ids):
            assert len(evaluations[model_id]) == len(first_evals)

            for k, ev in enumerate(evaluations[model_id]):
                met_results[j, k] = ev[metric]

        met_ranks = scistats.rankdata(met_results).reshape(met_results.shape)
        ranks[:, :, i] = met_ranks / np.max(met_ranks)

    mean_ranks = np.mean(ranks, axis=2)
    bottom_evals = np.min(mean_ranks, axis=1).tolist()

    return sorted(zip(model_ids, bottom_evals), key=lambda x: -x[1])


def finalize_search(settings):
    networks = []
    attempts = []
    importances = []
    performances = []

    submodels = sort_submodels(settings)
    nmods = max(1, int((settings.model_fraction or 0.1) * len(submodels)))
    output = None

    for i, id_and_score in enumerate(submodels):
        if i < nmods:
            model = read_model(settings, id_and_score, False)

            performances.append(model["evaluation_metrics"])
            importances.append(model["importances"])
            networks.append(to_submodel(model))

            if output is None:
                output = {k: model[k] for k in ENSEMBLE_GLOBAL_KEYS}
        else:
            model = read_model(settings, id_and_score, True)

        attempts.append(to_attempt(model))

    # Just take the average performance of the searched models
    # selected for inclusion; it's likely to be an underestimate on a
    # true holdout evaluation.
    metrics = sorted(performances[0].keys())
    agg_metrics = {k: np.mean([h[k] for h in performances]) for k in metrics}

    output["networks"] = networks
    output["candidates"] = attempts
    output["importances"] = np.array(importances).mean(axis=0).tolist()
    output["validation_metrics"] = agg_metrics

    return output


def image_network_layers(settings):
    if settings.has_image_inputs():
        model_id = settings.get_image_model_id()
        return json_from_model_id(settings, model_id, image_network=True)
    else:
        return None


def finalize(settings, image_model=False):
    """Get the final, canonical JSON output form of a learned model.

    If a model has been learned using the given `settings`, this
    function will find the learned weights, combine them with the
    given layers, and output a complete model in the expected JSON
    format.  If an image-only model was learned from these settings as
    well (e.g., as a feature extractor in the case of image models
    with more than one input), then passing the optional parameter
    `image_model=True` will return instead the image model trained in
    that "preprocessing" step.

    """
    if settings.is_search and not image_model:
        json_output = finalize_search(settings)
    else:
        if image_model:
            mid = settings.get_image_model_id()
        elif settings.single_image_input_only() and not settings.tree_embedding:
            mid = settings.get_image_model_id()
        else:
            mid = settings.get_job_id()

        json_output = json_from_model_id(settings, mid)

    if not image_model:
        json_output["trees"] = settings.load_trees()
    else:
        json_output["trees"] = None

    json_output["image_network"] = image_network_layers(settings)

    return json_output
