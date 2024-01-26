import os
import pathlib
import sys
import warnings
import torch

from setuptools import setup
from torch.utils.cpp_extension import CUDA_HOME, CUDAExtension


base_dir = pathlib.Path(__file__).parent.parent

# Check for CUDA availability
if not (torch.cuda.is_available() and CUDA_HOME is not None):
    sys.exit('ERROR: CUDA is not available. CUDA must be installed to build this package.')


csrc_dir = base_dir / 'deepsurfer' / 'extension'
sources = [
    csrc_dir / 'nearest.cu',
    csrc_dir / 'intersection.cu',
    csrc_dir / 'extension.cxx',
]

extra_compile_args = {'cxx': ['-std=c++14']}
nvcc_args = [
    '-DCUDA_HAS_FP16=1',
    '-D__CUDA_NO_HALF_OPERATORS__',
    '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__',
    '-std=c++14',
]

if os.name != 'nt':
    nvcc_args.append('-std=c++14')

# starting CUDA-toolkut 12.0, CUB is included in the toolkit
# https://github.com/NVIDIA/cccl/discussions/520
cub_home = os.environ.get('CUB_HOME', None)

if cub_home is None:
    cub_home = os.environ.get('CONDA_PREFIX', os.environ.get('CUDA_HOME', None))
    if cub_home:
        cub_home += '/include'


if cub_home is None:
    warnings.warn('The env var `CUB_HOME` was not found. NVIDIA '
                  'CUB is required for compilation.')
else:
    nvcc_args.append(f'-I{cub_home}')

# Allow custom NVCC flags from the environment
nvcc_flags_env = os.getenv('NVCC_FLAGS', '')
if nvcc_flags_env:
    nvcc_args.extend(nvcc_flags_env.split(' '))

ext_modules = [
    CUDAExtension(
        'deepsurfer.extension._cuda_extension',
        sources=[str(source.relative_to(base_dir)) for source in sources],
        include_dirs=[str(csrc_dir)],
        define_macros=[('WITH_CUDA', None), ('THRUST_IGNORE_CUB_VERSION_CHECK', None)],
        extra_compile_args={'cxx': ['-std=c++14'], 'nvcc': nvcc_args}
    )
]

setup(
    name='deepsurfer',
    ext_modules=ext_modules,
    include_package_data=True,
    cmdclass={'build_ext': torch.utils.cpp_extension.BuildExtension}
)