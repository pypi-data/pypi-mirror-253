import pyramid.importers

np = pyramid.importers.import_numpy()
sci_special = pyramid.importers.import_scipy_special()

import random
import math

from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageDraw

MAX_BLUR = 32
CUTOUT_FILL = (128, 128, 128, 255)
EMPTY_FILL = (0, 0, 0, 0)

AUGMENTATION_PARAMETERS = {
    "blur": 0.5,
    "brightness": 0.1,
    "contrast": 0.25,
    "color_invert": True,
    "cutout": 0.25,
    "deform": 0.1,
    "gaussian_noise": 0.1,
    "glare": 0.1,
    "height_shift": 0.1,
    "horizontal_flip": True,
    "rotation": 10.0,
    "shear": 10.0,
    "tint": 0.1,
    "vertical_flip": True,
    "width_shift": 0.1,
    "zoom": 0.1,
}

BOOLEAN_AUGMENTATIONS = ["height_shift", "width_shift", "color_invert"]


def not_implemented(op):
    def raise_error(image, arg, rng):
        raise NotImplementedError("'%s' transformation is not available" % op)

    return raise_error


def distance_grid(shape, point):
    reference = np.array(point)[:, np.newaxis, np.newaxis]
    xd, yd = np.meshgrid(np.arange(shape[1]), np.arange(shape[0])) - reference

    xd = xd / shape[0]
    yd = yd / shape[1]

    return np.sqrt(xd * xd + yd * yd)


def white_ellipse(shape, point1, point2, scale):
    d1 = distance_grid(shape, point1)
    d2 = distance_grid(shape, point2)
    total_dist = (d1 + d2) / 2

    dref = np.percentile(total_dist, scale)
    dmin = np.min(total_dist)

    return 255 * sci_special.expit((dref - total_dist) / (dref - dmin))


def numpy_glare(anarray, arg, rng):
    shape = anarray.shape
    p1 = [d * rng.random() for d in shape[:2]]
    p2 = [d * rng.random() for d in shape[:2]]
    scale = rng.random() * arg * 100

    noise = white_ellipse(shape, p1, p2, scale)
    return np.clip(anarray + noise[:, :, np.newaxis], 0, 255)


def numpy_noise(anarray, arg, rng):
    noise = anarray * rng.standard_normal(size=anarray.shape)
    return np.clip(anarray + (noise * arg), 0, 255)


def numpy_invert(anarray, arg, rng):
    anarray[:, :, :3] = 255.0 - anarray[:, :, :3]
    return anarray


def numpy_tint(anarray, arg, rng):
    channels = rng.integers(low=0, high=2, size=3)
    shift = (rng.random((3,)) - 0.5) * arg
    tint = shift * channels + 1.0

    outarray = np.zeros(anarray.shape, dtype=np.float32)
    outarray[:, :, :3] = anarray[:, :, :3] * tint[np.newaxis, np.newaxis, :]
    outarray[:, :, 3] = anarray[:, :, 3]

    return np.round(np.clip(outarray, 0, 255))


def apply_numpy_transformation(tfn, image, arg, rng):
    anarray = np.array(image)
    new_array = tfn(anarray, arg, rng)

    return Image.fromarray(new_array.astype(np.uint8), mode="RGBA")


def blur(image, arg, rng):
    max_blur_kernel_size = max(2, min(MAX_BLUR, int(round(1 / (1 - arg)))))
    radius = rng.integers(low=1, high=max_blur_kernel_size, size=1)[0]

    if radius <= 1:
        return image
    else:
        return image.filter(ImageFilter.BoxBlur(radius))


def brightness(image, arg, rng):
    delta = rng.uniform(1.0 - arg, 1.0 + arg)
    enhancer = ImageEnhance.Brightness(image)

    return enhancer.enhance(delta)


def contrast(image, arg, rng):
    delta = rng.uniform(1.0 - arg, 1.0 + arg)
    enhancer = ImageEnhance.Contrast(image)

    return enhancer.enhance(delta)


def color_invert(image, arg, rng):
    if rng.random() > 0.5:
        return apply_numpy_transformation(numpy_invert, image, arg, rng)
    else:
        return image


def cutout(image, arg, rng):
    if rng.random() > 0.5:
        min_dim = np.min(image.size)
        box_size = math.ceil(min_dim * arg)
        x1 = rng.integers(low=0, high=image.size[0] - box_size, size=1)[0]
        y1 = rng.integers(low=0, high=image.size[1] - box_size, size=1)[0]
        x2 = x1 + box_size
        y2 = y1 + box_size

        draw = ImageDraw.Draw(image)
        draw.rectangle((x1, y1, x2, y2), fill=CUTOUT_FILL)

    return image


def gaussian_noise(image, arg, rng):
    if rng.random() > 0.5:
        return apply_numpy_transformation(numpy_noise, image, arg, rng)
    else:
        return image


def glare(image, arg, rng):
    if rng.random() > 0.5:
        return apply_numpy_transformation(numpy_glare, image, arg, rng)
    else:
        return image


def height_shift(image, arg, rng):
    width, height = image.size
    shift = rng.integers(low=0, high=int(round(arg * height)) + 1, size=1)[0]
    shifted_image = Image.new("RGBA", (width, height + shift), EMPTY_FILL)
    shifted_image.paste(image, (0, shift), image)

    return shifted_image


def horizontal_flip(image, arg, rng):
    if rng.random() > 0.5:
        return ImageOps.mirror(image)
    else:
        return image


def rotation(image, arg, rng):
    angle = rng.uniform(-arg, arg)

    return image.rotate(
        angle, expand=True, resample=Image.BICUBIC, fillcolor=EMPTY_FILL
    )


def find_coeffs(source_coords, target_coords):
    matrix = []

    for s, t in zip(source_coords, target_coords):
        matrix.append([t[0], t[1], 1, 0, 0, 0, -s[0] * t[0], -s[0] * t[1]])
        matrix.append([0, 0, 0, t[0], t[1], 1, -s[1] * t[0], -s[1] * t[1]])

    A = np.matrix(matrix, dtype=np.float32)
    B = np.array(source_coords).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)

    return np.array(res).reshape(8)


def deform(image, arg, rng):
    if rng.random() > 0.5:
        width, height = image.size
        original = [(0, 0), (width, 0), (width, height), (0, height)]

        height_mod = rng.random() * arg * height
        width_mod = rng.random() * arg * width

        changed = [tuple(t) for t in original]

        for i, change in enumerate([width_mod, height_mod]):
            idx = rng.integers(low=0, high=4, size=1)[0]
            new_coord = list(changed[idx])

            if changed[idx][i] > 0:
                new_coord[i] -= change
            else:
                new_coord[i] += change

            changed[idx] = tuple(new_coord)

        mat = find_coeffs(original, changed)
        return image.transform(
            image.size, Image.PERSPECTIVE, mat, Image.BICUBIC
        )
    else:
        return image


def tint(image, arg, rng):
    if rng.random() > 0.5:
        return apply_numpy_transformation(numpy_tint, image, arg, rng)
    else:
        return image


def vertical_flip(image, arg, rng):
    if rng.random() > 0.5:
        return ImageOps.flip(image)
    else:
        return image


def width_shift(image, arg, rng):
    width, height = image.size
    shift = rng.integers(low=0, high=int(round(arg * width)) + 1, size=1)[0]
    shifted_image = Image.new("RGBA", (width + shift, height), EMPTY_FILL)
    shifted_image.paste(image, (shift, 0), image)

    return shifted_image


def zoom(image, arg, rng):
    scale_amt = rng.uniform(1.0 - arg, 1.0 + arg)
    return ImageOps.scale(image, scale_amt)


TRANSFORMERS = {
    "blur": blur,
    "brightness": brightness,
    "contrast": contrast,
    "color_invert": color_invert,
    "cutout": cutout,
    "deform": deform,
    "gaussian_noise": gaussian_noise,
    "glare": glare,
    "height_shift": height_shift,
    "horizontal_flip": horizontal_flip,
    "rotation": rotation,
    "shear": not_implemented("shear"),
    "tint": tint,
    "vertical_flip": vertical_flip,
    "width_shift": width_shift,
    "zoom": zoom,
}


class PILGenerator:
    def __init__(self, transformations):
        self._transformation_args = {}

        for key in transformations:
            if transformations[key]:
                self._transformation_args[key] = transformations[key]

    def random_transform(self, image, random_seed):
        self._rng = np.random.default_rng(seed=random_seed)
        transformed = image

        transformations = sorted(self._transformation_args.keys())
        self._rng.shuffle(transformations)

        for transformation in transformations:
            tfn = TRANSFORMERS[transformation]
            arg = self._transformation_args[transformation]
            transformed = tfn(transformed, arg, self._rng)

        return transformed


def make_augmentation_ranges(augs, excluded):
    ranges = {}

    for key in AUGMENTATION_PARAMETERS:
        if key in BOOLEAN_AUGMENTATIONS:
            ranges[key] = False
        else:
            ranges[key] = 0.0

    for key in augs:
        if excluded is None or key not in excluded:
            if isinstance(augs, dict) and augs[key] is not None:
                if key in BOOLEAN_AUGMENTATIONS:
                    ranges[key] = bool(augs[key])
                else:
                    ranges[key] = float(augs[key])
            else:
                ranges[key] = AUGMENTATION_PARAMETERS[key]

    return ranges


def make_pil_data_generator(settings, excluded, fill=None, augs=None):
    if augs is not None:
        ranges = make_augmentation_ranges(augs, excluded)
        return PILGenerator(ranges)
    else:
        return None
