import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import random
import glob
import os

from PIL import Image, ImageDraw

from sensenet.constants import BOUNDING_BOX

from pyramid.constants import MAX_INT_32
from pyramid.data.image import make_image_data_generator
from pyramid.data.image import apply_additional_augmentations
from pyramid.data.transform import make_pil_data_generator

MAX_SIZE = 256
MAX_BACKGROUND_SIZE = (512, 512)
MAX_BACKGROUND_SHAPES = 64
FEW_BACKGROUND_SHAPES = 4


def draw_line(draw, coordinates, fill_color, outline_color):
    draw.line(coordinates, width=10, fill=fill_color)


def draw_ellipse(draw, coordinates, fill_color, outline_color):
    draw.ellipse(coordinates, fill=fill_color, outline=outline_color)


def draw_rectangle(draw, coordinates, fill_color, outline_color, w=1):
    draw.rectangle(coordinates, fill=fill_color, outline=outline_color, width=w)


def draw_pieslice(draw, coordinates, fill_color, outline_color):
    draw.pieslice(coordinates, 0, 45, fill=fill_color, outline=outline_color)


SHAPE_METHODS = {
    "line": draw_line,
    "ellipse": draw_ellipse,
    "rectangle": draw_rectangle,
    "pieslice": draw_pieslice,
}

SHAPES = sorted(SHAPE_METHODS.keys())


def random_color(rng):
    return (rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255))


def random_coordinates(xmin, ymin, xmax, ymax, rng):
    x1 = rng.randint(xmin, xmax - 1)
    y1 = rng.randint(ymin, ymax - 1)
    x2 = rng.randint(x1 + 1, xmax)
    y2 = rng.randint(y1 + 1, ymax)

    return x1, y1, x2, y2


def random_location(max_w, max_h, object_x, object_y, rng):
    diff_x = max_w - object_x
    diff_y = max_h - object_y

    x1 = rng.randint(min(0, diff_x), abs(diff_x))
    y1 = rng.randint(min(0, diff_y), abs(diff_y))
    x2 = x1 + object_x
    y2 = y1 + object_y

    return x1, y1, x2, y2


def draw_random_shape(draw, shape, image_shape, rng):
    max_w, max_h = image_shape
    method = SHAPE_METHODS[shape]
    coordinates = random_coordinates(0, 0, max_w, max_h, rng)
    fill_color = random_color(rng)
    outline_color = random_color(rng)

    method(draw, coordinates, fill_color, outline_color)

    return coordinates


def make_background(image_shape, rng):
    if rng.random() > 0.5:
        nshapes = rng.randint(FEW_BACKGROUND_SHAPES, MAX_BACKGROUND_SHAPES)
    else:
        nshapes = rng.randint(0, FEW_BACKGROUND_SHAPES)

    bg_color = random_color(rng)
    image = Image.new("RGB", image_shape, bg_color)
    draw = ImageDraw.Draw(image)

    for _ in range(nshapes):
        shape = rng.choice(SHAPES)
        draw_random_shape(draw, shape, image_shape, rng)

    return np.array(image)


def images_from_dir(adir):
    images = []

    for classdir in [adir] + sorted(glob.glob(os.path.join(adir, "*"))):
        if os.path.isdir(classdir):
            if classdir == adir:
                aclass = ""
            else:
                aclass = os.path.basename(classdir)

            for ext in ["gif", "png", "jpg", "jpeg"]:
                img_files = glob.glob(os.path.join(classdir, "*." + ext))

                for afile in sorted(img_files):
                    basename = os.path.basename(afile)
                    path = os.path.join(aclass, basename)
                    images.append({"file": path, "label": aclass, "weight": 1})

    return images


def split_images(images):
    labels = sorted(set([img["label"] for img in images]))
    class_arrays = {k: [] for k in labels}

    for img in images:
        class_arrays[img["label"]].append(img)

    return class_arrays


def foreground_generator(settings):
    image_root = settings.foreground_image_root
    images = images_from_dir(image_root)

    if settings.balance_objective:
        images_by_class = split_images(images)
        classes = sorted(images_by_class.keys())
    else:
        images_by_class = {"all": images}
        classes = ["all"]

    rng = random.Random(settings.augmentation_seed or settings.seed)

    max_size = np.array(settings.input_image_shape[:2])
    augmentations = settings.get_foreground_augmentations()
    augmenter = make_pil_data_generator(settings, None, augs=augmentations)

    while True:
        aclass = rng.choice(classes)
        instance = rng.choice(images_by_class[aclass])

        img = Image.open(os.path.join(image_root, instance["file"]))
        img = img.convert("RGBA")

        original_size = np.array(img.size)

        if np.any(original_size > max_size):
            scale = np.max(max_size / original_size)
            new_size = np.round(original_size * scale).tolist()
            img = img.resize([int(s) for s in new_size])

        if augmenter:
            rseed = rng.randint(0, MAX_INT_32 - 1)
            image = augmenter.random_transform(img, rseed)
        else:
            image = img

        yield image, str(instance["label"])


def background_generator(settings):
    image_root = settings.background_image_root
    images = images_from_dir(image_root)
    rng = random.Random(settings.augmentation_seed or settings.seed)

    out_size = settings.input_image_shape[:2]
    random_bg_rate = settings.random_background_rate
    augmentations = settings.get_background_augmentations()
    augmenter = make_image_data_generator(settings, None, augs=augmentations)

    while True:
        if random_bg_rate is None or rng.random() > random_bg_rate:
            instance = rng.choice(images)
            img = tf.io.read_file(os.path.join(image_root, instance["file"]))
            img = tf.image.decode_png(img, channels=3)
            img = tf.image.resize_with_crop_or_pad(
                img, out_size[1], out_size[0]
            ).numpy()
        else:
            img = make_background(MAX_BACKGROUND_SIZE, rng)

        if augmenter:
            rseed = rng.randint(0, MAX_INT_32 - 1)
            image = augmenter.random_transform(img, seed=rseed)
            image = apply_additional_augmentations(augmenter, image)

            yield Image.fromarray(image.astype(np.uint8)).resize(out_size)


def add_foreground(foregrounds, bimg, bg_size, occupancy, rng):
    fimg, label = next(foregrounds)

    fg_max_size = [occupancy * d for d in bg_size]
    scale = min([m / f for m, f in zip(fg_max_size, fimg.size)])
    new_fg_size = [int(round(scale * d)) for d in fimg.size]
    fimg = fimg.resize(new_fg_size)

    width, height = bg_size
    fg_loc = random_location(width, height, fimg.size[0], fimg.size[1], rng)

    # Here we're using the image with transparency in the region
    # filled in due to rotation; the last argument uses the image
    # itself as the transparency mask
    bimg.paste(fimg, fg_loc, fimg)

    return label, np.array(fg_loc)


def make_example(backgrounds, foregrounds, settings, rng):
    full_bg = next(backgrounds)

    if rng.random() > 0.5:
        # Non-square image
        if rng.random() > 0.5:
            big = full_bg.size[1]
            bg_size = [full_bg.size[0], rng.randint(big // 2, big)]
        else:
            big = full_bg.size[0]
            bg_size = [rng.randint(big // 2, big), full_bg.size[1]]

        crop = [bg_size[1], bg_size[0], 3]
        rseed = rng.randint(0, MAX_INT_32 - 1)
        bg_arr = tf.image.random_crop(np.array(full_bg), crop, seed=rseed)
        bimg = Image.fromarray(bg_arr.numpy().astype(np.uint8))
    else:
        bg_size = full_bg.size
        bimg = full_bg

    if settings.empty_image_rate and rng.random() < settings.empty_image_rate:
        n_foregrounds = 0
    else:
        n_foregrounds = rng.randint(1, settings.max_foreground_images)

    size_range = settings.occupancy_range
    occupancy_high = size_range[1]

    labels = []
    locations = []

    for i in range(n_foregrounds):
        occupancy = rng.uniform(size_range[0], occupancy_high)
        label, loc = add_foreground(foregrounds, bimg, bg_size, occupancy, rng)
        labels.append(label)
        locations.append(loc)

        # Later objects are guaranteed to be smaller to limit occlusions
        occupancy_high = max(size_range[0], occupancy_high / 2)

    margin = settings.bounding_box_margin or 0
    box_margin = np.array([-margin, -margin, margin, margin])

    return np.array(bimg), labels, [loc + box_margin for loc in locations]


def image_generator(settings):
    bgs = background_generator(settings)
    fgs = foreground_generator(settings)
    rng = random.Random(settings.augmentation_seed or settings.seed)

    def gen():
        yield make_example(bgs, fgs, settings, rng)

    dtypes = (tf.float32, tf.string, tf.int32)
    return tf.data.Dataset.from_generator(gen, dtypes).repeat()
