import torch
import pathlib

from ..system import error
from ..system.formatting import formatted

try:
    from . import _cuda_extension
    available = True
except:
    available = False


def check_cuda_extension():
    """
    Check whether the deepsurfer cuda extensions have been built and can be
    loaded. These extensions are really only necessary for running a few things
    on the GPU, mainly the topofit intersection fix and training functionality.
    """
    if available:
        return True

    cuda_version = torch.version.cuda

    error('Cannot load deepsurfer cuda extensions.\n')
    message = f'''
    It looks like you are running some stuff on the GPU but do not have the
    deepsurfer cuda extensions that are required for this particular functionality.
    Good luck figuring that one out!

    Just kidding, it's not too difficult as long as you are using conda to manage
    your packages. If not, then you'll have to download and configure the cuda
    development toolkits on your own, which sounds way out of my league.

    Make sure you are running deepsurfer from source, and not from a pip install.
    You first need to install the cudatoolkit-dev conda package version corresponding
    to the cuda that your torch package was built with. It looks like your torch is
    using cuda {cuda_version}, so you can run:

    <DIM>conda install -c conda-forge cudatoolkit-dev={cuda_version}

    You might want to double check the versioning here. This will install the relevant
    cuda libraries and, importantly, install the nvcc compiler into the bin/ subdirectory
    of your conda environment.

    Make sure you are logged into a machine with a GPU device, and from the
    top-level of the deepsurfer source repository, run:

    <DIM>python build.py build_ext --inplace

    This will build the cuda c++ extension and install it into the package source
    tree. Note that this extension will only work for your current python version
    and torch-cuda version, so if you update torch (with a different cuda version)
    or run this deepsurfer source with a different python distribution, it will fail.
    '''
    print(formatted(message))
    exit(1)


def nearest_neighbor_cuda(*args):
    """
    Wrapper around the nearest neighbor cuda extension. This function shouldn't be called
    directly. Instead use `ds.nearest.nearest_neighbor()` for the device-independent method.
    """
    check_cuda_extension()
    return _cuda_extension.nearest_neighbor(*args)


def mark_self_intersecting_faces_cuda(*args):
    """
    Wrapper around the intersection marking cuda extension. This function shouldn't be called directly.
    Instead use `ds.surf.mesh.mark_self_intersecting_faces()` for the device-independent method.
    """
    check_cuda_extension()
    return _cuda_extension.mark_self_intersecting_faces(*args)
