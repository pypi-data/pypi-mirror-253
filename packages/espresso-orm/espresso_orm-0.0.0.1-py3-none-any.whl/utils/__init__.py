import importlib

from ...espresso_orm.model import EspressoModel


def first(x: list):
    return x[0] if len(x) else None


# Define the logging format
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"


def get_related_model(cls, model_name):
    models_module_name = ".".join(cls.__module__.split(".")[:-1])
    models_module = importlib.import_module(models_module_name)
    models = {
        class_name: model
        for class_name in dir(models_module)
        if isinstance(model := getattr(models_module, class_name), type)
        and issubclass(model.__class__, EspressoModel.__class__)
    }
    return models.get(model_name)
