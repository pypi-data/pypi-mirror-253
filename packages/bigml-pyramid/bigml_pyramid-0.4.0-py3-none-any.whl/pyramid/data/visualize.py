import pyramid.importers

np = pyramid.importers.import_numpy()

from pyramid.constants import CONF_FORMAT
from pyramid.data.generate import draw_rectangle
from pyramid.settings.bounding_box_loss import recover_tensors

BOX_COLORS = ["red", "blue", "green", "yellow", "black", "purple", "orange"]

BATCH_ROWS = 3
BATCH_COLUMNS = 4
BATCH_SIZE = BATCH_ROWS * BATCH_COLUMNS


def draw_boxes(image, boxes):
    import PIL as pil

    draw = pil.ImageDraw.Draw(image)

    for box in boxes:
        color = BOX_COLORS[box[-1] % len(BOX_COLORS)]
        draw_rectangle(draw, box[0:4], None, color, w=3)


def draw_image_grid(images, labels, all_boxes):
    import matplotlib.pyplot as plt
    import PIL as pil

    plt.figure(figsize=(10, 8), tight_layout=True)

    for i, img_array in enumerate(images):
        ax = plt.subplot(3, 4, i + 1)
        image = pil.Image.fromarray(img_array)

        if all_boxes is not None:
            draw_boxes(image, all_boxes[i])

        if labels is not None:
            plt.title(labels[i][-1])

        plt.imshow(image)
        plt.axis("off")

    plt.show()


def show_bounding_box_batch(batch, nclasses, strides):
    images_batch = batch[0].numpy()[0:BATCH_SIZE, ...].astype(np.uint8)
    boxes_batch = [list() for _ in range(BATCH_SIZE)]

    for i in range(len(strides)):
        grid = images_batch.shape[1] // strides[i]
        labels_boxes = batch[1][CONF_FORMAT % i]
        labels, boxes = recover_tensors(grid, nclasses, labels_boxes)

        for n in range(BATCH_SIZE):
            for label, box in zip(labels[n].numpy(), boxes[n].numpy()):

                if np.sum(box) > 0:
                    boxes_batch[n].append(
                        [
                            int(round(box[0] - 0.5 * box[2])),
                            int(round(box[1] - 0.5 * box[3])),
                            int(round(box[0] + 0.5 * box[2])),
                            int(round(box[1] + 0.5 * box[3])),
                            int(round(box[-1])),
                        ]
                    )

    draw_image_grid(images_batch, None, boxes_batch)


def show_generated_batch(dataset, show_boxes, empty_label):
    images = []
    labels = []

    if show_boxes:
        all_boxes = []
    else:
        all_boxes = None

    for image, box_labels, img_boxes in dataset.take(BATCH_SIZE):
        if len(box_labels) > 0:
            label = [b.numpy().decode("utf-8") for b in box_labels]
        else:
            label = [empty_label]

        labels.append(label)
        images.append(image.numpy().astype(np.uint8))

        if all_boxes is not None:
            boxes = [box.numpy().tolist() + [0] for box in img_boxes]
            all_boxes.append(boxes)

    draw_image_grid(images, labels, all_boxes)


def show_training_batch(batch, label_strings):
    images, ys, weights = batch
    idxs = np.argmax(ys, axis=-1)
    labels = [[label] for label in label_strings[idxs].tolist()]
    image_list = [image.astype(np.uint8) for image in images.numpy()]

    draw_image_grid(image_list[:BATCH_SIZE], labels[:BATCH_SIZE], None)
