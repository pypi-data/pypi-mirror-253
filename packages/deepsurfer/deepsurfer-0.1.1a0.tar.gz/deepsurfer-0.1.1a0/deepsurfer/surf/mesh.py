import warnings
import surfa as sf
import numpy as np
import torch

from ..nearest import nearest_neighbor
from .. import extension


def compute_face_normals(triangles, normalize=True):
    """
    Computes the normal vectors of the faces of a triangular mesh.

    Parameters
    ----------
    triangles : Tensor
        Tensor of shape (F, 3, 3) representing the vertices of each face.
    normalize : bool, optional
        If True, the normal vectors are normalized.

    Returns
    -------
    normals : Tensor
        Tensor of shape (F, 3) representing the normal vector of each face.
    """
    diffs = torch.diff(triangles, dim=1)
    vectors = torch.cross(diffs[:, 0], diffs[:, 1])
    if normalize:
        vectors = torch.nn.functional.normalize(vectors, p=2, dim=-1)
    return vectors


def compute_face_areas(triangles):
    """
    Compute the area of the faces of a triangular mesh.

    Parameters
    ----------
    triangles : Tensor
        Tensor of shape (F, 3, 3) representing the vertices of each face.

    Returns
    -------
    areas : Tensor
        Tensor of shape (F,) representing the area of each face.
    """
    norms = compute_face_normals(triangles, normalize=False)
    return torch.norm(norms, p=2, dim=-1) / 2


def compute_vertex_normals(vertices, faces, zeros=None):
    """
    Compute the normal vectors of the vertices of a triangular mesh.

    Parameters
    ----------
    vertices : Tensor
        Tensor of shape (V, 3) representing the vertices of the mesh.
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.
    zeros : Tensor, optional
        Pre-allocated tensor of shape (V, 3) representing the zero vector
        at each vertex. This is used as the initial buffer for gathering
        normals across faces, and computation might be (very) slightly sped
        up if it is pre-allocated. If None, it is allocated on the fly.

    Returns
    -------
    normals : Tensor
        Tensor of shape (V, 3) representing the normal vector at each vertex.
    """
    face_normals = compute_face_normals(vertices[faces])
    buffer = zeros if zeros is not None else torch.zeros(vertices.shape, dtype=torch.float32, device=vertices.device)
    buffer = buffer.scatter_add(-2, faces[..., 0:1].expand(-1, 3), face_normals)
    buffer = buffer.scatter_add(-2, faces[..., 1:2].expand(-1, 3), face_normals)
    buffer = buffer.scatter_add(-2, faces[..., 2:3].expand(-1, 3), face_normals)
    return torch.nn.functional.normalize(buffer, p=2, dim=-1)


def sample_grid(data, points, gridshape=None):
    """
    Interpolates data at given points on a regular 3D grid with C channels.

    Parameters
    ----------
    data : Tensor
        Tensor of shape (C, X, Y, Z).
    points : Tensor
        Tensor of shape (N, 3) representing the coordinates of each point.
    gridshape : Tensor, optional
        Tensor of shape (3,) representing the shape of the grid. If None, it
        is inferred from the shape of `data`.

    Returns
    -------
    sampled : Tensor
        Tensor of shape `(N, C)` representing the data sampled at each point.
    """
    if gridshape is None:
        gridshape = torch.tensor(data.shape[1:], device=data.device)

    half = (gridshape - 1) / 2
    points = (points - half) / half
    npoints = points.shape[0]
    points = torch.reshape(points, (1, points.shape[0], 1, 1, points.shape[1]))

    data = data.unsqueeze(0).swapaxes(-1, -3)

    sampled = torch.nn.functional.grid_sample(data, points, align_corners=True, mode='bilinear')
    sampled = sampled.reshape((-1, npoints)).swapaxes(-1, -2)
    return sampled


def dilate(mask, faces, iters=1):
    """
    Dilate a binary mask by the edges of a triangular mesh.

    Parameters
    ----------
    mask : Tensor
        Tensor of shape (V,) representing the binary mask.
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.
    iters : int, optional
        Number of iterations to perform the dilation.

    Returns
    -------
    dilated_mask : Tensor
        Tensor of shape `(V,)` representing the dilated binary mask.
    """
    source = faces.reshape(-1)
    target = faces.roll(1, dims=-1).reshape(-1)

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        for i in range(iters):
            mask = mask.scatter_reduce(0, target, mask[source], reduce='amax')

    return mask


def chamfer_distances(a, b, square=False):
    """
    Compute the chamfer distances between two sets of points in 3D space.

    Parameters
    ----------
    a : Tensor
        The first set of points in 3D space. Its shape is (N, 3), where N
        is the number of points.
    b : Tensor
        The second set of points in 3D space. Its shape is (M, 3), where M
        is the number of points.
    square : bool, optional
        The chamfer distances are square distances if True, and euclidean
        distances if False.

    Returns
    -------
    Tensor
        The chamfer distances between the two sets of points. Its shape is (N+M,).
    """
    # find the nearest neighbors between a and b
    ia = nearest_neighbor(a, b)
    ib = nearest_neighbor(b, a)
    # compute the distances between a and b[ia] and between b and a[ib]
    da = torch.sum((a - b[ia]) ** 2, dim=-1)
    db = torch.sum((b - a[ib]) ** 2, dim=-1)
    if not square:
        da = torch.sqrt(da)
        db = torch.sqrt(db)
    # concatenate the two sets of distances
    return torch.cat([da, db])


def compute_face_adjacency(faces):
    """
    Compute neighboring faces of a triangular mesh. It's best to precompute
    the face adjacency when possible instead of calling this on the fly.

    Parameters
    ----------
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.

    Returns
    -------
    adjacency : Tensor
        Tensor of shape (E, 2) representing the indices of the
        faces that form each edge.
    """
    edges = faces[:, [0, 1, 1, 2, 2, 0]].view((-1, 2))
    fa = torch.arange(faces.shape[0])
    edges_faces = torch.tile(fa, (3, 1)).T.reshape(-1)

    sorted_edges = edges.sort(dim=-1)[0]

    unq, inv = torch.unique(sorted_edges.T.flip(0), dim=-1, sorted=True, return_inverse=True)
    order = torch.argsort(inv)

    se = sorted_edges[order]
    ef = edges_faces[order]

    uniques = torch.diff(se, dim=0).abs().sum(1) == 0

    adjacency = torch.stack([ef[:-1][uniques], ef[1:][uniques]], dim=1)
    return adjacency


def hinge_distances(vertices, faces, face_adjacency, square=False):
    """
    Compute the hinge distances between neighboring triangles in a mesh. The
    hinge distance is the Euclidian distance between the normal vectors of two
    neighboring faces, which is a proxy for the size of the angle over an edge
    in the mesh.

    Parameters
    ----------
    vertices : Tensor
        The vertices of the mesh. Its shape is (V, 3), where V is the number
        of vertices.
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.
    face_adjacency : Tensor
        The adjacency information between neighboring faces. Its shape is (E, 2),
        where E is the number of unique edges.
    square : bool, optional
        The hinge distances are square distances if True, and euclidean
        distances if False.

    Returns
    -------
    Tensor
        The hinge distances between neighboring triangles in the mesh. Its shape
        is (E,).
    """
    triangles = vertices[faces]                  # [F, 3, 3]
    normals = compute_face_normals(triangles)    # [F, 3]
    edge_face_normals = normals[face_adjacency]  # [E, 2, 3]
    a = edge_face_normals[:, 0, :]               # [E, 3]
    b = edge_face_normals[:, 1, :]               # [E, 3]
    dist = torch.sum((a - b) ** 2, dim=-1)
    if not square:
        dist = torch.sqrt(dist)
    return dist


def find_component(mask, faces, random=False):
    """
    Find a single connected component in a binary mesh mask.

    This method essentially implements a flood fill algorithm, starting from a
    seed vertex and iteratively expanding the component within the mask until
    no more vertices can be added.

    This is an extremely inefficient algorithm if components are larger than a
    few hundred vertices.

    Parameters
    ----------
    mask : Tensor
        Tensor of shape (V,) representing the binary mask to find
        connected components in.
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.
    random : bool, optional
        Whether to choose a random seed vertex.

    Returns
    -------
    component : Tensor
        A boolean mask indicating the vertices that belong to the connected
        component.
    """
    # 
    nonzero = mask.nonzero()
    if len(nonzero) == 0:
        return None
    seed = tuple(nonzero[np.random.randint(len(nonzero))]) if random else tuple(nonzero[0])
    component = torch.zeros(mask.shape[0], dtype=torch.bool, device=mask.device)
    component[seed] = 1
    component_size = 1

    source = faces.reshape(-1)
    target = faces.roll(1, dims=-1).reshape(-1)

    zeros = torch.zeros(mask.shape[0], dtype=mask.dtype, device=mask.device)

    # hopefully this loop doesn't get anywhere near the total number of iterations
    for i in range(1e4):

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            for i in range(2):
                reduced = zeros.scatter_reduce(0, target, component[source], reduce='amax')
                component[mask] = reduced[mask]

        current_size = component.count_nonzero()
        if current_size == component_size:
            return component
        component_size = current_size

    # if we got this far, throw a warning
    warnings.warn('find_component function exceeded max iterations')
    return component


def mark_self_intersecting_faces(vertices, faces):
    """
    Mark vertices in a triangular mesh that intersect with themselves.

    Parameters
    ----------
    vertices : Tensor
        A tensor of shape (V, 3) containing the coordinates
        of the vertices in the mesh.
    faces : Tensor
        Tensor of shape (F, 3) representing mesh face indices.

    Returns
    -------
    Tensor
        A boolean tensor of shape (V,) indicating whether each vertex
        in the mesh intersects with itself.
    """
    vertices = vertices.detach()
    faces = faces.detach()

    if vertices.is_cuda: 
        marked_faces, _ = extension.mark_self_intersecting_faces_cuda(vertices, faces)
    else:
        mesh = sf.Mesh(vertices.numpy(), faces.numpy())
        marked_faces = mesh.find_self_intersecting_faces(overlay=True).data
        marked_faces = torch.tensor(marked_faces)

    return marked_faces[faces].any(1)
