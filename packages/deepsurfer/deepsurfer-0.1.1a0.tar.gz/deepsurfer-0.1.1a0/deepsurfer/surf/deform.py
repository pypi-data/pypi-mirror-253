import torch

from .conv import EdgeUNet
from .mesh import compute_vertex_normals
from .mesh import sample_grid


class GraphDeformationBlock(torch.nn.Module):

    def __init__(
        self,
        channels,
        in_channels,
        topology_collection=None,
        resolution=None,
        scale=None,
        steps=1,
        activation=None,
        include_positions=True,
        ):
        """
        Graph-based deformation network that uses a edge-convolutional UNet to estimate and apply
        a set of deformation vectors for each vertex in the mesh. The input features are extracted
        from the image space using trilinear interpolation and concatenated with position and normal
        for each vertex.

        Parameters
        ----------
        channels : tuple
            Tuple containing the number of channels for each level of the encoder and decoder.
        in_channels : int
            Number of channels for the input data.
        topology_collection : TopologyCollection, optional
            The collection of mesh topologies that defines the UNet down and upsampling structure.
        resolution : int, optional
            The top resolution level of the mesh topology collection.
        scale : float, optional
            The scale factor for the deformation vectors.
        steps : int, optional
            Number of deformation steps to apply.
        activation : callable, optional
            Activation for each convolution in the edge unet, except for the last. If None, then
            defaults to Leaky-ReLU with slope of 0.3.
        include_positions: bool, optional
            Whether to include vertex positions as an additional input feature.
        """
        super().__init__()
        self.scale = scale
        self.include_positions = include_positions
        self.topology_collection = topology_collection
        self.resolution = resolution
        self.steps = steps

        # is a static topology collection is provided then we can pre-initialize some tensors,
        # which probably saves minimal time in the end
        if topology_collection is not None:
            if self.resolution is None:
                self.resolution = len(topology_collection) - 1
            self.topology = topology_collection[self.resolution]
            # cache a set of zeros on the device for computing normals
            zeros = torch.zeros((self.topology.nv, 3), dtype=torch.float32)
            self.register_buffer('zeros', zeros, persistent=False)
        else:
            self.topology = None

        # add the normal and position features if needed
        if self.include_positions:
            in_channels += 3

        # default activation
        if activation is None:
            activation = torch.nn.LeakyReLU(0.3)

        # initialize a edge-convolution unet with multiple resolution
        # levels to convert sampled features into mesh deformation vectors
        self.edgenet = EdgeUNet(channels=channels,
                                in_channels=in_channels,
                                activation=activation,
                                initial_resolution=self.resolution,
                                topology_collection=topology_collection)

        # add a final convolution to estimate the deformation vectors
        self.edgenet.add_convolution(3)

    def forward(self, image_features, vertices, topology_collection=None, resolution=None, image_shape=None):
        """
        Foward pass through the deformation network.

        Parameters
        ----------
        image_features : Tensor
            Image features to sample with shape (C, W, H, D).
        vertices : Tensor
            Mesh vertices with shape (V, 3).
        topology_collection : TopologyCollection, optional
            The collection of mesh topologies that defines the UNet down and upsampling structure. If this parameter
            was provided during initialization, and the mesh topology has not changed, then it does not need to be set.
        resolution : int, optional
            The initial resolution level. If this parameter was provided during initialization, and the mesh topology
            has not changed, then it does not need to be set.
        image_shape : Tensor, optional
            The shape of the image features. If this parameter was provided during initialization, it will be computed
            on the fly.

        Returns
        -------
        Tensor
            Deformed mesh vertices with shape (V, 3).
        """

        # if no topology collection was provided at initialization, then we should precompute a 
        # zeros tensor for computing vertex normals
        if self.topology_collection is None:
            res = len(topology_collection) - 1 if resolution is None else resolution
            zeros = torch.zeros((topology[res].nv, 3), dtype=torch.float32, device=image_features.device)
        else:
            zeros = self.zeros

        # iterate over deformation steps for this block
        for step in range(self.steps):

            # TODO: should the applied gradient somehow be scaled by the number of steps?

            # get the image shape
            if image_shape is None:
                image_shape = torch.tensor(image_features.shape[1:], dtype=torch.int64, device=image_features.device)

            # sample mesh features from the image space
            features = sample_grid(image_features, vertices, image_shape)

            # add the normal and position features if needed
            added_features = []

            if self.include_positions:
                # normalize the vertex positions between 0 and 1
                normalized_positions = vertices / image_shape.max()
                added_features.append(normalized_positions)

            # merge these features
            if len(added_features) > 0:
                features = torch.cat([*added_features, features], dim=-1)

            # estimate the deformation vectors
            deformation = self.edgenet(features, topology_collection, resolution)

            # scale the predicted deformation vectors
            if self.scale is not None:
                deformation = deformation * self.scale

            # apply the deformation
            vertices = vertices + deformation

        return vertices


class QuadDeformationBlock(torch.nn.Module):

    def __init__(
        self,
        channels,
        in_channels,
        iterations,
        activation=None):
        """
        Image-based deformation network that uses a set of dense layers to estimate and apply
        a set of vertex deformations. Features are sampled from the image space using trilinear
        interpolation at each vertex position. A deformation is predicted by the dense layers for
        each vertex and applied using an interative quadrature update to encourage a near-diffeomorphic
        deformation.

        Parameters
        ----------
        channels : list of int
            Number of channels for each dense layers.
        in_channels : int
            Number of channels in the input image data.
        iterations : int
            Number of iterations to use for the quadrature update.
        activation : callable, optional
            Activation for each dense layer, except the last. If None, then defaults to
            Leaky-ReLU with slope of 0.3.
        """
        super().__init__()
        self.iterations = iterations
        self.scale = 1.0 / iterations

        # default activation
        if activation is None:
            activation = torch.nn.LeakyReLU(0.3)

        # this network is pretty simple - just a set of dense layers
        # that convert sampled features to a deformation vector
        last = in_channels
        self.layers = torch.nn.ModuleList()
        for c in channels:
            self.layers.append(torch.nn.Linear(last, c))
            self.layers.append(activation)
            last = c

        # final layer to predict deformation vector
        self.layers.append(torch.nn.Linear(last, 3))

    def forward(self, image_features, vertices, image_shape=None):
        """
        Foward pass through the deformation network.

        Parameters
        ----------
        image_features : Tensor
            Image features to sample with shape (C, W, H, D).
        vertices : Tensor
            Mesh vertices with shape (V, 3).
        image_shape : Tensor, optional
            The shape of the image features. If this parameter was provided during initialization, it will be computed
            on the fly.

        Returns
        -------
        Tensor
            Deformed mesh vertices with shape (V, 3).
        """
        # get the image shape
        if image_shape is None:
            image_shape = torch.tensor(image_features.shape[1:], dtype=torch.int64, device=image_features.device)

        for i in range(self.iterations):
            # predict and apply the deformation
            features = sample_grid(image_features, vertices, image_shape)
            for layer in self.layers:
                features = layer(features)
            vertices = vertices + self.scale * features

        return vertices
