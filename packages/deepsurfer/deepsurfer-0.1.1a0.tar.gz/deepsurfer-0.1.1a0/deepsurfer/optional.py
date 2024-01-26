import importlib


class MissingModule(object):
    """
    A module that raises an exception on any attribute access.
    """

    def __init__(self, exception):
        super().__setattr__('exception', exception)

    def __getattr__(self, attr):
        raise super().__getattribute__('exception')

    def __setattr__(self, attr, value):
        raise super().__getattr__('exception')


def load_module(name):
    """
    Load a module, returning a MissingModule if it cannot be loaded.
    This is useful for optional dependencies.
    """
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError as e:
        module = MissingModule(e)
    return module


# if any module loaded here is missing, it will not throw an import error
# until any of the module attributes are attempted to be accessed
voxynth = load_module('voxynth')
