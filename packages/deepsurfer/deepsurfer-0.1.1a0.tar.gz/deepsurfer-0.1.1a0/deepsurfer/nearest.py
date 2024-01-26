import numpy as np
import torch

from scipy.spatial import cKDTree

from . import extension


def nearest_neighbor(a, b, size_a=None, size_b=None):
    """
    Compute nearest neighbors between two sets of 3D points.

    Parameters
    ----------
    a, b : Tensor
        Tensors of shape (P, 3) or (batch, P, 3) representing point coordinates,
        where P is the number of points, which can differ between sets A and B.
    size_a, size_b : Tensor, optional
        Tensors of shape (B,) specifying the number of points in each batch. Only
        applicable if A and B have a batch dimension.

    Returns
    -------
    Tensor
        Tensor representing the indices of B nearest to each point in A.
    """
    if a.ndim != b.ndim or a.ndim > 3:
        raise ValueError('expected input of shape (points, dim) or (batch, points, dim) '
                        f'but got {a.shape} and {b.shape}')

    a = a.detach()
    b = b.detach()

    batched = a.ndim != 2
    if not batched:
        a = a.unsqueeze(0)
        b = b.unsqueeze(0)

    if size_a is None:
        size_a = torch.full([a.shape[0]], a.shape[1], dtype=torch.int64, device=a.device)
    if size_b is None:
        size_b = torch.full([b.shape[0]], b.shape[1], dtype=torch.int64, device=b.device)

    if a.shape[0] != size_a.shape[0]:
        raise ValueError(f'expected size_a to match batch size of a ')
    if b.shape[0] != size_b.shape[0]:
        raise ValueError(f'expected size_b to match batch size of b ')

    if a.is_cuda:
        a = a.type(torch.float32)
        b = b.type(torch.float32)
        nn = extension.nearest_neighbor_cuda(a, b, size_a, size_b)
    else:
        nn = np.zeros(a.shape[:2], dtype=np.int64)
        for i in range(a.shape[0]):
            x = a[i, :size_a[i]]
            y = b[i, :size_b[i]]
            nn[i, :size_a[i]] = cKDTree(y).query(x, workers=-1)[1]
        nn = torch.tensor(nn)

    if not batched:
        nn = nn.squeeze(0)
    return nn
