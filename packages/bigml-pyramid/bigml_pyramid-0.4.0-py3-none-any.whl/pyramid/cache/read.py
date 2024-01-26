import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import random

from sensenet.constants import NUMERIC, CATEGORICAL, IMAGE

from pyramid.serialize.data import lazy_rows
from pyramid.serialize.utils import get_feature_lengths, get_row_size


def row_subset(settings):
    row_size = get_row_size(settings)

    if row_size * settings.cache_rows < settings.max_data_size:
        return None
    else:
        rng = random.Random(settings.seed)
        nrows = int(max(1, np.floor(settings.max_data_size / row_size)))

        return set(rng.sample(list(range(settings.cache_rows)), nrows))


def get_image_projector(settings):
    read = settings.image_file_reader()
    model = settings.make_image_model(True)

    def project(apath):
        image = np.expand_dims(read(apath).numpy(), axis=0)
        return model.predict(image)[0]

    return project


def data_to_numpy(settings):
    row_set = row_subset(settings)
    nrows = len(row_set) if row_set is not None else settings.cache_rows
    ncols = settings.data_width()

    status = {"total_rows_to_cache": nrows}
    types = [f["type"] for f in settings.info_list]
    f_lengths = get_feature_lengths(settings)

    if settings.has_image_inputs():
        image_projector = get_image_projector(settings)

    with open(settings.cache_file, "rb") as fin:
        data = np.zeros((nrows, ncols), dtype=np.float32)

        for i, values in enumerate(lazy_rows(fin, settings.info_list, row_set)):
            if i % 100 == 0:
                status["row_number"] = i + 1
                settings.log_progress(status, 0.9 * (i / nrows))

            row_idx = 0

            for j, value in enumerate(values):
                if types[j] == NUMERIC:
                    data[i, row_idx] = value
                elif types[j] == CATEGORICAL:
                    intval = int(value)

                    if intval >= 0:
                        data[i, row_idx + intval] = 1.0
                elif types[j] == IMAGE:
                    features = image_projector(str(value, "utf-8"))
                    data[i, row_idx : (row_idx + f_lengths[j])] = features

                row_idx += f_lengths[j]

    status["row_number"] = nrows
    settings.log_progress(status, 0.9)

    return data
