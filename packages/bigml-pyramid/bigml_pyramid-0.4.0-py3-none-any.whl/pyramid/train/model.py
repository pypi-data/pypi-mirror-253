import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import random
import time

from sensenet.constants import CATEGORICAL, NUMERIC, BOUNDING_BOX, IMAGE
from sensenet.models.image import get_image_layers, get_image_layer_boundary

from pyramid.constants import LOG_TENSORFLOW

from pyramid.data.dataset import make_dataset, create_splits
from pyramid.data.stratify import stratified_split, class_indices, get_holdout
from pyramid.data.stratify import DEFAULT_HOLDOUT_RATE
from pyramid.settings.objectives import create_objective
from pyramid.settings.optimizers import create_optimizer
from pyramid.train.callbacks import PyramidController
from pyramid.train.importances import compute_importances
from pyramid.train.metrics import classification_metrics, regression_metrics

N_EVALUATION_SAMPLES = 128
MAX_EVALUATION_SAMPLE_SIZE = 256

SANITY_EPOCHS = 256000
EPOCH_STEPS = 32


def choose_metrics(settings):
    if settings.objective_type == CATEGORICAL:
        return ["accuracy"]
    elif settings.objective_type == NUMERIC:
        return ["mean_absolute_error"]
    elif settings.objective_type == BOUNDING_BOX:
        return []
    else:
        raise ValueError("Objective is %s" % settings.objective_type)


def train_phase(model, settings, dataset, callbacks, learning_rate):
    verbosity = 1 if settings.logging_level == LOG_TENSORFLOW else 0

    settings.log_setup("Compiling model...")
    model.compile(
        optimizer=create_optimizer(settings, learning_rate),
        loss=create_objective(settings),
        metrics=choose_metrics(settings),
    )

    callbacks[0].log_message("Fitting with learning rate %f..." % learning_rate)
    model.fit(
        x=dataset,
        # We're setting steps_per_epoch to a small value here
        # due to a bug in tensorflow, whereby the model will
        # only stop training at the end of an epoch when the
        # callback sets `model.stop_training = True`.  If/when
        # this bug is fixed, the number of steps can be
        # increased.  Note that, as many of our datasets are
        # generated on-the-fly (such as the Mixup and balanced
        # dataset types), the definition of "Epoch" is often
        # unclear, and so we do have to set some number here for
        # the general case
        steps_per_epoch=EPOCH_STEPS,
        epochs=SANITY_EPOCHS,  # We shouldn't reach this number
        callbacks=callbacks,
        verbose=verbosity,
        class_weight=settings.get_class_weights(),
    )


def set_trainability(layers, boolvalue):
    for layer in layers:
        layer.trainable = boolvalue


def trainable(layer):
    ltype = type(layer).__name__
    return "Conv2D" in ltype or "BatchNorm" in ltype


def image_model_fit(model, settings, dataset, callbacks):
    learning_rate = settings.learning_rate
    image_layers = get_image_layers(model)

    if not settings.initialize_randomly():
        # Take smaller steps for fine tuning or pretrained layers
        stepdowns = [8, 64]
        set_trainability(image_layers, False)

        if settings.objective_type == BOUNDING_BOX:
            # Get the names of the last convolutions
            names = get_image_layer_boundary(model, False)
            readout_convolutions = [model.get_layer(n) for n in names]
            set_trainability(readout_convolutions, True)
    else:
        stepdowns = [4, 16]

    train_phase(model, settings, dataset, callbacks, learning_rate)

    if not settings.use_pretrained():
        set_trainability(get_image_layers(model), True)
    else:
        trainable_layers = list(filter(trainable, image_layers))
        set_trainability(trainable_layers[-2:], True)

    callbacks[0].reset_patience()
    if not callbacks[0].is_finished(time.time()):
        new_rate = learning_rate / stepdowns[0]
        callbacks[0].log_message("Phase 2 learning rate: %f" % new_rate)
        train_phase(model, settings, dataset, callbacks, new_rate)

    callbacks[0].reset_patience()
    if not callbacks[0].is_finished(time.time()):
        new_rate = learning_rate / stepdowns[1]
        callbacks[0].log_message("Phase 3 learning rate: %f" % new_rate)
        train_phase(model, settings, dataset, callbacks, new_rate)


def fit(model, settings):
    tf.random.set_seed(settings.seed)

    settings.log_setup("Reading data from cache...")

    holdout_images = None
    splits = create_splits(settings)

    if settings.objective_type == BOUNDING_BOX:
        lengths = (len(splits["training"]), len(splits["validation"]))
        if settings.return_holdout_images and settings.rescaled_names:
            names = settings.rescaled_names
            holdout_images = [names[p[0]] for p in splits["validation"]]
    else:
        lengths = (len(splits["training"][0]), len(splits["validation"][0]))

        if settings.is_image_training_job() and settings.return_holdout_images:
            images = [str(x[0]) for x in splits["validation"][0]]

            if settings.objective_type == CATEGORICAL:
                classes = [int(np.argmax(y)) for y in splits["validation"][1]]
            else:
                classes = [float(y) for y in splits["validation"][1]]

            holdout_images = list(zip(images, classes))

    if lengths[0] == 0:
        raise IndexError("The length of the training dataset is zero.")

    settings.log_setup("%d training, %d holdout" % lengths)
    settings.log_setup("Creating dataset...")
    dataset = make_dataset(settings, splits["training"])

    settings.log_setup("Creating callbacks...")
    callbacks = [PyramidController(settings, splits["validation"])]

    if settings.is_image_training_job():
        settings.log_setup("Fitting image model...")
        image_model_fit(model, settings, dataset, callbacks)
    else:
        settings.log_setup("Fitting model...")
        train_phase(model, settings, dataset, callbacks, settings.learning_rate)

    settings.log_verbose("Fit complete")
    fit_info = callbacks[0].fit_info()
    fit_info.update(settings.get_settings_info())

    evaluation_data = {}

    if settings.is_standard_job():
        importances = compute_importances(model, settings)
        fit_info["importances"] = importances

        if settings.is_search_submodel():
            evaluation_data = evaluations(model, settings)

    elif settings.is_image_training_job():
        fit_info["holdout_images"] = holdout_images
        fit_info["importances"] = [1.0]
        fit_info["preprocess"] = [{"type": IMAGE, "index": 0}]

    fit_info["evaluation_metrics"] = evaluation_data.get("overall", None)
    return fit_info, evaluation_data.get("samples", None)


def metrics(y_true, y_score, is_classification):
    if is_classification:
        return classification_metrics(y_true, y_score)
    else:
        return regression_metrics(y_true, y_score)


def evaluations(model, settings):
    is_classification = settings.objective_type == CATEGORICAL
    X, y_true = settings.read_evaluation_data()
    y_score = model.predict(X)

    class_lists = class_indices(y_true)
    nrows = X.shape[0]
    max_rate = DEFAULT_HOLDOUT_RATE
    limit = MAX_EVALUATION_SAMPLE_SIZE
    rng = random.Random(42)

    overall_metrics = metrics(y_true, y_score, is_classification)
    output_metrics = []

    for i in range(N_EVALUATION_SAMPLES):
        idxs = np.array(get_holdout(class_lists, nrows, max_rate, limit, rng))
        ys_samp = y_score[idxs, :]
        yt_samp = y_true[idxs, :]
        sample_metrics = metrics(yt_samp, ys_samp, is_classification)

        output_metrics.append(sample_metrics)

    return {"samples": output_metrics, "overall": overall_metrics}
