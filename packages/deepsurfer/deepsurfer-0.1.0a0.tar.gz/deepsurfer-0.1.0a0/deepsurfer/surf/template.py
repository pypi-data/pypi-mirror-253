import warnings
import numpy as np
import torch


class TemplateMeshTopology:

    def __init__(self, nv, faces, unique_edges, face_adjacency=None):
        """
        A cache for mesh topological properties.

        Parameters
        ----------
        nv : int
            The number of vertices V in the mesh.
        faces : Tensor
            Vertex indices representing each mesh triangle. The expected shape
            is (F, 3), where F is the number of faces.
        unique_edges : Tensor
            Vertex indices representing each unique edge in the mesh. The expected
            shape is (E, 2), where E is the number of unique edges.
        face_adjacency : Tensor, optional
            Face indices representing each unique set of neighboring faces. The
            expected shape is (E, 2).
        """
        convert = lambda x: x if isinstance(x, torch.Tensor) else torch.tensor(x).type(torch.int64)

        self.nv = int(nv)
        self.faces = convert(faces)
        self.unique_edges = convert(unique_edges)

        if face_adjacency is not None:
            self.face_adjacency = convert(face_adjacency)

        self.neighborhood_source = torch.cat([self.unique_edges[:, 1], self.unique_edges[:, 0]])
        self.neighborhood_target = torch.cat([self.unique_edges[:, 0], self.unique_edges[:, 1]])

        self.pooling_target = torch.cat([torch.arange(self.nv),
                                         self.unique_edges[:, 0],
                                         self.unique_edges[:, 1]])

        new = torch.arange(unique_edges.shape[0]) + self.nv
        self.pooling_source = torch.cat([torch.arange(self.nv), new, new])
        self.pooling_source_size = self.nv + unique_edges.shape[0]

    def to(self, device):
        """
        Moves all tensor variables to the specified device.

        Parameters
        ----------
        device : str or torch.device
            The target device.

        Returns
        -------
        TemplateMeshTopology
            A pointer to the updated instance.
        """
        for name in vars(self):
            member = getattr(self, name)
            if isinstance(member, torch.Tensor):
                setattr(self, name, member.to(device))
        return self

    def upsample(self, vertices):
        """
        Upsample mesh vertex positions to the next mesh resolution level.

        Parameters
        ----------
        vertices : Tensor
            The vertices of the mesh. The expected shape is (V, 3).

        Returns
        -------
        Tensor
            Tensor representing the vertices of the upsampled mesh.
        """
        if vertices.shape[0] == self.pooling_source_size:
            return vertices
        if vertices.shape[0] != self.nv:
            raise ValueError(f'Vertices shape {vertices.shape} is not compatible '
                             f'with the mesh topology, which expects {self.nv} vertices.')
        return torch.cat([vertices, vertices[self.unique_edges].mean(-2)], dim=-2)

    def pool(self, features, zeros=None, reduce='max'):
        """
        Pool mesh features down to the next sparser resolution.

        Parameters
        ----------
        features : Tensor
            The mesh features. The expected shape is (V, C), where C is the number
            of feature channels.
        zeros : Tensor, optional
            A buffer of zeros to initialize with when reducing the features. If None,
            then allocated on the fly.
        reduce : str, optional
            The method to use for reducing the features. Must be 'max', 'min', or 'mean'.

        Returns
        -------
        Tensor
            The pooled features.
        """
        if features.shape[-2] != self.pooling_source_size:
            raise ValueError(f'Vertex features shape {vertices.shape} is not compatible '
                              'with the mesh topology, which expects pooling features with '
                             f'{self.pooling_source_size} vertices.')

        if zeros is None:
            zeros = torch.zeros((self.nv, features.shape[-1]), dtype=features.dtype, device=features.device)
        elif zeros.shape != (self.nv, features.shape[-1]):
            raise ValueError(f'Incorrect shape for zeros buffer, expected {(self.nv, features.shape[-1])} '
                             f'but got {zeros.shape}.')
        
        if reduce in ('max', 'amax'):
            reduce = 'amax'
        elif reduce in ('min', 'amin'):
            reduce = 'amin'
        elif reduce in ('mean', 'avg'):
            reduce = 'mean'
        else:
            raise ValueError(f'unknown pooling reduce type \'{reduce}\'')
        
        gathered = features[self.pooling_source]
        indices = self.pooling_target.view(-1, 1).expand(-1, gathered.shape[-1])

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            reduced = zeros.to(gathered.dtype).scatter_reduce(-2, indices, gathered, reduce=reduce, include_self=False)
        return reduced

    def unpool(self, features, reduce='max'):
        """
        Unpool mesh features to the next highest mesh resolution.

        Parameters
        ----------
        features : Tensor
            The mesh features. The expected shape is (V, C), where C is the number
            of feature channels.
        reduce : str, optional
            The method to use for reducing the features. Must be 'max', 'min', or 'mean'.

        Returns
        -------
        Tensor
            The (un)-pooled features.
        """
        sampled = features[self.unique_edges]
        if reduce in ('max', 'amax'):
            reduced = sampled.amax(-2)
        elif reduce in ('min', 'amin'):
            reduced = sampled.amin(-2)
        elif reduce == 'mean':
            reduced = sampled.mean(-2)
        else:
            raise ValueError(f'Unknown reduction type \'{reduce}\'')
        return torch.cat([features, reduced])


def load_topology_collection(filename, device=None):
    """
    Loads a collection of TemplateMeshTopology instances from a compressed npz file.
    The returned value is a list of topologies, where each index represents the
    mesh resolution level.

    Parameters
    ----------
    filename : str
        The name of the file containing the topologies.
    device : str or torch.device, optional
        The target device.

    Returns
    -------
    TemplateMeshTopology list
        A list of TemplateMeshTopology objects containing the topologies loaded from
        the file.
    """
    npz = np.load(filename)
    collection = []
    for i in range(npz['num-resolutions']):
        nv = npz[f'res-{i}-nvertices']
        faces = npz[f'res-{i}-faces']
        unique_edges = npz[f'res-{i}-unique-edges']
        face_adjacency = npz[f'res-{i}-face-adjacency']
        topology = TemplateMeshTopology(nv, faces, unique_edges, face_adjacency)
        if device is not None:
            topology = topology.to(device)
        collection.append(topology)
    return collection
