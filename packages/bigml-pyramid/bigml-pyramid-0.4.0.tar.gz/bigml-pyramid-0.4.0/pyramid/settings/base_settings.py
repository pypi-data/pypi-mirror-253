import pyramid.importers

tf = pyramid.importers.import_tensorflow()

import os
import sys
import json

from sensenet.constants import NUMERIC, CATEGORICAL, IMAGE
from sensenet.constants import TRIPLET, BOUNDING_BOX
from sensenet.constants import WARP, PAD, CROP

from sensenet.accessors import get_image_shape
from sensenet.layers.construct import feed_through
from sensenet.models.image import image_model
from sensenet.models.settings import Settings
from sensenet.preprocess.image import make_image_reader

from pyramid.constants import LOG_PRODUCTION, LOG_VERBOSE, LOG_TENSORFLOW
from pyramid.constants import MAX_TREE_EMBEDDING_SIZE, MAX_TREE_MODELS
from pyramid.utils import log, progress_string

from pyramid.settings.image import construct_image_network
from pyramid.settings.objectives import LOSSES
from pyramid.settings.optimizers import OPTIMIZERS

IMG_SCRATCH = "randomly_initialize"
IMG_FINE_TUNE = "fine_tune"
IMG_PRETRAINED = "use_pretrained"

FINALIZING = "finalize_output"
SEARCH_SUBMODEL = "search_submodel"
IMAGE_TRAINING = "image_training"
DATA_CACHING = "dataset_caching"
STANDARD = "standard_training"

JOB_TYPES = [
    FINALIZING,
    SEARCH_SUBMODEL,
    IMAGE_TRAINING,
    DATA_CACHING,
    STANDARD,
]
IMAGE_TRAINING_TYPES = [IMG_SCRATCH, IMG_FINE_TUNE, IMG_PRETRAINED]

OPTIONAL = {
    "augmentation_ranges": dict,
    "augmentation_seed": int,
    "background_augmentation_ranges": dict,
    "background_image_augmentations": [list, str],
    "balance_objective": bool,
    "beta1": [0.0, 1.0],
    "beta2": [0.0, 1.0],
    "bounding_box_anchors": [list, list],
    "bounding_box_margin": [0.0, float("inf")],
    "deepnet_version": [None, "alpha", "beta"],
    "cheat_on_validation": bool,
    "class_weights": [list, list],
    "color_space": ["rgb", "RGB"],
    "constant_box_label": str,
    "empty_image_rate": [0.0, 1.0],
    "epsilon": [0.0, 1.0],
    "foreground_augmentation_ranges": dict,
    "foreground_image_augmentations": [list, str],
    "holdout_rate": [0.0, 1.0],
    "holdout_set_size": [1.0, 8192.0],
    "image_augmentations": [list, str],
    "image_training_data": list,
    "init_accumulator": [0.0, float("inf")],
    "initial_model": str,
    "initial_network_metadata": dict,
    "instance_weights": bool,
    "job_type": JOB_TYPES,
    "l1_regularization": [0.0, float("inf")],
    "l2_regularization": [0.0, float("inf")],
    "label_smoothing_factor": [0.0, 0.5],
    "learning_rate_power": [-1.0, 0.0],
    "learning_rate_warmup_iterations": [0.0, float("inf")],
    "logging_level": [None, LOG_VERBOSE, LOG_PRODUCTION, LOG_TENSORFLOW],
    "max_iterations": [0.0, float("inf")],
    "max_training_time": [0.0, float("inf")],
    "max_seconds_per_update": [0.0, float("inf")],
    "mixup_alpha": [0.0, 1.0],
    "model_fraction": [0.0, 1.0],
    "momentum": [0.0, 1.0],
    "patience": [1.0, 8192.0],
    "random_background_rate": [0.0, 1.0],
    "rescale_type": [WARP, PAD, CROP],
    "rescaled_names": dict,
    "return_holdout_images": bool,
    "rho": [0.0, 1.0],
    "strict_boxes": bool,
    "tree_embedding": bool,
    "tree_inputs": [0.0, MAX_TREE_EMBEDDING_SIZE],
}

REQUIRED = {
    "activation_function": str,
    "background_image_root": str,
    "background_label": str,
    "base_image_network": str,
    "batch_size": [1.0, 8192.0],
    "cache_file": str,
    "cache_rows": int,
    "descent_algorithm": list(OPTIMIZERS.keys()),
    "dropout_rate": [0.0, 0.75],
    "foreground_image_root": str,
    "generated_dataset_size": [1.0, float("inf")],
    "image_root": str,
    "image_training_type": IMAGE_TRAINING_TYPES,
    "info_list": [list, dict],
    "input_image_shape": [list, int],
    "is_search": bool,
    "job_id": str,
    "largest_layer_size": [2.0, 1024],
    "layers": [list, dict],
    "learn_residuals": bool,
    "learning_rate": [0.0, float("inf")],
    "loss_function": list(LOSSES.keys()),
    "max_data_size": int,
    "max_foreground_images": [1.0, 32.0],
    "number_of_layers": [0.0, 128.0],
    "objective_type": [CATEGORICAL, NUMERIC, TRIPLET, BOUNDING_BOX],
    "occupancy_range": [list, float],
    "output_directory": str,
    "parallelism": int,
    "seed": [0, 2147483647],
    "start_time": [0.0, float("inf")],
    "topology": str,
    "training_options": dict,
}


class BaseSettings(Settings):
    _required_attributes = REQUIRED
    _attribute_validators = {}
    _attribute_validators.update(OPTIONAL)
    _attribute_validators.update(REQUIRED)

    def __init__(self, amap):
        super().__init__(amap)
        self.__setattr__("training_options", amap)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def get_image_model_id(self):
        return "%s_%s" % (self.base_image_network, self.image_training_type)

    def get_job_id(self):
        if self.is_image_training_job():
            return self.get_image_model_id()
        else:
            return self.job_id

    def log(self, msg, level):
        if level == self.logging_level:
            log(msg)

    def log_verbose(self, msg):
        self.log(msg, LOG_VERBOSE)

    def log_progress(self, adict, progress):
        output = dict(adict)

        output["job_id"] = self.get_job_id()
        output["progress"] = progress

        self.log(progress_string(output), LOG_PRODUCTION)

        # These are setup messages that make me feel good to see
        if progress == 0.0 and "message" in adict:
            self.log(adict["message"], LOG_VERBOSE)

    def log_setup(self, msg):
        self.log_progress({"message": msg}, 0.0)

    def get_settings_info(self):
        class_index = len(self.info_list) - 1
        weight_index = None
        non_inputs = 1

        if self.instance_weights:
            weight_index = len(self.info_list) - 2
            non_inputs += 1

        outex = dict(self.info_list[-1])
        outex.pop("index")

        return {
            "training_options": self.training_options,
            "optypes": [info["type"] for info in self.info_list],
            "preprocess": self.info_list[:-non_inputs],
            "class_index": class_index,
            "weight_index": weight_index,
            "output_exposition": outex,
        }

    def get_classes(self):
        if self.objective_type in [BOUNDING_BOX, CATEGORICAL]:
            return self.info_list[-1]["values"]
        else:
            return None

    def get_class_weights(self):
        if self.class_weights is None or self.objective_type != CATEGORICAL:
            return None
        else:
            classes = self.get_classes()
            weights = {i: 1.0 for i in range(len(classes))}

            for cls, wt in self.class_weights:
                weights[classes.index(cls)] = wt

            weight_sum = sum(weights.values())
            return {k: weights[k] / weight_sum for k in weights}

    def is_search_submodel(self):
        return self.job_type == SEARCH_SUBMODEL

    def is_image_training_job(self):
        return self.job_type == IMAGE_TRAINING

    def is_caching_job(self):
        return self.job_type == DATA_CACHING

    def is_finalizing_job(self):
        return self.job_type == FINALIZING

    def is_standard_job(self):
        return self.job_type in [None, STANDARD, SEARCH_SUBMODEL]

    def is_training_job(self):
        return self.job_type in [None, STANDARD, IMAGE_TRAINING]

    def data_width(self, input_info_list=None):
        width = 0
        image_network = None

        for type_info in input_info_list or self.info_list:
            if type_info["type"] == NUMERIC:
                width += 1
            elif type_info["type"] == CATEGORICAL:
                width += len(type_info["values"])
            elif type_info["type"] == IMAGE:
                if image_network is None:
                    image_network = self.image_network()

                width += image_network["image_network"]["metadata"]["outputs"]
            else:
                raise ValueError("What is a %s?" % type_info["type"])

        return width

    def single_image_input_only(self):
        if self.has_image_inputs():
            if self.instance_weights and len(self.info_list) == 3:
                return True
            elif len(self.info_list) == 2:
                return True
            else:
                return False
        else:
            return False

    def has_image_inputs(self):
        return any([info["type"] == IMAGE for info in self.info_list])

    def tree_features(self):
        if self.tree_inputs is not None:
            return self.tree_inputs
        else:
            n_features = self.number_of_inputs(original_only=True)
            n_classes = self.number_of_classes()
            max_outputs = min(MAX_TREE_EMBEDDING_SIZE, n_features)
            n_models = min(MAX_TREE_MODELS, max(1, max_outputs // n_classes))

            return n_models * n_classes

    def number_of_inputs(self, original_only=False):
        if self.instance_weights:
            inputs = self.info_list[:-2]
        else:
            inputs = self.info_list[:-1]

        original_inputs = self.data_width(input_info_list=inputs)

        if self.tree_embedding and not original_only:
            return self.tree_features() + original_inputs
        else:
            return original_inputs

    def number_of_classes(self):
        if self.objective_type in [CATEGORICAL, BOUNDING_BOX]:
            return len(self.get_classes())
        else:
            return 1

    def make_layer_sequence(self, in_tensor=None, layers=None):
        if in_tensor is None:
            inputs = tf.keras.Input(self.number_of_inputs(), dtype=tf.float32)
        else:
            inputs = in_tensor

        to_propagate = layers or self.layers
        outputs = feed_through(to_propagate, inputs)

        return inputs, outputs

    def use_pretrained(self):
        return self.image_training_type == IMG_PRETRAINED

    def fine_tune(self):
        return self.image_training_type == IMG_FINE_TUNE

    def initialize_randomly(self):
        return self.image_training_type == IMG_SCRATCH

    def image_network(self):
        return construct_image_network(self)

    def create_base_image_model(self, load_weights):
        image_model_settings = {
            "load_pretrained_weights": load_weights,
            "regression_normalize": True,
        }

        return image_model(self.image_network(), image_model_settings)

    def image_file_reader(self, root=None):
        target_shape = get_image_shape(self)
        file_prefix = root if root is not None else self.image_root
        settings = Settings({"rescale_type": self.rescale_type or CROP})

        return make_image_reader("file", target_shape, file_prefix, settings)

    def get_augmentations(self):
        if self.augmentation_ranges:
            return self.augmentation_ranges
        elif self.image_augmentations:
            return {k: None for k in self.image_augmentations}
        else:
            return {}

    def get_foreground_augmentations(self):
        if self.foreground_augmentation_ranges:
            return self.foreground_augmentation_ranges
        elif self.foreground_image_augmentations:
            return {k: None for k in self.foreground_image_augmentations}
        else:
            return {}

    def get_background_augmentations(self):
        if self.background_augmentation_ranges:
            return self.background_augmentation_ranges
        elif self.background_image_augmentations:
            return {k: None for k in self.background_image_augmentations}
        else:
            return {}
