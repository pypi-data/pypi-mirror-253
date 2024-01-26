import torch


def configure_device(cpu=False, threads=None, verbose=False):
    """
    Configure the PyTorch device.

    Parameters
    ----------
    cpu : bool, optional
        Whether to use CPU or GPU. Default is False, i.e., GPU is used.
    threads : int, optional
        Number of CPU threads to use. If None, uses all available threads.
    verbose : bool, optional
        Whether to print information about the device.

    Returns
    -------
    torch.device
        The configured PyTorch device.
    """
    if threads is not None:
        torch.set_num_threads(threads)
    device = torch.device('cuda' if torch.cuda.is_available() and not cpu else 'cpu')
    if verbose:
        print(f'Using device {device} and {torch.get_num_threads()} cpu threads')
    return device
