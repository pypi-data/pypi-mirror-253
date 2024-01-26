from sensenet.constants import BOUNDING_BOX

from pyramid.data.bounding_box import box_dataset, read_bounding_box_data
from pyramid.data.numpy import read_numpy_arrays
from pyramid.data.image import image_dataset, image_validation_dataset
from pyramid.data.stratify import stratified_split
from pyramid.data.tabular import mixup_dataset, balanced_dataset
from pyramid.data.tabular import standard_dataset

MIN_SPLIT_DATA_SIZE = 32


def make_dataset(settings, arrays):
    if settings.is_image_training_job():
        if settings.objective_type == BOUNDING_BOX:
            return box_dataset(settings, arrays, False)
        else:
            return image_dataset(settings, arrays)
    elif settings.mixup_alpha is not None and settings.mixup_alpha > 0:
        return mixup_dataset(settings, arrays)
    elif settings.balance_objective:
        return balanced_dataset(settings, arrays)
    else:
        return standard_dataset(settings, arrays)


def create_splits(settings):
    if settings.objective_type == BOUNDING_BOX:
        data = read_bounding_box_data(settings)
        nrows = len(data)
    else:
        data = read_numpy_arrays(settings)
        nrows = data[0].shape[0]

    settings.log_progress({"message": "Total training rows: %d" % nrows}, 0.0)

    if nrows > MIN_SPLIT_DATA_SIZE:
        splits = stratified_split(data, settings)
        if settings.cheat_on_validation:
            splits["training"] = data
    else:
        # We don't have enough data to split and do reasonable validation
        # Use the training data as the validation data.
        # We'll definitely overfit, but it's better than no fit at all
        splits = {"training": data, "validation": data}

    return splits


def validation_dataset(settings, validation_data):
    if settings.objective_type == BOUNDING_BOX:
        return box_dataset(settings, validation_data, True)
    else:
        y = validation_data[1]

        if settings.is_image_training_job():
            X = image_validation_dataset(settings, validation_data)
        else:
            X = validation_data[0]

        return X, y
