import pathlib
import yaml


class ConfigDict(dict):
    """
    Dictionary for managing training configuration parameters,
    loaded from a yaml file.
    """

    def opt(self, *args):
        """
        Retrieve an option from the config. If the option does not exist in the dict,
        an exception will be raise, unless a fallback value is provided, similarly to
        the get() function of a dict. To retrieve a nested option (e.g. an option that
        is stored in a sub-dictionary), use the '/' character. For example, to retrieve
        the batch size option:

            batch_size = config.opt('optimization/batch_size', 1)

        This will default to 1 if the batch_size parameter has not been defined under the
        optimization sub-dictionary.

        Parameters
        ----------
        option : str
            Option to retrieved from the config. Nested options can be divided with
            the '/' character.
        fallback : object, optional
            The fallback value to use if option is not found in
            the configuration dictionary.

        Returns
        -------
        object
            Retrieved parameter value, if found in the config.
        """
        if len(args) > 2 or len(args) == 0:
            raise ValueError('config.opt() requires an option to retrieve')
        # 
        keys = args[0].split('/')
        try:
            item = self
            for key in keys:
                item = item[key]
        except KeyError:
            if len(args) == 2:
                return args[1]
            else:
                raise RuntimeError(f'Option \'{args[0]}\' is missing from the config.')
        return item


def load_config(path):
    """
    Load a yaml file into a configuration dictionary.

    Parameters
    ----------
    path : str or Path
        Path to a yaml configuration file or a training base directory which
        contains a config.yaml file.

    Returns
    -------
    ConfigDict
        The loaded configuration dictionary.
    """
    path = pathlib.Path(path)

    if path.is_file():
        filename = path
    else:
        if not path.is_dir():
            print(f'error: training directory {path} does not exist.')
            exit(1)
        filename = path / 'config.yaml'
        if not filename.exists():
            print(f'error: expected config.yaml file in {path}.')
            exit(1)

    with open(filename, 'r') as f:
        config = yaml.safe_load(f)

    return ConfigDict(config)
