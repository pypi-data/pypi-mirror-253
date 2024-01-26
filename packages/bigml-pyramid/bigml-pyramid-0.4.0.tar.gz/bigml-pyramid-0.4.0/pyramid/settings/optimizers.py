import pyramid.importers

tf = pyramid.importers.import_tensorflow()

optimizers = tf.keras.optimizers


def adadelta(settings, learning_rate):
    return optimizers.Adadelta(
        learning_rate=learning_rate,
        rho=settings.rho or 0.95,
        epsilon=settings.epsilon or 1e-07,
    )


def adagrad(settings, learning_rate):
    init_accum = settings.init_accumulator or 0.1

    return optimizers.Adagrad(
        learning_rate=learning_rate,
        initial_accumulator_value=init_accum,
        epsilon=settings.epsilon or 1e-07,
    )


def adam(settings, learning_rate):
    return optimizers.Adam(
        learning_rate=learning_rate,
        beta_1=settings.beta1 or 0.9,
        beta_2=settings.beta2 or 0.999,
        epsilon=settings.epsilon or 1e-07,
    )


def adamax(settings, learning_rate):
    return optimizers.Adamax(
        learning_rate=learning_rate,
        beta_1=settings.beta1 or 0.9,
        beta_2=settings.beta2 or 0.999,
        epsilon=settings.epsilon or 1e-07,
    )


def ftrl(settings, learning_rate):
    init_accum = settings.init_accumulator or 0.1
    learn_pow = settings.learning_rate_power or -0.5
    l1_reg = settings.l1_regularization or 0.0
    l2_reg = settings.l2_regularization or 0.0

    return optimizers.Ftrl(
        learning_rate=learning_rate,
        learning_rate_power=learn_pow,
        initial_accumulator_value=init_accum,
        l1_regularization_strength=l1_reg,
        l2_regularization_strength=l2_reg,
    )


def momentum(settings, learning_rate):
    return optimizers.SGD(
        learning_rate=learning_rate,
        momentum=settings.momentum or 0.9,
        nesterov=True,
    )


def nadam(settings, learning_rate):
    return optimizers.Nadam(
        learning_rate=learning_rate,
        beta_1=settings.beta1 or 0.9,
        beta_2=settings.beta2 or 0.999,
        epsilon=settings.epsilon or 1e-07,
    )


def rms_prop(settings, learning_rate):
    return optimizers.RMSprop(
        learning_rate=learning_rate,
        momentum=settings.momentum or 0.0,
        rho=settings.rho or 0.9,
        epsilon=settings.epsilon or 1e-07,
    )


def sgd(settings, learning_rate):
    return optimizers.SGD(
        learning_rate=learning_rate,
        momentum=settings.momentum or 0.9,
        nesterov=False,
    )


OPTIMIZERS = {
    "adadelta": adadelta,
    "adagrad": adagrad,
    "adam": adam,
    "adamax": adamax,
    "ftrl": ftrl,
    "momentum": momentum,
    "nadam": nadam,
    "rms_prop": rms_prop,
    "sgd": sgd,
}


def create_optimizer(settings, learning_rate):
    return OPTIMIZERS[settings.descent_algorithm](settings, learning_rate)
