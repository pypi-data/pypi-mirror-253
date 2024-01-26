#!/usr/bin/env python
import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import sys
import os
import json
import time

from sensenet.constants import BOUNDING_BOX

from pyramid.utils import log
from pyramid.settings.job_settings import JobSettings
from pyramid.data.generate import image_generator
from pyramid.data.visualize import show_generated_batch

EXCLUDE_FROM_EXPORTED_CONFIG = [
    "background_augmentation_ranges",
    "background_image_augmentations",
    "background_image_root",
    "background_label",
    "bounding_box_margin",
    "constant_box_label",
    "empty_image_rate",
    "foreground_augmentation_ranges",
    "foreground_image_augmentations",
    "foreground_image_root",
    "generated_dataset_size",
    "max_foreground_images",
    "occupancy_range",
    "random_background_rate",
]

COMMAND_LINE_ONLY_KEYS = ["max_total_time", "image_network_candidates"]


def make_settings(document):
    settings_doc = dict(document)

    for key in COMMAND_LINE_ONLY_KEYS:
        settings_doc.pop(key, None)

    settings = JobSettings(settings_doc)

    for key in COMMAND_LINE_ONLY_KEYS:
        settings.training_options[key] = document[key]

    return settings


def generate(settings):
    import PIL as pil

    training_data = []
    image_number = 0

    constant_label = settings.constant_box_label
    n_to_generate = int(settings.generated_dataset_size)
    train_dir = os.path.join(settings.output_directory, "train")

    log("Generating images...")
    tf_dataset = image_generator(settings)

    if os.path.exists(train_dir):
        raise ValueError("%s already exists" % train_dir)
    else:
        os.makedirs(train_dir)

    for image, labels, boxes in tf_dataset.take(n_to_generate):
        if len(labels) > 0:
            outlabel = constant_label or labels[-1].numpy().decode("UTF-8")
        else:
            outlabel = settings.background_label

        outfile = os.path.join(outlabel, "%08d.png" % image_number)
        outimage = pil.Image.fromarray(image.numpy().astype(np.uint8))

        if not os.path.exists(os.path.join(train_dir, outlabel)):
            os.makedirs(os.path.join(train_dir, outlabel))

        outpath = os.path.join(train_dir, outfile)
        outimage.save(outpath)
        image_number += 1

        instance = {"file": outfile, "weight": 1}

        if settings.objective_type == BOUNDING_BOX:
            instance["boxes"] = []

            for label, box_tensor in zip(labels, boxes):
                box = box_tensor.numpy()
                box_label = constant_label or label.numpy().decode("UTF-8")
                instance["boxes"].append(box.tolist() + [box_label])
        else:
            instance["label"] = outlabel

        training_data.append(instance)

        if image_number % 100 == 0:
            log("Wrote %d images" % image_number)

    outdir = settings.output_directory
    outjson = dict(settings.training_options)

    for key in EXCLUDE_FROM_EXPORTED_CONFIG:
        outjson.pop(key, None)

    outjson["training_data"] = training_data
    outjson["image_root"] = train_dir
    outjson["output_directory"] = os.path.join(outdir, "results")

    with open(os.path.join(outdir, "config.json"), "w") as fout:
        json.dump(outjson, fout, sort_keys=True, indent=4)

    return outjson


def visualize_batches(settings, nbatches):
    log("Visualizing batches...")
    tf_dataset = image_generator(settings)

    show_boxes = settings.objective_type == BOUNDING_BOX

    for _ in range(nbatches):
        show_generated_batch(tf_dataset, show_boxes, settings.background_label)


def write_bigml_metadata(document):
    import PIL as pil

    outdata = []

    for point in document["training_data"]:
        newpoint = {"file": point["file"]}
        img_path = os.path.join(document["image_root"], point["file"])

        with pil.Image.open(img_path) as img:
            width, height = img.size

        if "boxes" in point:
            newpoint["boxes"] = []

            for box in point["boxes"]:
                newpoint["boxes"].append(
                    {
                        "xmin": max(0, box[0]),
                        "ymin": max(0, box[1]),
                        "xmax": min(width - 1, box[2]),
                        "ymax": min(height - 1, box[3]),
                        "label": box[4],
                    }
                )

        if "label" in point:
            newpoint["label"] = point["label"]

        outdata.append(newpoint)

    outpath = os.path.join(document["image_root"], "metadata.json")

    with open(outpath, "w") as fout:
        json.dump(outdata, fout, sort_keys=True, indent=4)

    log("Wrote BigML-style metadata to %s" % outpath)


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
        visualize_batches(make_settings(document), nbatches)
    elif bigmlize:
        write_bigml_metadata(document)
    else:
        outjson = generate(make_settings(document))


if __name__ == "__main__":
    main()
