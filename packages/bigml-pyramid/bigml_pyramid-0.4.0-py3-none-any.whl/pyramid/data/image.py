import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import os
import random
import math

from sensenet.accessors import get_image_shape
from sensenet.preprocess.image import rescale

from pyramid.constants import MAX_INT_32, BG_CONSTANT
from pyramid.data.tabular import balanced_dataset
from pyramid.data.transform import numpy_glare, numpy_noise
from pyramid.data.transform import AUGMENTATION_PARAMETERS
from pyramid.data.transform import make_augmentation_ranges
from pyramid.data.stratify import DEFAULT_HOLDOUT_RATE

AUTOTUNE = tf.data.experimental.AUTOTUNE
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator

FUNCTION_AUGMENTATIONS = ["blur", "cutout", "gaussian_noise", "glare"]
GENERATOR_ONLY = ["rotation", "shear", "glare"]


def read_from_path(settings, shape, path):
    img = tf.io.read_file(path)
    img = tf.image.decode_png(img, channels=3)

    return tf.cast(rescale(settings, shape, img), tf.float32)


def read_image(settings, shape, from_disk, image):
    if from_disk:
        path = tf.strings.join([settings.image_root + os.sep, image[0]])
        return read_from_path(settings, shape, path)
    else:
        return image


def read_images(settings, numpy_arrays):
    root = settings.image_root
    image_shape = get_image_shape(settings)

    paths = [os.path.join(root, str(p[0])) for p in numpy_arrays[0]]
    imgs = [read_from_path(settings, image_shape, p).numpy() for p in paths]

    return (np.array(imgs, dtype=np.float32), numpy_arrays[1], numpy_arrays[2])


def blur_image(image, image_shape, blur_amount, seed):
    if len(image_shape) == 4:
        dims = image_shape[1:3]
    else:
        dims = image_shape[:2]

    scale = 1 - tf.random.uniform((), seed=seed) * blur_amount
    little_dims = tf.maximum(1, tf.cast(tf.round(scale * dims), tf.int32))
    little = tf.image.resize(image, little_dims)

    return tf.image.resize(little, dims)


def tf_transformer(settings, from_disk, no_augmentations):
    seed = settings.augmentation_seed or settings.seed
    image_shape = get_image_shape(settings)

    if no_augmentations:
        ranges = {k: None for k in AUGMENTATION_PARAMETERS}
    else:
        augmentations = settings.get_augmentations()
        ranges = make_augmentation_ranges(augmentations, None)

    def transformer(Xin, y, w):
        X = read_image(settings, image_shape, from_disk, Xin)

        if ranges["brightness"]:
            delta = ranges["brightness"] * 255.0
            X = tf.image.random_brightness(X, max_delta=delta, seed=seed)
            X = tf.clip_by_value(X, 0.0, 255.0)

        if ranges["zoom"]:
            zoom = ranges["zoom"]
            max_h = math.ceil((1.0 + zoom) * image_shape[1])
            max_w = math.ceil((1.0 + zoom) * image_shape[2])
            X = tf.image.resize(X, [max_h, max_w])
            X = tf.image.random_crop(X, size=image_shape[1:], seed=seed)

        if ranges["height_shift"] or ranges["width_shift"]:
            max_h = math.ceil((1.0 + ranges["height_shift"]) * image_shape[1])
            max_w = math.ceil((1.0 + ranges["width_shift"]) * image_shape[2])
            X = tf.image.resize_with_crop_or_pad(X, max_h, max_w)
            X = tf.image.random_crop(X, size=image_shape[1:], seed=seed)

        if ranges["horizontal_flip"]:
            X = tf.image.random_flip_left_right(X, seed=seed)

        if ranges["vertical_flip"]:
            X = tf.image.random_flip_up_down(X, seed=seed)

        if ranges["contrast"]:
            crange = ranges["contrast"]
            X = tf.image.random_contrast(X, 1 - crange, 1 + crange, seed=seed)
            X = tf.clip_by_value(X, 0.0, 255.0)

        if ranges["gaussian_noise"]:
            s1 = seed + 1
            mag = ranges["gaussian_noise"]

            noise = X * tf.random.normal(image_shape[1:], stddev=mag, seed=seed)
            do_noise = tf.cast(tf.random.uniform((), seed=s1) > 0.5, tf.float32)
            X = tf.clip_by_value(X + (noise * X * do_noise), 0.0, 255.0)

        if ranges["cutout"]:
            min_dim = min(image_shape[1], image_shape[2])
            box_size = math.ceil(min_dim * ranges["cutout"])
            max_h = (2 * (image_shape[1] - box_size)) + box_size
            max_w = (2 * (image_shape[2] - box_size)) + box_size

            box = tf.ones((box_size, box_size, 3), dtype=np.float32) * 127
            box_image = tf.image.resize_with_crop_or_pad(box, max_h, max_w)
            mask = tf.image.random_crop(
                box_image, size=image_shape[1:], seed=seed
            )

            do_mask = tf.random.uniform((), seed=seed) > 0.5
            mask = mask * tf.cast(do_mask, tf.float32)

            X = X * tf.cast(mask == 0, X.dtype) + mask

        if ranges["blur"]:
            s2 = seed + 2
            do_blur = lambda: blur_image(X, image_shape, ranges["blur"], seed)
            X = tf.cond(
                tf.random.uniform((), seed=s2) > 0.5, do_blur, lambda: X
            )

        if ranges["color_invert"]:
            s3 = seed + 3
            invert = lambda: 255 - X
            X = tf.cond(tf.random.uniform((), seed=s3) > 0.5, invert, lambda: X)

        return X, y, w

    return transformer


def make_additional_augmentations(settings, ranges):
    image_shape = get_image_shape(settings)
    min_dim = min(image_shape[1], image_shape[2])

    blur_amount = ranges["blur"]
    glare = ranges["glare"]
    mag = ranges["gaussian_noise"]
    contrast_range = ranges["contrast"]
    cutsize = math.ceil(ranges["cutout"] * min_dim)

    cutout = cutsize > 0
    gaussian_noise = mag > 0
    blur = blur_amount > 0
    contrast = contrast_range > 0
    invert = ranges["color_invert"]

    pad = [1, 1, 1, 1]
    rng = np.random.RandomState(settings.augmentation_seed or settings.seed)

    def more_augmentations(image):
        new_image = np.array(image, copy=True)
        shape = new_image.shape

        if contrast:
            adj = rng.uniform(1 - contrast_range, 1 + contrast_range)
            mean = new_image.mean(axis=(0, 1))
            centered = new_image - mean
            new_image = np.clip(centered * adj + mean, 0, 255)

        if gaussian_noise and rng.uniform() < 0.5:
            new_image = numpy_noise(new_image, mag, rng)

        if cutout and rng.uniform() < 0.5:
            cy = rng.randint(image_shape[1] - cutsize)
            cx = rng.randint(image_shape[2] - cutsize)

            new_image[cy : cy + cutsize, cx : cx + cutsize] = 128.0

        if blur and rng.uniform() < 0.5:
            rseed = rng.randint(MAX_INT_32)
            new_image = blur_image(new_image, shape, blur_amount, rseed).numpy()

        if glare and rng.uniform() < 0.5:
            new_image = numpy_glare(new_image, glare, rng)

        if invert and rng.uniform() < 0.5:
            new_image = 255 - new_image

        return new_image

    return more_augmentations


def make_image_data_generator(settings, excluded, fill="nearest", augs=None):
    if augs is None:
        ranges = make_augmentation_ranges(
            settings.get_augmentations(), excluded
        )
    else:
        ranges = make_augmentation_ranges(augs, excluded)

    if ranges:
        if any(ranges[augmentation] for augmentation in FUNCTION_AUGMENTATIONS):
            more_augmentations = make_additional_augmentations(settings, ranges)
        else:
            more_augmentations = None

        brightness_range = (1 - ranges["brightness"], 1 + ranges["brightness"])

        return ImageDataGenerator(
            rotation_range=ranges["rotation"],
            shear_range=ranges["shear"],
            width_shift_range=ranges["width_shift"],
            height_shift_range=ranges["height_shift"],
            brightness_range=brightness_range,
            zoom_range=ranges["zoom"],
            horizontal_flip=ranges["horizontal_flip"],
            vertical_flip=ranges["vertical_flip"],
            fill_mode=fill,
            cval=BG_CONSTANT,
            preprocessing_function=more_augmentations,
        )
    else:
        return None


def make_training_image_generator(settings, excluded):
    return make_image_data_generator(settings, excluded)


def apply_additional_augmentations(augmenter, image):
    more_augmentations = augmenter.preprocessing_function

    if more_augmentations:
        return more_augmentations(image)
    else:
        return image


def generator_transformer(settings, from_disk, no_augmentations):
    seed = settings.seed
    image_shape = get_image_shape(settings)
    nclasses = settings.number_of_classes()

    if no_augmentations:
        augmenter = None
    else:
        augmenter = make_training_image_generator(settings, None)

    def transform(Xin, y, w):
        nonlocal seed

        X = read_image(settings, image_shape, from_disk, Xin)

        if augmenter is not None:
            X = augmenter.random_transform(X.numpy(), seed=seed)
            X = apply_additional_augmentations(augmenter, X)

        # Keep this to a 32-bit int; numpy has overflow problems
        # in its random seed
        seed = (seed + 1) % MAX_INT_32

        return X, y, w

    dtypes = (tf.float32, tf.float32, tf.float32)

    def to_image_row(Xi, yi, wi):
        X, y, w = tf.py_function(func=transform, inp=[Xi, yi, wi], Tout=dtypes)

        return [
            tf.ensure_shape(X, image_shape[1:]),
            tf.ensure_shape(y, (nclasses,)),
            tf.ensure_shape(w, ()),
        ]

    return to_image_row


def transformer(settings, from_disk, is_holdout):
    has_augmentations = (not is_holdout) and settings.get_augmentations()
    must_gen = any(
        aug in settings.get_augmentations() for aug in GENERATOR_ONLY
    )

    if must_gen and has_augmentations:
        return generator_transformer(settings, from_disk, not has_augmentations)
    else:
        return tf_transformer(settings, from_disk, not has_augmentations)


def estimate_size(settings, numpy_arrays):
    ds_len = numpy_arrays[0].shape[0]
    im_floats = np.prod([ds_len] + list(settings.input_image_shape))

    return 4 * im_floats + numpy_arrays[1].nbytes + numpy_arrays[2].nbytes


def leave_on_disk(settings, numpy_arrays, is_holdout):
    holdout_rate = settings.holdout_rate or DEFAULT_HOLDOUT_RATE

    if is_holdout:
        max_size = settings.max_data_size * holdout_rate
    else:
        max_size = settings.max_data_size * (1 - holdout_rate)

    return estimate_size(settings, numpy_arrays) > max_size


def arrays_and_transformer(settings, numpy_arrays, is_holdout):
    from_disk = leave_on_disk(settings, numpy_arrays, is_holdout)
    arrays = numpy_arrays if from_disk else read_images(settings, numpy_arrays)
    transform = transformer(settings, from_disk, is_holdout)

    return arrays, transform


def image_dataset(settings, numpy_arrays):
    arrays, transform = arrays_and_transformer(settings, numpy_arrays, False)
    dataset = balanced_dataset(settings, arrays, raw_dataset=True)

    if not settings.get_augmentations():
        augmented = dataset.map(transform, num_parallel_calls=AUTOTUNE)
    else:
        augmented = dataset.map(transform, num_parallel_calls=1)

    return augmented.batch(settings.batch_size).prefetch(buffer_size=AUTOTUNE)


def image_validation_dataset(settings, numpy_arrays):
    arrays, transform = arrays_and_transformer(settings, numpy_arrays, True)
    dataset = tf.data.Dataset.from_tensor_slices(arrays)
    image_dataset = dataset.map(transform, num_parallel_calls=AUTOTUNE)

    return image_dataset.batch(1).prefetch(buffer_size=AUTOTUNE)
