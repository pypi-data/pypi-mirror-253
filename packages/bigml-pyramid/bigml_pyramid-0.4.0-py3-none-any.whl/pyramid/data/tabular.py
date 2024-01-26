import random

import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()
sci_stats = pyramid.importers.import_scipy_stats()

from pyramid.data.stratify import split_by_class

AUTOTUNE = tf.data.experimental.AUTOTUNE
sample_from_datasets = tf.data.experimental.sample_from_datasets


def to_dataset(settings, numpy_arrays):
    ds_len = numpy_arrays[0].shape[0]
    dataset = tf.data.Dataset.from_tensor_slices(numpy_arrays)
    return dataset.shuffle(ds_len, seed=settings.seed).repeat()


def standard_dataset(settings, numpy_arrays):
    dataset = to_dataset(settings, numpy_arrays)
    return dataset.batch(settings.batch_size).prefetch(buffer_size=AUTOTUNE)


def balanced_dataset(settings, numpy_arrays, raw_dataset=False):
    subsets = split_by_class(numpy_arrays)
    datasets = [to_dataset(settings, arrays) for arrays in subsets]
    bal = [1.0 / len(datasets) for _ in range(len(datasets))]
    combined = sample_from_datasets(datasets, weights=bal, seed=settings.seed)

    if raw_dataset:
        return combined
    else:
        return combined.batch(settings.batch_size).prefetch(
            buffer_size=AUTOTUNE
        )


def mixup_generator(settings, numpy_arrays):
    subsets = split_by_class(numpy_arrays)

    rng = random.Random(settings.seed)
    beta_dist = sci_stats.beta(settings.mixup_alpha, settings.mixup_alpha)
    betas = list(beta_dist.rvs(random_state=settings.seed, size=4096))

    nclasses = len(subsets)
    nclassesminus1 = nclasses - 1
    nbetas = len(betas)

    def gen():
        while True:
            if nclasses > 1:
                c1 = rng.randrange(nclasses)
                c2 = rng.randrange(nclassesminus1)

                if c2 == c1:
                    c2 = nclassesminus1
            else:
                c1 = c2 = 0

            i1 = rng.randrange(subsets[c1][0].shape[0])
            i2 = rng.randrange(subsets[c2][0].shape[0])

            X1, y1, w1 = subsets[c1]
            X2, y2, w2 = subsets[c2]

            p1 = (X1[i1, :], y1[i1, :], w1[i1])
            p2 = (X2[i2, :], y2[i2, :], w2[i2])

            lamda = betas[rng.randrange(nbetas)]
            oneminuslamda = 1 - lamda

            yield tuple(
                [lamda * v1 + oneminuslamda * v2 for v1, v2 in zip(p1, p2)]
            )

    return gen


def mixup_dataset(settings, numpy_arrays):
    gen = mixup_generator(settings, numpy_arrays)
    dtypes = (tf.float32, tf.float32, tf.float32)
    dshapes = tuple([a.shape[1:] for a in numpy_arrays])

    dataset = tf.data.Dataset.from_generator(gen, dtypes, dshapes)
    return dataset.batch(settings.batch_size).prefetch(buffer_size=AUTOTUNE)
