import pyramid.importers

tf = pyramid.importers.import_tensorflow()

from sensenet.constants import NUMERIC, CATEGORICAL, BOUNDING_BOX

from pyramid.settings.bounding_box_loss import box_losses

losses = tf.keras.losses

LOSSES = {
    "huber": (NUMERIC, losses.Huber),
    "hinge": (CATEGORICAL, losses.CategoricalHinge),
    "crossentropy": (CATEGORICAL, losses.CategoricalCrossentropy),
    "kl_divergence": (CATEGORICAL, losses.KLDivergence),
    "cosine": (CATEGORICAL, losses.CosineSimilarity),
    "mean_squared_error": (NUMERIC, losses.MeanSquaredError),
    "mean_percentage_error": (NUMERIC, losses.MeanAbsolutePercentageError),
}


def classification_loss(settings):
    loss_type, loss_object = LOSSES[settings.loss_function]

    if settings.objective_type == loss_type:
        return loss_object()
    else:
        raise ValueError(
            "%s objective incompatible with %s"
            % (settings.objective_type, loss_type)
        )


def create_objective(settings):
    if settings.objective_type == BOUNDING_BOX:
        return box_losses(settings)
    else:
        return classification_loss(settings)
