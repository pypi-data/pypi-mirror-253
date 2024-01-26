import pyramid.importers

np = pyramid.importers.import_numpy()
tf = pyramid.importers.import_tensorflow()

import time

from sensenet.constants import NUMERIC, CATEGORICAL, BOUNDING_BOX

from pyramid.data.dataset import validation_dataset
from pyramid.train.metrics import classification_metrics, regression_metrics
from pyramid.settings.bounding_box_loss import compute_bbox_losses
from pyramid.settings.objectives import create_objective

BASE_CHECK_WAIT = 4
UPDATE_SECONDS = 16
DEFAULT_PATIENCE = 32

HIGH_EPSILON_IMPROVEMENT = 1e-3
LOW_EPSILON_IMPROVEMENT = 1e-8

BAD_METRICS = "Invalid metrics (probably due to NaN). Learning terminating."


def set_backend_value(parameter, value):
    val = tf.keras.backend.get_value(value)
    tf.keras.backend.set_value(parameter, val)


class PyramidController(tf.keras.callbacks.Callback):
    def __init__(self, job_settings, validation_data):
        self._settings = job_settings

        self._max_training_time = job_settings.max_training_time or float("inf")
        self._max_iterations = job_settings.max_iterations or float("inf")
        self._patience = job_settings.patience or DEFAULT_PATIENCE
        self._update_secs = (
            job_settings.max_seconds_per_update or UPDATE_SECONDS
        )
        self._warmup = job_settings.learning_rate_warmup_iterations or 0
        self._base_learning_rate = job_settings.learning_rate

        self._objective_type = job_settings.objective_type
        self._start_time = job_settings.start_time
        self._valid_dataset = validation_dataset(job_settings, validation_data)
        self._loss = create_objective(job_settings)

        self._next_check = BASE_CHECK_WAIT
        self._last_progress = 0.0
        self._total_iterations = 0
        self._total_iteration_time = 0.0
        self._end_time = None
        self.reset_patience()

    def log_verbose(self, msg):
        self._settings.log_verbose(msg)

    def log_progress(self, status):
        self._settings.log_progress(status, self._last_progress)

    def log_message(self, msg):
        self.log_verbose(msg)
        self.log_progress({"message": msg})

    def log_warning(self, msg):
        self.log_verbose("WARNING: " + msg)
        self.log_progress({"message": "WARNING: " + msg})

    def reset_patience(self):
        current_time = time.time()

        self._last_update_time = current_time
        self._last_progress_time = current_time
        self._update_iterations = 0
        self._checks_since_improvement = 0
        self._phase_iterations = 0

    def do_check(self, current_time):
        if self._update_iterations >= self._next_check:
            return True
        else:
            if current_time - self._last_update_time > self._update_secs:
                return True
            else:
                return False

    def is_finished(self, current_time):
        msg = None

        if self._checks_since_improvement > self._patience:
            msg = "Maximum improvement checks  (%d >= %d) reached" % (
                self._checks_since_improvement,
                self._patience,
            )
        elif current_time - self._start_time > self._max_training_time:
            msg = "Maximum total training time  (%.2f > %.2f) reached" % (
                current_time - self._start_time,
                self._max_training_time,
            )
        elif self._total_iterations >= self._max_iterations:
            msg = "Maximum iterations (%d >= %d) reached" % (
                self._total_iterations,
                self._max_iterations,
            )

        if msg is not None:
            self.log_message(msg)
            return True
        else:
            return False

    def get_bbox_metrics(self):
        mvals = compute_bbox_losses(self.model, self._valid_dataset, self._loss)
        return {k: -float(mvals[k].numpy()) for k in mvals}

    def get_classifier_metrics(self):
        X, y = self._valid_dataset
        y_ = self.model.predict(X)

        if self._objective_type == NUMERIC:
            return regression_metrics(y, y_)
        elif self._objective_type == CATEGORICAL:
            if y_.shape[1] >= 1:
                return classification_metrics(y, y_)
            else:
                raise ValueError("Prediction shape is %s" % str(y_.shape))

    def get_validation_metrics(self):
        try:
            if self._objective_type == BOUNDING_BOX:
                metrics = self.get_bbox_metrics()
            else:
                metrics = self.get_classifier_metrics()
        except ValueError:
            raise ArithmeticError("Problem getting validation metrics")

        if np.any(np.isnan(list(metrics.values()))):
            raise ArithmeticError("NaN found in validation metrics")
        else:
            return metrics

    def improvement(self, metrics):
        low_improved = 0
        high_improved = 0

        if "total_loss" in metrics:
            delta = metrics["total_loss"] - self._best_metrics["total_loss"]

            if delta > LOW_EPSILON_IMPROVEMENT:
                return 1
            elif delta < -LOW_EPSILON_IMPROVEMENT:
                return -len(metrics) // 2
            else:
                return 0
        else:
            for key in metrics:
                delta = metrics[key] - self._best_metrics[key]

                if delta > HIGH_EPSILON_IMPROVEMENT:
                    high_improved += 1
                    low_improved += 1
                elif delta > LOW_EPSILON_IMPROVEMENT:
                    low_improved += 1
                elif delta < -LOW_EPSILON_IMPROVEMENT:
                    high_improved -= 1
                    low_improved -= 1

            if low_improved == 1:
                # Only net one metric improved; be conservative
                return high_improved
            else:
                return low_improved

    def report_metrics(self):
        if self._objective_type == CATEGORICAL:
            return "likelihood", "accuracy"
        elif self._objective_type == NUMERIC:
            return "r_squared", "mean_squared_error"
        elif self._objective_type == BOUNDING_BOX:
            return "ciou_loss", "confidence_loss"
        else:
            raise ValueError("Objective is %s" % self._objective_type)

    def metrics_string(self, metrics):
        m1, m2 = self.report_metrics()
        return "%s: %.4f, %s: %.4f" % (m1, metrics[m1], m2, metrics[m2])

    def log_improvement_message(self):
        metrics_str = self.metrics_string(self._best_metrics)
        self.log_verbose("-------- New best model: " + metrics_str)

    def log_update(self, imp, metrics):
        metrics_str = self.metrics_string(metrics)
        status_str = "Iteration: %d, n-improved: %d, checks: %d, " % (
            self._total_iterations,
            imp,
            self._checks_since_improvement,
        )

        self.log_verbose(status_str + metrics_str)

    def new_best_metrics(self, metrics):
        return {k: max(self._best_metrics[k], metrics[k]) for k in metrics}

    def on_train_begin(self, logs=None):
        self._best_metrics = self.get_validation_metrics()
        self._best_weights = self.model.get_weights()
        self.log_improvement_message()

    def on_train_batch_begin(self, batch, logs=None):
        if self._phase_iterations < self._warmup:
            decay = (self._phase_iterations / self._warmup) ** 2
            lr = self._base_learning_rate * decay
            set_backend_value(self.model.optimizer.lr, lr)

        current_time = time.time()
        since_progress = current_time - self._last_progress_time
        since_start = current_time - self._start_time

        self._iteration_start_time = current_time

        if since_progress > self._update_secs:
            m1, m2 = self.report_metrics()
            itr_prg = self._total_iterations / self._max_iterations
            time_prg = since_start / self._max_training_time

            self._last_progress = min(0.95, max(itr_prg, time_prg))
            self._last_progress_time = current_time

            if self._total_iterations > 0:
                itr_time = self._total_iteration_time / self._total_iterations
            else:
                itr_time = 0

            status = {
                "iterations": self._total_iterations,
                "seconds_per_iteration": itr_time,
                "time_elapsed": since_start,
                "checks": self._checks_since_improvement,
                m1: self._best_metrics[m1],
                m2: self._best_metrics[m2],
            }

            self.log_progress(status)

    def on_train_batch_end(self, batch, logs=None):
        current_time = time.time()
        self._total_iteration_time += current_time - self._iteration_start_time

        self._total_iterations += 1
        self._phase_iterations += 1
        self._update_iterations += 1

        if self.do_check(current_time):
            try:
                metrics = self.get_validation_metrics()
            except ArithmeticError:
                self.log_warning(BAD_METRICS)
                metrics = None

            if metrics is not None:
                imp = self.improvement(metrics)
                self.log_update(imp, metrics)
            else:
                self.model.stop_training = True
                imp = float("-inf")

            if imp > 0:
                self._best_metrics = self.new_best_metrics(metrics)
                self._checks_since_improvement = 0
            elif self._phase_iterations > self._warmup:
                self._checks_since_improvement += 1

            if imp >= 0:
                self._best_weights = self.model.get_weights()
                self.log_improvement_message()

            self._next_check = max(BASE_CHECK_WAIT, -imp * BASE_CHECK_WAIT)
            self._update_iterations = 0
            self._last_update_time = current_time

        if self.is_finished(time.time()):
            self.model.stop_training = True

    def on_train_end(self, logs=None):
        self.model.set_weights(self._best_weights)
        self._end_time = time.time()

    def fit_info(self):
        if self._end_time is not None:
            elapsed = self._end_time - self._start_time
        else:
            elapsed = None

        return {
            "iterations": self._total_iterations,
            "elapsed_time": elapsed,
            "validation_metrics": self._best_metrics,
        }
