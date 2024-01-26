import pyramid.importers

sktree = pyramid.importers.import_sklearn_tree()

from shapsplain.scikit import shap_importances

from pyramid.serialize.utils import get_feature_lengths


def to_json(tree, node_id):
    if tree.children_left[node_id] == sktree._tree.TREE_LEAF:
        values = tree.value[node_id][0]

        if len(values) > 1:
            sum_values = float(sum(values))
            return [[v / sum_values for v in values], None]
        else:
            return [values.tolist(), None]
    else:
        feature = int(tree.feature[node_id])
        threshold = float(tree.threshold[node_id])
        left_child = to_json(tree, tree.children_left[node_id])
        right_child = to_json(tree, tree.children_right[node_id])

        return [feature, threshold, left_child, right_child]


def fields_for_range(start, end, index_map):
    fields = {}

    for i, r in enumerate(range(start, end)):
        true_idx = index_map[r]
        fields[str(i)] = {"optype": "numeric", "name": r, "true_idx": true_idx}

    return fields


def trees_to_json(embedding, settings):
    feature_lengths = get_feature_lengths(settings)

    fidx = 0
    index_map = {}

    for i, flen in enumerate(feature_lengths):
        for _ in range(flen):
            index_map[fidx] = i
            fidx += 1

    if embedding["trees"] is not None:
        out_trees = []
        out_importances = []

        for feature_range, ensemble in embedding["trees"]:
            start, end = feature_range
            fields = fields_for_range(start, end, index_map)
            all_shap_values = shap_importances(ensemble, fields, False)

            for values_for_output in all_shap_values:
                imp = {fields[v]["true_idx"]: 0.0 for v in fields.keys()}

                for sv in values_for_output:
                    true_idx = fields[sv[0]]["true_idx"]
                    imp[true_idx] += sv[1]

                out_importances.append(imp)

            jensemble = []
            for model in ensemble.estimators_:
                jensemble.append(to_json(model.tree_, 0))

            out_trees.append([feature_range, jensemble])

        assert len(out_importances) == embedding["tree_features"]
    else:
        out_trees = None
        out_importances = None

    return {
        "trees": out_trees,
        "importances": out_importances,
        "tree_features": embedding["tree_features"],
    }
