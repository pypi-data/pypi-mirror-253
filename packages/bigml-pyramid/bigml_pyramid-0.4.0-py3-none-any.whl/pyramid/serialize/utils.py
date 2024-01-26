from sensenet.constants import CATEGORICAL, IMAGE

from pyramid.constants import MAX_TREE_EMBEDDING_SIZE
from pyramid.settings.image import construct_image_network


def get_feature_lengths(settings):
    image_features = None
    types = [f["type"] for f in settings.info_list]
    f_lengths = [1] * len(settings.info_list)

    for i, info in enumerate(settings.info_list):
        if types[i] == CATEGORICAL:
            f_lengths[i] = len(info["values"])
        elif types[i] == IMAGE:
            if image_features is None:
                img_net = construct_image_network(settings)
                image_features = img_net["image_network"]["metadata"]["outputs"]

            f_lengths[i] = image_features

    return f_lengths


def get_row_size(settings):
    data_width = settings.data_width()

    if settings.tree_embedding:
        data_width += settings.tree_features()

    return data_width * 4.0
