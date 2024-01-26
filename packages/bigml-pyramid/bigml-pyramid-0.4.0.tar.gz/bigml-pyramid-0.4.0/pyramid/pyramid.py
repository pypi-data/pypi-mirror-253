#!/usr/bin/env python
import pyramid.importers

tf = pyramid.importers.import_tensorflow()

import os
import sys
import time
import json
import traceback
import gc
import glob

from sensenet.constants import BOUNDING_BOX, CATEGORICAL, NUMERIC
from sensenet.constants import MEAN, STANDARD_DEVIATION
from sensenet.layers.construct import remove_weights
from sensenet.layers.legacy import legacy_convert
from sensenet.models.wrappers import create_model

from pyramid import __version__
from pyramid.constants import DEFAULT_EXPORT_SETTINGS, HOLDOUT_PREDICT_SETTINGS
from pyramid.trainer import rescale_boxes
from pyramid.utils import get_input, log, print_final
from pyramid.cache.read import data_to_numpy
from pyramid.cache.write import create_cache
from pyramid.data.numpy import array_hash
from pyramid.settings.image import make_anchors
from pyramid.settings.job_settings import JobSettings
from pyramid.train.finalize import finalize, select_config_options
from pyramid.train.model import fit

MODEL_OUTPUT_KEYS = [
    "validation_metrics",
    "evaluation_metrics",
    "iterations",
    "elapsed_time",
]

CONFIGURATION_PARAMETERS = [
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

FINAL_MODEL_FILE = "final_model.json"
SHORT_MODEL_FILE = "short_model.json"

WEIGHT_FILE = "final_model_weights.h5"
BUNDLE_FILE = "final_model_bundle.smbundle"
JS_PATH = "final_model_js_export"


def model_learning(settings):
    tf.random.set_seed(settings.seed)

    settings.log_setup("Creating TF model...")
    model = settings.make_model(False)

    fit_info, evaluation_data = fit(model, settings)
    settings.write_network(model, fit_info, evaluation_data)

    if settings.is_search_submodel():
        config = select_config_options(fit_info)
    else:
        config = None

    if settings.is_image_training_job():
        base_net = settings.base_image_network
        image_type = settings.image_training_type
    else:
        base_net = image_type = None

    output = {k: fit_info[k] for k in MODEL_OUTPUT_KEYS}
    output["job_id"] = settings.get_job_id()

    output["configuration_parameters"] = config
    output["base_image_network"] = base_net
    output["image_training_type"] = image_type

    # Comment in to enable verification that we're getting exactly the same
    # dataset samples from run to run
    #
    # output['evaluation_hash'] = array_hash(settings.read_evaluation_data()[0])
    # output['importance_hash'] = array_hash(settings.read_importance_data())

    return output


def holdout_image_predictions(settings):
    fit_info = settings.read_fit_info(settings.get_image_model_id())
    holdout_images = fit_info["holdout_images"]
    outex = fit_info["output_exposition"]

    json_image_model = finalize(settings, image_model=True)
    model = create_model(json_image_model, HOLDOUT_PREDICT_SETTINGS)

    root = (
        "" if settings.objective_type == BOUNDING_BOX else settings.image_root
    )
    predictions = []

    for afile, truth in holdout_images:
        full_path = os.path.join(root, afile) if root else afile
        output = model([[full_path]])

        if settings.objective_type == CATEGORICAL:
            tval = truth
            prediction = [float(v) for v in output[0].tolist()]
        elif settings.objective_type == NUMERIC:
            # Training assumes the ground truth values are
            # standardized, so they need to be "destandardized" so
            # that they are comparable with the predictions
            tval = truth * outex[STANDARD_DEVIATION] + outex[MEAN]
            prediction = float(output[0][0])
        elif settings.objective_type == BOUNDING_BOX:
            tval = truth
            prediction = output
        else:
            raise ValueError("objective_type is %s" % settings.objective_type)

        predictions.append([full_path, tval, prediction])

    return predictions


def model_finalizing(settings):
    start = time.time()

    settings.log_progress({"message": "Finalizing"}, 0.0)
    json_model = finalize(settings)

    if settings.has_image_inputs():
        settings.log_progress({"message": "Creating holdout predictions"}, 0.1)
        preds = holdout_image_predictions(settings)
        json_model["holdout_image_predictions"] = preds

    settings.log_progress({"message": "Recreating model"}, 0.3)
    wrapped = create_model(json_model, DEFAULT_EXPORT_SETTINGS)
    settings.log_progress({"message": "Writing weight file"}, 0.4)
    weight_path = settings.write_h5(wrapped, WEIGHT_FILE)
    settings.log_progress({"message": "Writing bundle file"}, 0.5)
    bundle_path, js_path = settings.write_bundle(wrapped, BUNDLE_FILE, JS_PATH)

    if settings.deepnet_version == "alpha":
        json_model = legacy_convert(json_model)

    short_model = remove_weights(json_model)

    settings.log_progress({"message": "Writing JSON"}, 0.8)
    final_path = settings.write_json(json_model, FINAL_MODEL_FILE)
    short_path = settings.write_json(short_model, SHORT_MODEL_FILE)

    settings.log_progress({"message": "Globbing paths and finishing"}, 0.9)
    js_bins = glob.glob(os.path.join(js_path, "*.bin"))
    js_json = glob.glob(os.path.join(js_path, "*.json"))

    return {
        "final_model_path": final_path,
        "short_model_path": short_path,
        "weight_path": weight_path,
        "bundle_path": bundle_path,
        "tfjs_weight_paths": js_bins,
        "tfjs_model_path": js_json[0],
        "final_model_size": os.path.getsize(final_path),
        "short_model_size": os.path.getsize(short_path),
        "weights_size": os.path.getsize(weight_path),
        "bundle_size": os.path.getsize(bundle_path),
    }


def dataset_caching(settings):
    data = data_to_numpy(settings)
    return create_cache(data, settings)


def process(settings):
    start_time = time.time()

    settings.start_time = start_time
    settings.log_setup("pyramid job beginning")

    if settings.is_caching_job():
        output = dataset_caching(settings)
    elif settings.is_finalizing_job():
        output = model_finalizing(settings)
    elif settings.is_image_training_job() or settings.is_standard_job():
        output = model_learning(settings)
    else:
        raise ValueError("Cannot do job type of %s" % settings.training_type)

    output["job_time"] = time.time() - start_time
    return output


def create_bbox_job(jdoc, logger):
    with open(jdoc["cache_file"]) as fin:
        raw_data = json.load(fin)

    new_document, training_data = rescale_boxes(jdoc, raw_data, logger=logger)
    bbox_anchors = make_anchors(None, jdoc["base_image_network"], training_data)

    logger.log_setup("Bounding box anchors: %s" % str(bbox_anchors))

    new_document["cache_file"] = ""
    new_document["image_training_data"] = training_data
    new_document["bounding_box_anchors"] = bbox_anchors

    return new_document


def main():
    if sys.argv[-1] == "--version":
        log("Pyramid %s" % __version__)
        sys.exit(0)

    log("pyramid process ready - version %s" % __version__)

    timeout = int(sys.argv[-1])
    to_process = get_input(timeout)

    while to_process and to_process != "terminate":
        with open(to_process, "r") as fin:
            document = json.load(fin)

        try:
            if document["objective_type"] == BOUNDING_BOX:
                logger = JobSettings(document)
                document = create_bbox_job(document, logger)

            settings = JobSettings(document)
            output = process(settings)
            print_final(output)
        except:
            print_final(
                {"job_id": document["job_id"], "error": traceback.format_exc()}
            )

        gc.collect()
        to_process = get_input(timeout)


if __name__ == "__main__":
    main()
