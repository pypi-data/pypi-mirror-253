#!/usr/bin/env python
import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import sys
import os
import json
import time

from PIL import Image, ImageDraw

from sensenet.constants import BOUNDING_BOX, NUMERIC, CATEGORICAL, IMAGE
from sensenet.constants import PAD
from sensenet.preprocess.image import scale_for_box, resize_with_crop_or_pad
from sensenet.models.settings import Settings

from pyramid.data.dataset import make_dataset, create_splits
from pyramid.generator import write_bigml_metadata
from pyramid.settings.base_settings import IMAGE_TRAINING, IMG_FINE_TUNE
from pyramid.settings.image import make_anchors
from pyramid.settings.job_settings import JobSettings
from pyramid.train.finalize import finalize
from pyramid.train.model import fit
from pyramid.utils import log
from pyramid.data.visualize import show_bounding_box_batch, show_training_batch
from pyramid.data.visualize import BATCH_SIZE

DCT = "INTEGER_ACCURATE"
FINAL_MODEL_FILE = "final_model.json"

HEADERS = {
    BOUNDING_BOX: ("Network", "Training Type", "CIOU", "Prob.", "Confidence"),
    CATEGORICAL: ("Network", "Training Type", "Accuracy", "AUC", "Likelihood"),
    NUMERIC: ("Network", "Training Type", "MAE", "MSE", "r-squared"),
}

METRIC_KEYS = {
    BOUNDING_BOX: ("ciou_loss", "probability_loss", "confidence_loss"),
    CATEGORICAL: ("accuracy", "auc", "likelihood"),
    NUMERIC: ("mean_absolute_error", "mean_squared_error", "r_squared"),
}


def model_learning(settings):
    tf.random.set_seed(settings.seed)

    model = settings.make_model(False)
    fit_info, evaluation_data = fit(model, settings)
    settings.write_network(model, fit_info, evaluation_data)

    return fit_info["validation_metrics"]


def make_top_layers(noutputs, softmax):
    return [
        {
            "type": "dense",
            "number_of_nodes": 256,
            "seed": 0,
            "weights": "glorot_uniform",
            "offset": "zeros",
            "activation_function": "relu",
        },
        {
            "type": "dense",
            "number_of_nodes": noutputs,
            "seed": 0,
            "weights": "glorot_uniform",
            "offset": "zeros",
            "activation_function": "softmax" if softmax else "identity",
        },
    ]


def improved(best_metrics, metrics):
    if best_metrics is None:
        return True
    else:
        imp = 0

        for k in metrics:
            if metrics[k] > best_metrics[k]:
                imp += 1
            elif metrics[k] < best_metrics[k]:
                imp -= 1

        return imp > 0


def get_info_list(training_data):
    info_list = [{"index": 0, "type": IMAGE}]

    if "boxes" in training_data[0]:  # Object detection problem
        obj_values = []

        for d in training_data:
            obj_values.extend([box[4] for box in d["boxes"]])

        values = sorted(set(obj_values))
        info_list.append({"type": BOUNDING_BOX, "values": values})
    else:
        obj_values = [d["label"] for d in training_data]

        if type(obj_values[0]) == str:
            values = sorted(set(obj_values))
            info_list.append({"type": CATEGORICAL, "values": values})
        else:
            values = np.array([float(v) for v in obj_values])
            mean, stdev = np.mean(values), np.stdev(values)
            info_list.append({"type": NUMERIC, "mean": mean, "stdev": stdev})

    info_list[-1]["index"] = 1

    return info_list


def get_top_layers(document):
    otype = document["objective_type"]

    if otype == BOUNDING_BOX:
        return []
    elif "layers" in document:
        return document["layers"]
    else:
        noutputs = len(document["info_list"][-1].get("values", [NUMERIC]))
        return make_top_layers(noutputs, otype == CATEGORICAL)


def classes_to_indices(document, training_data):
    values = document["info_list"][-1]["values"]
    for point in training_data:
        point["label"] = values.index(point["label"])

    return training_data


def rescale_boxes(document, training_data, logger=None):
    new_data = []
    name_map = {}

    target_dims = [document["input_image_shape"][i] for i in [1, 0]]
    image_root = document["image_root"]
    settings = Settings({"rescale_type": PAD})

    cache_path = os.path.join(document["output_directory"], ".image_cache")
    os.makedirs(cache_path, exist_ok=True)

    for i, point in enumerate(training_data):
        original_path = os.path.join(image_root, point["file"])
        img_bytes = tf.io.read_file(original_path)
        image = tf.io.decode_jpeg(img_bytes, dct_method=DCT, channels=3)
        input_dims = tf.shape(image)[:2]

        scale = float(scale_for_box(input_dims, target_dims, True).numpy())
        pboxes = point["boxes"]
        boxes = [
            [int(round(c * scale)) for c in b[:4]] + [b[4]] for b in pboxes
        ]

        scaled_image = resize_with_crop_or_pad(settings, target_dims, image)
        out_png = tf.image.encode_png(scaled_image)
        filename = "%08d.png" % i

        tf.io.write_file(os.path.join(cache_path, filename), out_png)
        new_data.append({"file": filename, "boxes": boxes})
        name_map[filename] = [original_path, point["boxes"]]

        if logger and i > 0 and (i + 1) % 100 == 0:
            logger.log_setup("Rescaling complete for %d images" % (i + 1))

    new_doc = dict(document)
    new_doc["image_root"] = cache_path
    new_doc["rescaled_names"] = name_map

    return new_doc, new_data


def create_job(document):
    doc = dict(document)

    if "cache_file" in document:
        log("Cache file detected.  Reading training data.")
        with open(document["cache_file"], "r") as fin:
            training_data = json.load(fin)
    else:
        training_data = doc.pop("training_data")

    doc["job_type"] = IMAGE_TRAINING
    doc["info_list"] = get_info_list(training_data)
    doc["objective_type"] = doc["info_list"][-1]["type"]
    doc["cache_file"] = ""
    doc["cache_rows"] = len(training_data)
    doc["is_search"] = False
    doc["logging_level"] = document.get("logging_level", 1)
    doc["seed"] = document.get("seed", 42)
    doc["layers"] = get_top_layers(doc)

    if doc["objective_type"] == CATEGORICAL:
        training_data = classes_to_indices(doc, training_data)
        new_doc = doc
    elif doc["objective_type"] == BOUNDING_BOX:
        new_doc, training_data = rescale_boxes(doc, training_data)

    return new_doc, training_data


def make_candidate_doc(common_settings, candidate, training_data, index):
    settings_doc = dict(common_settings)
    anchors = settings_doc.pop("bounding_box_anchors", None)

    if candidate[0] == "initial_model":
        settings_doc["base_image_network"] = candidate[0] + "_" + str(index)
        settings_doc["image_training_type"] = IMG_FINE_TUNE
        settings_doc["initial_model"] = candidate[1]
    else:
        settings_doc["base_image_network"] = candidate[0]
        settings_doc["image_training_type"] = candidate[1]

        if settings_doc["objective_type"] == BOUNDING_BOX:
            bbox_anchors = make_anchors(anchors, candidate[0], training_data)
            log("Bounding box anchors: %s" % str(bbox_anchors))
            settings_doc["bounding_box_anchors"] = bbox_anchors

    return settings_doc


def train(document):
    candidates = document.pop("image_network_candidates")
    time_remaining = document.pop("max_total_time")

    common_doc, training_data = create_job(document)

    best_metrics = None
    candidates_remaining = len(candidates)
    end_time = time.time() + time_remaining

    results = {}

    for i, cand in enumerate(candidates):
        settings_doc = make_candidate_doc(common_doc, cand, training_data, i)
        settings_doc["max_training_time"] = (
            time_remaining / candidates_remaining
        )

        settings = JobSettings(settings_doc)
        settings.start_time = time.time()
        settings.image_training_data = training_data

        log(
            "Testing %s for %.2f seconds"
            % (str(cand), settings.max_training_time)
        )

        name_keys = ["base_image_network", "image_training_type"]
        attempt_name = tuple([settings_doc[k] for k in name_keys])

        metrics = model_learning(settings)
        results[attempt_name] = metrics

        if improved(best_metrics, metrics):
            best_metrics = metrics
            best_candidate = attempt_name

        time_remaining = end_time - time.time()
        candidates_remaining -= 1

    settings.base_image_network = best_candidate[0]
    settings.image_training_type = best_candidate[1]

    json_output = finalize(settings)
    settings.write_json(json_output, FINAL_MODEL_FILE)

    head = HEADERS[settings.objective_type]
    metrics = METRIC_KEYS[settings.objective_type]

    print("\n%-16s %-20s %8s %8s %12s" % head)
    print(
        "--------------------------------------------------------------------"
    )

    fmt = "%-16s %-20s %8.4f %8.4f %12.4f"

    for ct in results:
        print(fmt % tuple([ct[0], ct[1]] + [results[ct][k] for k in metrics]))

    print(
        "\nBest result %s written to %s"
        % (
            str(best_candidate),
            os.path.join(settings.output_directory, FINAL_MODEL_FILE),
        )
    )


def visualize_batches(document, nbatches):
    candidates = document.pop("image_network_candidates")
    document.pop("max_total_time")
    settings_doc, training_data = create_job(document)

    settings = JobSettings(settings_doc)
    settings.image_training_data = training_data
    settings.image_training_type = "randomly_initialize"
    settings.batch_size = min(BATCH_SIZE, max(BATCH_SIZE, settings.batch_size))

    show_boxes = settings.objective_type == BOUNDING_BOX

    if show_boxes:
        settings.base_image_network = candidates[0][0]
        metadata = settings.image_network()["image_network"]["metadata"]
        strides = [b["strides"] for b in metadata["outputs"]]
    else:
        settings.base_image_network = "simple"

    splits = create_splits(settings)
    tf_dataset = make_dataset(settings, splits["training"])

    obj_field = settings.info_list[-1]
    labels = obj_field["values"] if "values" in obj_field else None

    for batch in tf_dataset.take(nbatches):
        if show_boxes:
            show_bounding_box_batch(batch, len(labels), strides)
        else:
            show_training_batch(batch, np.array(labels))


def main():
    log("Pyramid is parsing training file...")

    if len(sys.argv) == 3:
        visualize = sys.argv[1].startswith("--visualize")
        bigmlize = sys.argv[1].startswith("--bigmlize")

        if "=" in sys.argv[1]:
            nbatches = int(sys.argv[1].split("=")[-1])
        else:
            nbatches = 1
    else:
        visualize = False
        bigmlize = False
        nbatches = None

    with open(sys.argv[-1], "r") as fin:
        document = json.load(fin)

    if visualize:
        visualize_batches(document, nbatches)
    elif bigmlize:
        write_bigml_metadata(document)
    else:
        train(document)


if __name__ == "__main__":
    main()
