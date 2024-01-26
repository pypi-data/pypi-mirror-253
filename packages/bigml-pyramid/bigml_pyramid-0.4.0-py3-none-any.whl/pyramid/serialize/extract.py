import pyramid.importers

tf = pyramid.importers.import_tensorflow()

import os
import copy

from sensenet.layers.extract import index_in_model, extract_layers_list
from sensenet.layers.extract import IGNORED_LAYERS
from sensenet.models.image import get_image_layers, pretrained_image_model
from sensenet.pretrained import get_pretrained_network

from pyramid.settings.job_settings import JobSettings

WEIGHT_KEYS = ["beta", "gamma", "mean", "variance", "weights", "offset"]


def unroll_parameterized_layers(layers):
    output_layers = []

    for layer in layers:
        if layer["type"] in ["dense", "batch_normalization"]:
            output_layers.append(layer)
        elif layer["type"] in ["dense_residual_block"]:
            output_layers.extend(
                unroll_parameterized_layers(layer["dense_path"])
            )

    return output_layers


def copy_parameters(source_layers, destination_layers):
    source = unroll_parameterized_layers(source_layers)
    destination = unroll_parameterized_layers(destination_layers)

    assert len(source) == len(destination)

    for src, dst in zip(source, destination):
        assert src["type"] == dst["type"]

        for key in WEIGHT_KEYS:
            if key in src:
                assert key in dst
                dst[key] = src[key]


def json_layers(settings, model):
    try:
        first_dense = index_in_model(model, "Dense", 0)
    except ValueError:
        first_dense = None

    if first_dense:
        readout_layers = model.layers[first_dense:]
        model_layers = extract_layers_list(model, readout_layers)
    else:
        model_layers = []

    if settings.deepnet_version == "alpha":
        new_layers = []

        for layer in settings.layers:
            if layer["type"] not in IGNORED_LAYERS:
                new_layers.append(copy.deepcopy(layer))

        copy_parameters(model_layers, new_layers)

        return new_layers
    else:
        return model_layers


def json_image_layers(model):
    image_layers = get_image_layers(model, truncate_start=True)
    return extract_layers_list(model, image_layers)


def model_to_json(model, settings, fit_info):
    output = dict(fit_info)

    layers = json_layers(settings, model)
    output["layers"] = layers
    output["trees"] = settings.tree_embedding is True

    return output


def json_from_model_id(settings, model_id, image_network=False):
    fit_info = settings.read_fit_info(model_id)
    model_settings = JobSettings(fit_info["training_options"])
    model = model_settings.make_model(True)

    if image_network:
        network = settings.image_network()["image_network"]
        network["layers"] = json_image_layers(model)

        return network
    else:
        return model_to_json(model, model_settings, fit_info)


def json_from_pretrained(network_name):
    settings = {"load_pretrained_weights": True}
    network_specs = get_pretrained_network(network_name)
    model = pretrained_image_model(network_name, settings)

    output = dict(network_specs)
    output["image_network"]["layers"] = json_image_layers(model)
    output["layers"] = json_layers(model)

    return output
