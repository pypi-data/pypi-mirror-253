import pytest

def test_imports():
    try:
        import deepsurfer
        import numpy
        import scipy
        import yaml
        import surfa
        assert surfa.__version__ >= '0.5.0'
        import torch
        assert torch.__version__ >= '1.12'
    except ImportError:
        assert False, "One or more imports failed or are below the required version"
    else:
        assert True