import os
import sys
import time

from sensenet.constants import CATEGORICAL

import pyramid.importers

np = pyramid.importers.import_numpy()

from pyramid.settings.base_settings import IMAGE_TRAINING
from pyramid.settings.job_settings import JobSettings
from pyramid.data.dataset import make_dataset
from pyramid.data.generate import image_generator
from pyramid.data.image import read_images, leave_on_disk, estimate_size
from pyramid.data.numpy import image_dicts_to_numpy, read_numpy_arrays

from .utils import image_rows_from_directory, clean_temp
from .utils import TEST_DATA_DIR, DIGIT_ROOT

SERIALIZED_IMAGE_INFO_LIST = [
    {"index": 0, "type": "image"},
    {"index": 1, "type": "numeric", "mean": 2.0, "stdev": -2.0},
    {"index": 2, "type": "numeric", "mean": 12, "stdev": 1},
    {"index": 3, "type": "numeric", "mean": -1, "stdev": 1},
    {"index": 4, "type": "image"},
    {"index": 5, "type": "image"},
    {"index": 6, "type": "categorical", "values": ["a", "b", "c"]},
    {"index": 7, "type": "categorical", "values": ["a", "b", "c"]},
]

CLASS_NAMES = np.array(["Three", "Eight"])


def setup_module(module):
    clean_temp()


def teardown_module(module):
    clean_temp()


def show_batch(batch, is_tensors=True):
    import matplotlib.pyplot as plt

    if is_tensors:
        image_batch = batch[0].numpy()
        label_batch = batch[1].numpy()
    else:
        image_batch = batch[0]
        label_batch = batch[1]

    plt.figure(figsize=(10, 10))

    for n in range(16):
        ax = plt.subplot(4, 4, n + 1)
        plt.imshow(image_batch[n].astype(np.uint8))

        if is_tensors:
            cname = CLASS_NAMES[label_batch[n] == 1][0].title()
        else:
            cname = str(label_batch[n])

        plt.title(cname)
        plt.axis("off")

    plt.show()


def time_batches(ds, batch_size, steps):
    start = time.time()
    it = iter(ds)

    for i in range(steps):
        batch = next(it)

    end = time.time()
    duration = end - start

    sys.stdout.write("%.2f images/sec ... " % (batch_size * steps / duration))
    sys.stdout.flush()


def check_batch(tensors, nrows, nclasses, has_weights):
    X, y, w = tensors

    assert len(X.shape) == 4
    assert X.shape[0] == nrows
    assert X.shape[1] == X.shape[2] == 32
    assert X.shape[3] == 3

    assert len(y.shape) == 2
    assert y.shape[0] == nrows, str((y.shape, nrows))
    assert y.shape[1] == nclasses, str((y.shape, nclasses))

    assert len(w.shape) == 1, w.shape
    assert w.shape == (nrows,)

    if nclasses > 1:
        assert np.all(np.isin(y, [0, 1]))
    else:
        assert np.all(y < 0)

    if not has_weights:
        assert np.all(w == 1)
    else:
        assert not np.all(w == 1)


def make_image_dataset(max_data_size, check=True, aug_seed=None, augs=None):
    data = image_rows_from_directory(DIGIT_ROOT)
    default_augs = ["color_invert", "contrast"]

    settings = JobSettings(
        {
            "image_root": DIGIT_ROOT,
            "objective_type": CATEGORICAL,
            "input_image_shape": [32, 32, 3],
            "max_data_size": max_data_size,
            "batch_size": 16,
            "seed": max_data_size + 42,
            "augmentation_seed": aug_seed,
            "image_augmentations": default_augs if augs is None else augs,
            "job_type": IMAGE_TRAINING,
            "info_list": [
                {"type": "image"},
                {"type": "categorical", "values": ["3", "8"]},
            ],
        }
    )

    npdata = image_dicts_to_numpy(data, settings)
    dataset = make_dataset(settings, npdata)

    if check:
        time_batches(dataset, 16, 512)

        for batch in dataset.take(128):
            # show_batch(batch)
            check_batch(batch, 16, 2, False)

    return dataset


def test_estimate_size():
    settings = JobSettings(
        {
            "input_image_shape": [28, 28, 3],
            "image_root": DIGIT_ROOT,
            "objective_type": CATEGORICAL,
        }
    )

    data = image_rows_from_directory(DIGIT_ROOT)
    npdata = image_dicts_to_numpy(data, settings)
    np_arrays = read_images(settings, npdata)

    assert len(npdata[0].shape) == 2
    assert len(np_arrays[0].shape) == 4

    actual_size = np.sum([arr.nbytes for arr in np_arrays])
    estimated_size = estimate_size(settings, npdata)

    assert actual_size == estimated_size, (actual_size, estimated_size)


def test_memory_dataset():
    make_image_dataset(1024000, aug_seed=1)


def test_generator_dataset():
    make_image_dataset(1024000, augs=["color_invert", "rotation"])


def test_disk_dataset():
    make_image_dataset(1024)


def dataset_batches(from_disk, augs):
    if from_disk:
        return make_image_dataset(1024, check=False, augs=augs).take(32)
    else:
        return make_image_dataset(1024000, check=False, augs=augs).take(32)


def test_consistency():
    bs1 = [b for b in iter(dataset_batches(True, []))]
    bs2 = [b for b in iter(dataset_batches(True, []))]

    for b1, b2 in zip(bs1, bs2):
        assert np.array_equal(b1[1].numpy(), b2[1].numpy())
        assert np.array_equal(b1[0].numpy(), b2[0].numpy())


def test_augmented_consistency():
    bs1 = [b for b in iter(dataset_batches(False, None))]
    bs2 = [b for b in iter(dataset_batches(False, None))]

    for b1, b2 in zip(bs1, bs2):
        assert np.array_equal(b1[1].numpy(), b2[1].numpy())
        assert np.array_equal(b1[0].numpy(), b2[0].numpy())


def test_cache_images():
    settings = JobSettings(
        {
            "info_list": SERIALIZED_IMAGE_INFO_LIST,
            "cache_file": os.path.join(TEST_DATA_DIR, "image.ser"),
            "cache_rows": 5,
            "job_type": IMAGE_TRAINING,
            "objective_type": CATEGORICAL,
        }
    )

    X, y, w = read_numpy_arrays(settings)
    nrows = 15

    assert X.shape == (nrows, 1)
    assert y.shape == (nrows, 3)
    w.shape == (nrows,)


def test_pil_generator():
    settings = JobSettings(
        {
            "foreground_image_root": DIGIT_ROOT,
            "background_image_root": DIGIT_ROOT,
            "input_image_shape": [256, 256, 3],
            "augmentation_seed": 43,
            "random_background_rate": 1.0,
            "occupancy_range": [0.25, 0.75],
            "max_foreground_images": 3,
            "foreground_augmentation_ranges": {
                "zoom": None,
                "blur": None,
                "brightness": None,
                "rotation": None,
                "deform": None,
                "cutout": None,
                "glare": None,
                "contrast": None,
                "gaussian_noise": None,
                "color_invert": True,
                "horizontal_flip": True,
                "vertical_flip": True,
            },
        }
    )

    dataset = image_generator(settings)

    images = []
    labels = []

    for batch in dataset.take(64):
        images.append(batch[0].numpy())
        labels.append((batch[1].numpy()))

        if len(images) == 16:
            # show_batch((images, labels), is_tensors=False)
            images = []
            labels = []
