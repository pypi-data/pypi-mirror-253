import os
import sys
import json
import glob

import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

from sensenet.accessors import is_yolo_model
from sensenet.constants import BOUNDING_BOX
from sensenet.layers.construct import remove_weights
from sensenet.models.image import io_for_extractor
from sensenet.models.wrappers import create_model, convert

from pyramid.data.numpy import shape_data
from pyramid.settings.base_settings import BaseSettings, BOUNDING_BOX
from pyramid.settings.image import pretrained_weights_available, trainable_yolo
from pyramid.utils import find_invalid_value

INITIAL_MODEL_SETTINGS = {"regression_normalize": True}

FULL_DATASET = "full_dataset.npy"
EVALUATION_DATASET = "evaluation_dataset.npy"
IMPORTANCE_DATASET = "importance_dataset.npy"
SUBSET_FORMAT = "data_subset_%i.npy"

TREES_FILE = "trees.json"
TREE_IMPORTANCE_FILE = "tree_importances.json"

DIRECTORY_PREFIX = "submodel_"
FIT_INFO_JSON = "model_fit_info.json"
WEIGHTS_FILE = "model_weights.h5"
EVALUATIONS_JSON = "evaluations.json"


class JobSettings(BaseSettings):
    def __init__(self, amap):
        super(JobSettings, self).__init__(amap)

    def select_data(self, X):
        if X.shape[1] > self.number_of_inputs() and not self.tree_embedding:
            return X[:, self.tree_features() :]
        else:
            return X

    def read_json(self, filename):
        with open(os.path.join(self.output_directory, filename), "r") as fin:
            return json.load(fin)

    def read_evaluation_data(self):
        path = os.path.join(self.output_directory, EVALUATION_DATASET)
        X, y, _ = shape_data(np.load(path), self)
        X = self.select_data(X)

        return X, y

    def read_importance_data(self):
        path = os.path.join(self.output_directory, IMPORTANCE_DATASET)
        data = np.load(path)[:, :-1]

        return self.select_data(data)

    def list_submodels(self):
        globstr = os.path.join(self.output_directory, DIRECTORY_PREFIX + "*")
        return [adir.split(DIRECTORY_PREFIX)[1] for adir in glob.glob(globstr)]

    def model_directory(self, model_id):
        mdir = DIRECTORY_PREFIX + (model_id or self.get_job_id())
        os.makedirs(os.path.join(self.output_directory, mdir), exist_ok=True)

        return mdir

    def model_resource(self, afile, model_id):
        return os.path.join(self.model_directory(model_id), afile)

    def read_fit_info(self, model_id):
        return self.read_json(self.model_resource(FIT_INFO_JSON, model_id))

    def read_evaluation(self, model_id):
        try:
            eval_path = self.model_resource(EVALUATIONS_JSON, model_id)
            return self.read_json(eval_path)
        except FileNotFoundError:
            return None

    def get_weight_path(self, model_id):
        return os.path.join(
            self.output_directory, self.model_resource(WEIGHTS_FILE, model_id)
        )

    def load_weights(self, model, model_id):
        model.load_weights(self.get_weight_path(model_id))

    def load_trees(self):
        if self.is_search or self.tree_embedding:
            return self.read_json(TREES_FILE)
        else:
            return None

    def load_tree_importances(self):
        return self.read_json(TREE_IMPORTANCE_FILE)

    def get_image_network_metadata(self):
        return get_pretrained_network(self.base_image_network)

    def make_image_model(self, use_trained_weights):
        load_pretrained_weights = False

        if (
            self.is_image_training_job()
            and pretrained_weights_available(self.base_image_network)
            and (self.use_pretrained() or self.fine_tune())
        ):

            load_pretrained_weights = True

        base_model = self.create_base_image_model(load_pretrained_weights)

        if self.objective_type == BOUNDING_BOX:
            if self.is_image_training_job() or self.is_finalizing_job():
                model = trainable_yolo(self, base_model, True)

                if use_trained_weights:
                    self.load_weights(model, self.get_image_model_id())
            else:
                raise ValueError(
                    "Bounding box model and non-image training job"
                )
        else:
            inputs, base_features = io_for_extractor(base_model)
            _, outputs = self.make_layer_sequence(base_features, self.layers)
            model = tf.keras.Model(inputs=inputs, outputs=outputs)

            if use_trained_weights or self.is_caching_job():
                self.load_weights(model, self.get_image_model_id())

            if self.is_caching_job():
                inputs, features = io_for_extractor(base_model)
                model = tf.keras.Model(inputs=inputs, outputs=features)

        return model

    def set_training_option(self, name, value):
        self.__setattr__(name, value)
        self.training_options[name] = value

    def initial_model_reset(self, document):
        metadata = document["image_network"]["metadata"]

        self.set_training_option("tree_embedding", None)
        self.set_training_option("layers", remove_weights(document["layers"]))
        self.set_training_option("initial_network_metadata", metadata)

        info = self.get_settings_info()

        assert document["output_exposition"] == info["output_exposition"]
        assert document["preprocess"] == info["preprocess"]

    def make_model(self, use_trained_weights):
        if self.initial_model and "initial_model" in self.base_image_network:
            if use_trained_weights:
                assert self.initial_network_metadata is not None
                model = self.make_image_model(True)
            else:
                self.log_setup("Reading model from %s..." % self.initial_model)

                with open(self.initial_model, "r") as fin:
                    model_doc = json.load(fin)

                self.initial_model_reset(model_doc)
                self.log_setup("Creating pretrained model...")
                base_model = create_model(model_doc, INITIAL_MODEL_SETTINGS)

                if self.objective_type == BOUNDING_BOX:
                    model = trainable_yolo(self, base_model._model, False)
                else:
                    model = base_model._model

            return model
        elif self.is_image_training_job():
            return self.make_image_model(use_trained_weights)
        else:
            inputs, outputs = self.make_layer_sequence()
            model = tf.keras.Model(inputs=inputs, outputs=outputs)

            if use_trained_weights:
                self.load_weights(model, self.get_job_id())

            return model

    def write_numpy(self, array, filename):
        path = os.path.join(self.output_directory, filename)
        np.save(path, array)

        return path

    def write_importance_data(self, array):
        return self.write_numpy(array, IMPORTANCE_DATASET)

    def write_evaluation_data(self, array):
        return self.write_numpy(array, EVALUATION_DATASET)

    def write_full_dataset(self, array):
        return self.write_numpy(array, FULL_DATASET)

    def write_subdataset(self, array, i):
        return self.write_numpy(array, SUBSET_FORMAT % i)

    def write_json(self, obj, filename, pretty=False):
        apath = os.path.join(self.output_directory, filename)
        with open(apath, "w") as f:
            try:
                if pretty:
                    json.dump(obj, f, allow_nan=False, indent=4, sort_keys=True)
                else:
                    json.dump(obj, f, allow_nan=False)
            except ValueError:
                bad_path = find_invalid_value(obj, [])
                raise ValueError("Out of range value at %s" % str(bad_path))

        return apath

    def write_weights(self, model, model_id):
        model.save_weights(self.get_weight_path(model_id))

    def write_trees(self, tree_info):
        self.write_json(tree_info["importances"], TREE_IMPORTANCE_FILE)
        self.write_json(tree_info["trees"], TREES_FILE)

    def write_network(self, model, fit_info, evaluations):
        mid = self.get_job_id()

        if fit_info is None:
            fi = {"training_options": self.training_options}
        else:
            fi = fit_info

        self.write_json(fi, self.model_resource(FIT_INFO_JSON, mid))
        self.write_weights(model, mid)

        if evaluations is not None:
            eval_path = self.model_resource(EVALUATIONS_JSON, mid)
            self.write_json(evaluations, eval_path)

    def write_h5(self, wrapped_model, pathname):
        apath = os.path.join(self.output_directory, pathname)
        convert(wrapped_model, None, apath, "h5")

        return apath

    def write_bundle(self, wrapped_model, bundle_name, tfjs_name):
        bundle_path = os.path.join(self.output_directory, bundle_name)
        tfjs_path = os.path.join(self.output_directory, tfjs_name)

        wrapped_model.save_bundle(bundle_path, tfjs_path=tfjs_path)

        return bundle_path, tfjs_path
