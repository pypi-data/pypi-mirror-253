import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()
sk_cluster = pyramid.importers.import_sklearn_cluster()

import math
import copy

from sensenet.constants import BOUNDING_BOX, CROP

from sensenet.accessors import get_image_shape, yolo_outputs
from sensenet.layers.convolutional import conv_2d
from sensenet.layers.yolo import yolo_decode
from sensenet.models.image import get_image_layers
from sensenet.pretrained import get_pretrained_network, PRETRAINED_CNN_METADATA

from pyramid.constants import CONF_FORMAT, PROB_FORMAT, CIOU_FORMAT
from pyramid.constants import ANCHORS_PER_SIZE

BN_LAYER = {
    "beta": "zeros",
    "gamma": "ones",
    "mean": "zeros",
    "type": "batch_normalization",
    "variance": "ones",
}

DUMMY_NETWORK = {
    "layers": [
        {
            "activation_function": "softmax",
            "number_of_nodes": 2,
            "offset": "zeros",
            "seed": 0,
            "type": "dense",
            "weights": "glorot_uniform",
        }
    ],
    "preprocess": [{"index": 0, "type": "image"}],
    "output_exposition": {"type": "categorical", "values": ["a", "b"]},
    "trees": None,
}


def max_pool(pool_size, strides):
    return {
        "padding": "same",
        "pool_size": list(pool_size),
        "strides": list(strides),
        "type": "max_pool_2d",
    }


def conv_bn_act(kernel_dimensions, nfilters, activation, drop_size):
    conv = {
        "bias": "zeros",
        "kernel": "glorot_uniform",
        "kernel_dimensions": kernel_dimensions,
        "number_of_filters": nfilters,
        "padding": "same",
        "seed": 1,
        "strides": [1, 1],
        "type": "convolution_2d",
    }

    act = {"activation_function": activation, "type": "activation"}

    if drop_size:
        drop = {
            "type": "dropout",
            "dropout_type": "block",
            "rate": 0.1,
            "block_size": drop_size,
        }

        return [conv, drop, BN_LAYER, act]
    else:
        return [conv, BN_LAYER, act]


def compose_simple(settings):
    input_shape = settings.input_image_shape
    layers = []

    layers.extend(conv_bn_act([3, 3], 32, "relu", None))
    layers.append(max_pool([3, 3], [2, 2]))
    layers.extend(conv_bn_act([3, 3], 64, "relu", None))
    layers.append(max_pool([3, 3], [2, 2]))
    layers.extend(conv_bn_act([3, 3], 128, "relu", None))
    layers.append({"type": "global_max_pool_2d"})

    return layers


def res_block(nfilters, activation, drop_size, last):
    layers = []

    layers.extend(conv_bn_act([1, 1], nfilters, activation, drop_size))

    residual_layers = []
    residual_layers.extend(conv_bn_act([3, 3], nfilters, activation, drop_size))
    residual_layers.extend(conv_bn_act([3, 3], nfilters, "linear", drop_size))

    block = {
        "type": "resnet_block",
        "convolution_path": residual_layers,
        "identity_path": [],
        "activation_function": activation,
    }

    layers.append(block)

    if not last:
        layers.append(max_pool([3, 3], [2, 2]))

    return layers


def compose_simple_residual(settings):
    input_shape = settings.input_image_shape
    is_training = settings.is_image_training_job()

    min_dim = min(input_shape[0], input_shape[1])
    nlayers = min(6, max(3, int(round(math.log2(min_dim))) - 2))
    drop_size = is_training and max(1, int(round(0.03 * min_dim)))

    layers = []

    for n in range(nlayers):
        nfilters = 2 ** (5 + n)  # Kind of standard increases as we go up
        layers.extend(res_block(nfilters, "mish", drop_size, n == nlayers - 1))

    layers.append({"type": "global_average_pool_2d"})

    return layers


COMPOSERS = {
    "simple": compose_simple,
    "simple_residual": compose_simple_residual,
}


def get_outputs(layers):
    if layers[-2]["type"] == "resnet_block":
        cpath = layers[-2]["convolution_path"]
        if cpath[-3]["type"] == "dropout":
            return cpath[-4]["number_of_filters"]
        else:
            return cpath[-3]["number_of_filters"]
    else:
        return layers[-4]["number_of_filters"]


def generate_metadata(settings):
    return {
        "base_image_network": settings.base_image_network,
        "input_image_shape": settings.input_image_shape,
        "loading_method": "centering",
        "mean_image": None,
        "outputs": None,
        "version": None,
        "rescale_type": settings.rescale_type or CROP,
    }


def simple_network(settings):
    composer = COMPOSERS[settings.base_image_network]

    layers = composer(settings)
    metadata = generate_metadata(settings)
    image_network = {"layers": layers, "metadata": metadata}

    network = dict(DUMMY_NETWORK)
    network["image_network"] = image_network
    network["image_network"]["metadata"]["outputs"] = get_outputs(layers)

    return network


def pretrained_weights_available(network_name):
    return network_name in PRETRAINED_CNN_METADATA


def construct_image_network(settings):
    if settings.initial_network_metadata:
        base_network = settings.initial_network_metadata["base_image_network"]
        rescale_type = settings.initial_network_metadata["rescale_type"]
        input_shape = settings.initial_network_metadata["input_image_shape"]

        if settings.objective_type == BOUNDING_BOX:
            anchors = []
            for branch in settings.initial_network_metadata["outputs"]:
                anchors.extend(branch["anchors"])
    else:
        base_network = settings.base_image_network
        rescale_type = settings.rescale_type
        input_shape = settings.input_image_shape
        anchors = settings.bounding_box_anchors

    if pretrained_weights_available(base_network):
        network = get_pretrained_network(base_network)
    else:
        network = simple_network(settings)

    network = copy.deepcopy(network)

    network["image_network"]["metadata"]["input_image_shape"] = input_shape

    if rescale_type:
        network["image_network"]["metadata"]["rescale_type"] = rescale_type

    if settings.objective_type == BOUNDING_BOX:
        network["layers"] = []

        if anchors:
            for i, branch in enumerate(yolo_outputs(network)):
                begin = i * ANCHORS_PER_SIZE
                end = begin + ANCHORS_PER_SIZE
                branch["anchors"] = anchors[begin:end]

    return network


def yolo_training_outputs(yolo_predictions):
    outputs = {}

    for i, prediction in enumerate(yolo_predictions):
        raw, boxes = prediction
        boxes_xywhc = boxes[:, :, :, :, 0:5]
        raw_conf = raw[:, :, :, :, 4:5]
        conf_out = tf.concat([boxes_xywhc, raw_conf], -1)

        outputs[CONF_FORMAT % i] = conf_out
        outputs[PROB_FORMAT % i] = raw
        outputs[CIOU_FORMAT % i] = boxes

    return outputs


def make_anchors(anchors, base_network, training_data):
    network = get_pretrained_network(base_network)

    n_anchors = len(yolo_outputs(network)) * ANCHORS_PER_SIZE
    box_sizes = set()

    if anchors:
        for anchor in anchors:
            if len(anchor) != 2:
                raise ValueError('"%s" is an invalid anchor' % str(anchor))
            else:
                box_sizes.add(tuple([float(d) for d in anchor]))
    else:
        for point in training_data:
            for box in point["boxes"]:
                x1, y1, x2, y2 = box[:4]
                box_sizes.add((x2 - x1, y2 - y1))

    if len(box_sizes) > n_anchors:
        km = sk_cluster.KMeans(n_anchors)
        km.fit(np.array(sorted(box_sizes)))
        centers = km.cluster_centers_
    else:
        centers = np.array([list(s) for s in sorted(box_sizes)])

    if centers.shape[0] < n_anchors:
        centers = np.tile(centers, (n_anchors, 1))[:n_anchors, :]

    anchors = [[int(round(d)) for d in size] for size in centers.tolist()]

    return sorted(anchors, key=lambda x: x[0] * x[1])


def trainable_yolo(settings, yolo_model, reconfigure_readout):
    preds = []

    nclasses = settings.number_of_classes()
    image_input = yolo_model.input
    image_layers = get_image_layers(yolo_model)

    network = construct_image_network(settings)
    in_size = get_image_shape(network)[1]

    for branch in yolo_outputs(network):
        old_layer = image_layers[branch["input"]]

        if reconfigure_readout:
            config = network["image_network"]["layers"][branch["input"]]
            config["number_of_filters"] = ANCHORS_PER_SIZE * (nclasses + 5)

            new_layer = conv_2d(config)
            features = new_layer(old_layer.input)
        else:
            features = old_layer.output

        decode_info = [branch[k] for k in ["strides", "anchors", "xyscale"]]
        preds.append(yolo_decode(features, decode_info, in_size, nclasses))

    all_outputs = yolo_training_outputs(preds)

    return tf.keras.Model(inputs=image_input, outputs=all_outputs)
