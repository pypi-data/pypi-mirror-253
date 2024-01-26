import time
import math

from pyramid.serialize.utils import get_feature_lengths

from shapsplain.gradient import GradientExplainer


def original_inputs(settings):
    if settings.instance_weights:
        return len(settings.info_list) - 2
    else:
        return len(settings.info_list) - 1


def make_fields(settings):
    fields_map = {}
    ninputs = original_inputs(settings)
    feature_lengths = get_feature_lengths(settings)[:ninputs]

    fidx = 0

    if settings.tree_embedding:
        tree_maps = settings.load_tree_importances()
        for j, importance in enumerate(tree_maps):
            fields_map[(-1, j)] = {"index": fidx}
            fidx += 1
    else:
        tree_maps = None

    for i, flen in enumerate(feature_lengths):
        for j in range(flen):
            fields_map[(i, j)] = {"index": fidx}
            fidx += 1

    return fields_map, tree_maps


def aggregate(settings, fields, tree_maps, importances):
    output_importances = [0.0] * original_inputs(settings)

    for key, value in importances:
        if math.isfinite(value):
            input_idx, seq_idx = key

            if input_idx == -1:
                portions = tree_maps[seq_idx]

                for idx in portions:
                    output_importances[int(idx)] += portions[idx] * value
            else:
                output_importances[input_idx] += value

    return output_importances


def compute_importances(model, settings):
    if original_inputs(settings) > 1:
        fields, tree_maps = make_fields(settings)

        data = settings.read_importance_data()
        explainer = GradientExplainer(model, data, fields)
        importances = explainer.shap_importances()

        return aggregate(settings, fields, tree_maps, importances)
    else:
        return [1.0]
