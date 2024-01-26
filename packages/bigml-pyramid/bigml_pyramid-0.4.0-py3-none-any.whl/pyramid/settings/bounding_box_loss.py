import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

from pyramid.constants import CONF_FORMAT, PROB_FORMAT, CIOU_FORMAT, CENT_FORMAT
from pyramid.constants import MAX_BOXES, ANCHORS_PER_SIZE, BACKGROUND_IOU
from pyramid.data.bounding_box import bbox_iou
from pyramid.settings.image import yolo_outputs

BOX_LOSS_TYPES = {
    "ciou_loss": CIOU_FORMAT,
    "confidence_loss": CONF_FORMAT,
    "probability_loss": PROB_FORMAT,
}


def recover_tensors(grid_size, nclasses, all_label_tensors):
    outputs = nclasses + 5
    numpy_batch = all_label_tensors.shape[0]
    tf_batch = tf.shape(all_label_tensors)[0]
    batch_size = numpy_batch or tf_batch

    bboxes_size = MAX_BOXES * 5
    bboxes_shape = (batch_size, MAX_BOXES, 5)
    labels_shape = (batch_size, grid_size, grid_size, ANCHORS_PER_SIZE, outputs)

    labels = tf.reshape(all_label_tensors[:, :-bboxes_size], labels_shape)
    bboxes = tf.reshape(all_label_tensors[:, -bboxes_size:], bboxes_shape)

    return labels, bboxes


def bbox_giou(boxes1, boxes2):
    boxes1_area = boxes1[..., 2] * boxes1[..., 3]
    boxes2_area = boxes2[..., 2] * boxes2[..., 3]

    coor1 = tf.concat(
        [
            boxes1[..., :2] - boxes1[..., 2:] * 0.5,
            boxes1[..., :2] + boxes1[..., 2:] * 0.5,
        ],
        axis=-1,
    )
    coor2 = tf.concat(
        [
            boxes2[..., :2] - boxes2[..., 2:] * 0.5,
            boxes2[..., :2] + boxes2[..., 2:] * 0.5,
        ],
        axis=-1,
    )

    left_up = tf.maximum(coor1[..., :2], coor2[..., :2])
    right_down = tf.minimum(coor1[..., 2:], coor2[..., 2:])

    intersection = tf.maximum(right_down - left_up, 0.0)
    isect_area = intersection[..., 0] * intersection[..., 1]
    union_area = boxes1_area + boxes2_area - isect_area
    iou = tf.math.divide_no_nan(isect_area, union_area)

    enclose_left_up = tf.minimum(coor1[..., :2], coor2[..., :2])
    enclose_right_down = tf.maximum(coor1[..., 2:], coor2[..., 2:])
    enclose = tf.maximum(enclose_right_down - enclose_left_up, 0.0)
    enclose_area = enclose[..., 0] * enclose[..., 1]

    return iou - tf.math.divide_no_nan(enclose_area - union_area, enclose_area)


def bbox_ciou(boxes1, boxes2):
    boxes1_area = boxes1[..., 2] * boxes1[..., 3]
    boxes2_area = boxes2[..., 2] * boxes2[..., 3]

    coor1 = tf.concat(
        [
            boxes1[..., :2] - boxes1[..., 2:] * 0.5,
            boxes1[..., :2] + boxes1[..., 2:] * 0.5,
        ],
        axis=-1,
    )
    coor2 = tf.concat(
        [
            boxes2[..., :2] - boxes2[..., 2:] * 0.5,
            boxes2[..., :2] + boxes2[..., 2:] * 0.5,
        ],
        axis=-1,
    )

    left_up = tf.maximum(coor1[..., :2], coor2[..., :2])
    right_down = tf.minimum(coor1[..., 2:], coor2[..., 2:])

    intersection = tf.maximum(right_down - left_up, 0.0)
    isect_area = intersection[..., 0] * intersection[..., 1]
    union_area = boxes1_area + boxes2_area - isect_area
    iou = tf.math.divide_no_nan(isect_area, union_area)

    enclose_left_up = tf.minimum(coor1[..., :2], coor2[..., :2])
    enclose_right_down = tf.maximum(coor1[..., 2:], coor2[..., 2:])
    enclose = tf.maximum(enclose_right_down - enclose_left_up, 0.0)
    enclose_area = enclose[..., 0] * enclose[..., 1]

    c2 = enclose[..., 0] ** 2 + enclose[..., 1] ** 2
    center_diagonal = boxes2[..., :2] - boxes1[..., :2]
    rho2 = center_diagonal[..., 0] ** 2 + center_diagonal[..., 1] ** 2
    diou = iou - tf.math.divide_no_nan(rho2, c2)

    p_angle = tf.math.atan(
        tf.math.divide_no_nan(boxes1[..., 2], boxes1[..., 3])
    )
    t_angle = tf.math.atan(
        tf.math.divide_no_nan(boxes2[..., 2], boxes2[..., 3])
    )
    v = ((p_angle - t_angle) * 2 / np.pi) ** 2
    alpha = tf.math.divide_no_nan(v, 1 - iou + v)

    return diou - alpha * v


def center_distance(boxes1, boxes2):
    xdiff = boxes1[..., 0] - boxes2[..., 0]
    ydiff = boxes1[..., 1] - boxes2[..., 1]

    return tf.math.sqrt(xdiff * xdiff + ydiff * ydiff)


def cross_entropy(labels, logits):
    return tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=logits)


def confidence_loss(batch_size, input_size, grid_size, nclasses):
    def loss(y_true, y_pred):
        labels, bboxes = recover_tensors(grid_size, nclasses, y_true)
        is_bbox = labels[:, :, :, :, 4:5]

        pred_xywh = y_pred[:, :, :, :, 0:4]
        pred_conf = y_pred[:, :, :, :, 4:5]
        raw_conf = y_pred[:, :, :, :, 5:6]

        iou = bbox_iou(
            pred_xywh[:, :, :, :, np.newaxis, :],
            bboxes[:, np.newaxis, np.newaxis, np.newaxis, :, 0:4],
        )

        max_iou = tf.expand_dims(tf.reduce_max(iou, axis=-1), axis=-1)
        respond_bgd = (1.0 - is_bbox) * tf.cast(
            max_iou < BACKGROUND_IOU, tf.float32
        )

        conf_focal = tf.pow(is_bbox - pred_conf, 2)
        conf_cent = cross_entropy(is_bbox, raw_conf)
        conf_loss = conf_focal * (is_bbox * conf_cent + respond_bgd * conf_cent)

        return tf.reduce_mean(tf.reduce_sum(conf_loss, axis=[1, 2, 3, 4]))

    return loss


def probability_loss(batch_size, input_size, grid_size, nclasses):
    def loss(y_true, y_pred):
        label_prob = y_true[:, :, :, :, 5:]
        is_bbox = y_true[:, :, :, :, 4:5]
        raw_prob = y_pred[:, :, :, :, 5:]

        prob_loss = is_bbox * cross_entropy(label_prob, raw_prob)

        return tf.reduce_mean(tf.reduce_sum(prob_loss, axis=[1, 2, 3, 4]))

    return loss


def ciou_loss(batch_size, input_size, grid_size, nclasses):
    def loss(y_true, y_pred):
        label_xywh = y_true[:, :, :, :, 0:4]
        is_bbox = y_true[:, :, :, :, 4:5]
        pred_xywh = y_pred[:, :, :, :, 0:4]

        ciou = tf.expand_dims(bbox_ciou(pred_xywh, label_xywh), axis=-1)

        bbox_area = label_xywh[:, :, :, :, 2:3] * label_xywh[:, :, :, :, 3:4]
        loss_scale = 2.0 - 1.0 * bbox_area / (input_size ** 2)
        ciou_loss = is_bbox * loss_scale * (1 - ciou)

        return tf.reduce_mean(tf.reduce_sum(ciou_loss, axis=[1, 2, 3, 4]))

    return loss


def center_loss(batch_size, input_size, grid_size, nclasses):
    def loss(y_true, y_pred):
        label_xywh = y_true[:, :, :, :, 0:4]
        is_bbox = y_true[:, :, :, :, 4:5]
        pred_xywh = y_pred[:, :, :, :, 0:4]

        center_dist = center_distance(label_xywh, pred_xywh)

        bbox_area = label_xywh[:, :, :, :, 2:3] * label_xywh[:, :, :, :, 3:4]
        loss_scale = 2.0 - 1.0 * bbox_area / (input_size ** 2)
        center_loss = (
            is_bbox * loss_scale * tf.expand_dims(center_dist, axis=-1)
        )

        return tf.reduce_mean(tf.reduce_sum(center_loss, axis=[1, 2, 3, 4]))

    return loss


def box_losses(settings):
    losses = {}

    batch = settings.batch_size
    in_size = settings.input_image_shape[1]
    ncls = settings.number_of_classes()

    strides = [b["strides"] for b in yolo_outputs(settings.image_network())]
    output_sizes = [in_size // int(s) for s in strides]

    for i, size in enumerate(output_sizes):
        losses[CONF_FORMAT % i] = confidence_loss(batch, in_size, size, ncls)
        losses[PROB_FORMAT % i] = probability_loss(batch, in_size, size, ncls)
        losses[CIOU_FORMAT % i] = ciou_loss(batch, in_size, size, ncls)

    return losses


def compute_bbox_losses(model, dataset, losses):
    aggregate_losses = {k: 0.0 for k in losses}
    output_loss = {k: 0.0 for k in BOX_LOSS_TYPES}

    nimages = 0

    for images, outputs in dataset:
        predictions = model.predict(images)
        nimages += len(images)

        for key in losses:
            # Un-average the loss
            loss = losses[key](outputs[key], predictions[key]) * len(images)
            aggregate_losses[key] += loss

    for loss_type in BOX_LOSS_TYPES:
        loss_fmt = BOX_LOSS_TYPES[loss_type]

        for loss in aggregate_losses:
            for i in range(len(aggregate_losses)):
                if loss_fmt % i == loss:
                    output_loss[loss_type] += aggregate_losses[loss]

        # Re-average to make the loss validation size independent
        output_loss[loss_type] /= nimages

    total_loss = sum(output_loss.values())
    output_loss["total_loss"] = total_loss

    return output_loss
