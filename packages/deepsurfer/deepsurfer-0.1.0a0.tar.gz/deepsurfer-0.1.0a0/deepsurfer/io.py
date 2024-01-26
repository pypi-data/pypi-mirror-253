import inspect
import functools
import importlib
import torch

from deepsurfer.system import version
from deepsurfer.system import fatal


def load_model(filename, strict=True, device=None, update=None, expected=None, newclass=None):
    """
    Load model from a saved file, including its initialization parameters and weights.
    The saved file must be created using the `save` method of a `LoadableModule` subclass.

    Parameters
    ----------
    filename : str
        The file path to the saved model.
    strict : bool, optional
        If True, load the model in strict mode, where weights must match target architecture.
    device : str or torch.device, optional
        The device to load the model onto.
    update : dict, optional
        A dictionary containing updated keyword arguments for the loaded model.
    expected : type, optional
        The expected class of the loaded model.
    newclass : type, optional
        The class type to force the model to be loaded as.

    Returns
    -------
    LoadableModel
        The loaded model.
    """
    loaded = torch.load(filename, map_location=device)
    module = loaded.get('package_module')
    name   = loaded.get('class_name')
    kwargs = loaded.get('class_kwargs')

    if not all([module, name, kwargs]):
        raise ValueError(f'model file {filename} does not appear like it '
                         'was saved as a LoadableModule subclass')

    this_version = version.current_version()
    that_version = version.parse_version(loaded.get('deepsurfer_version'))

    min_version = loaded.get('min_version')
    if min_version is not None and this_version < version.parse_version(min_version):
        raise ValueError(f'loading model file \'{filename}\' requires deepsurfer '
                         f'{min_version} but you have version {this_version}')

    def throw_load_error(message):
        message = f'error when loading model from \'{filename}\'\n\n{message}\n'
        if this_version != that_version:
            message = (f'{message}\nNote that the model was saved with '
                       f'deepsurfer version {that_version}, and you\'re '
                       f'using version {this_version}\n')
        raise ValueError(message)

    if newclass is None:
        try:
            m = importlib.import_module(module)
            classtype = getattr(m, name)
        except (ModuleNotFoundError, AttributeError):
            throw_load_error(f'The saved module class {module}.{name} no longer '
                'appears to exist in the package. Most likely the class location '
                'has changed or been renamed in the code. If you know the renamed '
                'model class, it can be specified with the \'newclass\' argument')
        if expected is not None and expected != classtype:
            raise ValueError(f'Expected {expected.__name__} model in file {filename}, '
                             f'but got {classtype.__name__}')
    else:
        classtype = newclass

    if update is not None:
        if not isinstance(update, dict):
            raise ValueError(f'update param must be a dict, but got type {type(update)}')
        kwargs.update(update)

    accepted_params = list(inspect.signature(classtype).parameters.keys())
    for param in kwargs.keys():
        if not param in accepted_params:
            throw_load_error(f'{name}() got an unexpected keyword argument \'{param}\'. '
                 'Most likely the __init__ method has been modified. To load and '
                 'change the saved model arguments, use the load_model_kwargs() method.')

    model = classtype(**kwargs)
    model.load_state_dict(loaded['model_state_dict'], strict=strict)
    if device is not None:
        model = model.to(device)
    return model


def load_model_kwargs(filename):
    """
    Load only the cached initialization arguments from a "loadable" model file.

    Parameters
    ----------
    filename : str
        Model file to load parameters from.

    Returns
    -------
    dict
        Initialization parameters as keyword argument dictionary.
    """
    return torch.load(filename).get('class_kwargs')


def store_config_args(func):
    """
    Class-method decorator that saves every argument provided to the
    function as a dictionary in 'self.config'. This is used to assist
    model loading - see LoadableModel.
    """
    attrs, varargs, varkw, defaults = inspect.getargspec(func)

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        self._cached_kwargs = {}

        # first save the default values
        if defaults:
            for attr, val in zip(reversed(attrs), reversed(defaults)):
                self._cached_kwargs[attr] = val

        # next handle positional args
        for attr, val in zip(attrs[1:], args):
            self._cached_kwargs[attr] = val

        # lastly handle keyword args
        if kwargs:
            for attr, val in kwargs.items():
                self._cached_kwargs[attr] = val

        return func(self, *args, **kwargs)
    return wrapper


class LoadableModule(torch.nn.Module):
    """
    Base module to facilitate torch model IO that automatically accounts
    for model architecture configuration.

    Any modules that inherit from this class will have initialization
    arguments cached internally (accessible by the `kwargs` dictionary).
    When writing a model, these cached parameters will be included in the
    saved file, along with information like module class name and deepsurfer
    version. This way, when loading the model file, the module can be reconstructed
    using the same parameters without any manual specification.
    """
    def __init__(self, *args, **kwargs):
        # this constructor is just functions as a check to make sure that every
        # LoadableModule subclass has provided an internal _cached_kwargs parameter
        # either manually or via store_config_args (preffered)
        if not hasattr(self, '_cached_kwargs'):
            raise NotImplementedError(
                'modules that inherit from LoadableModule must decorate the __init__ '
                'method like so:\n\n'
                'class Module(ds.io.LoadableModule):\n\n'
                '    @ds.io.store_config_args\n'
                '    def __init__(self, ...):\n'
                '        ...\n')
        super().__init__(*args, **kwargs)

    @property
    def kwargs(self):
        """
        The cached model initialization arguments as a keyword argument dictionary.
        """
        return self._cached_kwargs

    @property
    def device(self):
        """
        The device of the model parameters.
        """
        return next(self.parameters()).device

    def save(self, filename, optimizer_state_dict=None):
        """
        Save the model weights and initialization parameters to disk.

        Parameters
        ----------
        filename : str
            The file path to save the model to.
        optimizer_state_dict : dict, optional
            A dictionary containing the optimizer state, which includes information such as
            the current learning rate and momentum. If provided, this information will also
            be saved along with the model weights and initialization parameters.
        """
        classtype = self.__class__
        d = {
            'package_module': classtype.__module__,
            'class_name': classtype.__qualname__,
            'class_kwargs': self.kwargs,
            'deepsurfer_version': str(version.current_version()),
            'model_state_dict': self.state_dict().copy(),
        }
        if optimizer_state_dict is not None:
            d['optimizer_state_dict'] = optimizer_state_dict
        torch.save(d, filename)


def remove_optimizer_state_from_model_file(filename):
    """
    Remove the optimizer state dictionary from a saved "loadable" model file.

    Parameters
    ----------
    filename : str
        The file path of the PyTorch model file to modify. Note that this
        file will be overwritten with the updated model file.
    """
    d = torch.load(filename, map_location='cpu')
    d.pop('optimizer_state_dict')
    torch.save(d, filename)


def edit_min_version_required_by_model_file(filename, min_version):
    """
    Edit the minimum version required by a saved "loadable" model file.

    Parameters
    ----------
    filename : str
        The file path of the PyTorch model file to modify. Note that this
        file will be overwritten with the updated model file.
    min_version : str
        The new minimum version required by the model.
    """
    d = torch.load(filename, map_location='cpu')
    d['min_version'] = str(parse_version(min_version))
    torch.save(d, filename)    
