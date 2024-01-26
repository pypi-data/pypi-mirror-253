#!/usr/bin/env python
import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import os
import sys
import json

from sensenet.models.wrappers import create_model

from pyramid.utils import log


def evaluate(data, root_dir, model_dict):
    total = 0
    correct = 0

    log("Creating model...")
    model = create_model(model_dict, None)

    log("Evaluating...")
    for point in data:
        path = os.path.join(root_dir, point["file"])
        label_idx = model._classes.index(point["label"])
        prediction = model(path)

        print(path, label_idx, prediction)
        if np.argmax(prediction) == label_idx:
            correct += 1

        total += 1

        if total % 100 == 0:
            log("Evaluated %d of %d images" % (total, len(data)))

    log(correct / total)


def main():
    log("Pyramid is parsing training file...")

    with open(sys.argv[-1], "r") as fin:
        model = json.load(fin)

    with open(sys.argv[-2], "r") as fin:
        document = json.load(fin)

    data = None

    for key in ["training_data", "image_training_data", "test_data"]:
        if key in document:
            data = document[key]

    if data is not None and "image_root" in document:
        evaluate(data, document["image_root"], model)
    else:
        print("Bad argument")


if __name__ == "__main__":
    main()
