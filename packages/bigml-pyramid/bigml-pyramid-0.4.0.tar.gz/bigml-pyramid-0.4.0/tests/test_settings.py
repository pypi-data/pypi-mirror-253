import traceback

from sensenet.constants import CATEGORICAL

from pyramid.settings.job_settings import JobSettings
from pyramid.settings.optimizers import create_optimizer
from pyramid.utils import find_invalid_value

from .utils import TEST_OUTPUT


def check_alg(descent_alg, is_param, param_name, param_value):
    lr = 0.42
    amap = {"descent_algorithm": descent_alg, "learning_rate": lr}

    if is_param:
        amap[param_name] = param_value

    settings = JobSettings(amap)
    optimizer = create_optimizer(settings, settings.learning_rate)

    if param_name == "beta1":
        assert optimizer.beta_1 == param_value, optimizer.beta_1
    elif param_name == "beta2":
        assert optimizer.beta_2 == param_value, optimizer.beta_2
    elif param_name == "momentum":
        assert optimizer.momentum == param_value, optimizer.momentum
    elif param_name == "rho":
        assert optimizer.rho == param_value, optimizer.rho
    elif param_name == "init_accumulator":
        assert optimizer.initial_accumulator_value == param_value
    else:
        raise RuntimeError("You gotta check SOMETHING!")

    assert optimizer.learning_rate == lr


def test_optimizer():
    tests = [
        ("nadam", False, "beta1", 0.9),
        ("adam", True, "beta1", 0.799),
        ("adamax", True, "beta2", 0.799),
        ("ftrl", False, "init_accumulator", 0.1),
        ("adagrad", True, "init_accumulator", 0.5),
        ("adadelta", True, "rho", 0.95),
        ("sgd", True, "momentum", 0.24),
        ("momentum", False, "momentum", 0.9),
        ("rms_prop", False, "momentum", 0.0),
    ]

    for descent_alg, is_param, param_name, param_value in tests:
        check_alg(descent_alg, is_param, param_name, param_value)


def test_seed():
    for seed_value in [4000000000, -1, -40000000000]:
        try:
            JobSettings({"seed": seed_value})
            raise ValueError("Should have gotten an error: %d" % seed_value)
        except AssertionError:
            pass

    JobSettings({"seed": 0})
    JobSettings({"seed": 2100000000})


def test_failed_settings():
    tests = [
        ("descent_algorithm", "some_crazy_thing"),
        ("init_accumulator", -0.5),
        ("learning_rate", -1),
        ("learning_rate_power", 0.5),
        ("beta1", -5),
    ]

    for test in tests:
        key, value = test
        try:
            JobSettings({key: value})
            raise ValueError("Should have gotten an error: %s" % str(test))
        except AssertionError:
            pass

        js = JobSettings({})

        try:
            js.__setattr__(key, value)
            raise ValueError("Should have gotten an error: %s" % str(test))
        except AssertionError:
            pass

    js = JobSettings({})

    try:
        js.non_attribute = True
        raise ValueError("Should have gotten an error setting non_attribute")
    except AttributeError:
        pass

    js.descent_algorithm = "nadam"
    js.learning_rate = 1e-3


def test_simple_network_construct():
    little = {
        "base_image_network": "simple",
        "image_training_type": "randomly_initialize",
        "input_image_shape": [64, 64, 3],
        "objective_type": CATEGORICAL,
    }

    big = dict(little)
    big["input_image_shape"] = [256, 256, 3]

    ls = JobSettings(little)
    bs = JobSettings(big)

    assert 128 == ls.image_network()["image_network"]["metadata"]["outputs"]
    assert 128 == bs.image_network()["image_network"]["metadata"]["outputs"]


def test_residual_network_construct():
    little = {
        "base_image_network": "simple_residual",
        "image_training_type": "randomly_initialize",
        "input_image_shape": [64, 64, 3],
        "objective_type": CATEGORICAL,
    }

    big = dict(little)
    big["input_image_shape"] = [256, 256, 3]

    ls = JobSettings(little)
    bs = JobSettings(big)

    assert 256 == ls.image_network()["image_network"]["metadata"]["outputs"]
    assert 1024 == bs.image_network()["image_network"]["metadata"]["outputs"]


def test_nan_output():
    settings = JobSettings(
        {
            "output_directory": TEST_OUTPUT,
        }
    )

    structure = [
        {
            "a": [1, 2, {"aa": "hello", "x": -3.0, "b": {"c": 0, "d": 5}}],
            "c": [1, 2, [1, 2.0, 3], [1, 2, {"d": [1, 2, 3, [4, 5, 6]]}]],
        }
    ]

    try:
        settings.write_json(structure, "test.json")
    except:
        assert False

    structure[0]["a"][2]["b"]["bad"] = float("nan")

    try:
        settings.write_json(structure, "test.json")
        assert False
    except ValueError:
        path = find_invalid_value(structure, [])
        assert path == [0, "a", 2, "b", "bad"]
