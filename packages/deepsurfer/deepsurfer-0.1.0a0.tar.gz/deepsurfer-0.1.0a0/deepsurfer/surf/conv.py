import warnings
import torch


class EdgeConv(torch.nn.Module):

    def __init__(
        self,
        in_channels,
        out_channels,
        num_vertices=None,
        activation=None,
        bias=True):
        """
        Edge convolutional layer that computes a vertex feature as a function of the vertex neighborhood.
        See: Dynamic Graph CNN for Learning on Point Clouds (https://arxiv.org/abs/1801.07829)

        Parameters
        ----------
        in_channels : int
            Number of channels in the input vertex features.
        out_channels : int
            Number of channels in the output vertex features.
        num_vertices : int, optional
            Number of vertices in the topology. If None, then the number of vertices is inferred
            dynamically from the input features in the forward pass.
        activation : callable, optional
            Activation function for the convolutional layer.
        bias : bool, optional
            Whether to use a bias term in the convolution.
        """
        super().__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.activation = activation

        # initialize the vertex feature buffer (might only provide a minimal speedup)
        self.num_vertices = num_vertices
        if num_vertices is not None:
            self.register_buffer('zeros', torch.zeros((num_vertices, self.out_channels)), persistent=False)

        # initialize the convolution
        self.conv1d = torch.nn.Conv1d(
            in_channels=in_channels * 2,
            out_channels=out_channels,
            kernel_size=1,
            stride=1,
            padding='valid',
            bias=bias)

    def forward(self, features, topology):
        """
        Forward pass through the edge convolution.

        Parameters
        ----------
        features : torch.Tensor
            The input vertex features of shape `(V, C)`.
        topology : Topology
            The topology of the mesh graph.

        Returns
        -------
        Tensor
            The predicted vertex features.
        """

        # initialize zeros, unless already intialized
        if self.num_vertices is None:
            zeros = torch.zeros((topology.num_vertices, self.out_channels), device=features.device)
        elif self.num_vertices != topology.nv:
            raise ValueError(f'invalid number of vertices: {topology.num_vertices} (expected {self.num_vertices})')
        else:
            zeros = self.zeros

        # extract features in each vertex neighborhood
        neighbors = features[topology.neighborhood_source]
        local = features[topology.neighborhood_target]
        x = torch.cat([local, neighbors - local], -1)

        # pass features through convolution
        x = x.swapaxes(-2, -1).unsqueeze(0)
        y = self.conv1d(x).squeeze(0).swapaxes(-2, -1)

        # gather edge features from each vertex neighborhood
        indices = topology.neighborhood_target.view(-1, 1).expand(-1, y.shape[-1])
        with warnings.catch_warnings():
            # scatter_reduce is an experimental torch feature, so we suppress the warning
            warnings.simplefilter('ignore')
            reduced = zeros.to(y.dtype).scatter_reduce(-2, indices, y, reduce='mean', include_self=False)

        # activate
        if self.activation is not None:
            reduced = self.activation(reduced)
        return reduced


class EdgeUNet(torch.nn.Module):

    def __init__(
        self,
        channels,
        in_channels,
        pooling_mode='max',
        initial_resolution=None,
        topology_collection=None,
        **kwargs,
        ):
        """
        Edge-convolutional UNet architecture that computes vertex features as a function of vertex neighborhoods.

        Note if you find this code useful, please cite:

        Hoopes et al. "TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces"
        Medical Imaging with Deep Learning. 2022.

        Parameters
        ----------
        channels : tuple
            Tuple containing the number of channels for each level of the encoder and decoder.
        in_channels : int
            Number of channels for the input data.
        pooling_mode : str, optional
            Type of pooling used in the encoder, either 'max' or 'avg'. Default is 'max'.
        initial_resolution : int, optional
            The top resolution level of the mesh topology collection. Default is the maximum resolution
            in the topology collection.
        topology_collection : TopologyCollection, optional
            The collection of mesh topologies that defines the UNet down and upsampling structure. If the mesh
            topologies do not change, then this parameter can be provided to cache tensors and avoid
            needing to provide them during each forward pass. A (minimal) speedup can be achieved by doing this.
        activation : callable, optional
            Activation to apply after each convolutional layer. If not provided, default is Leaky ReLU with slope 0.3.
        """
        super().__init__()

        # initialize parameters
        self.cached_topology_collection = topology_collection
        self.pooling_mode = pooling_mode

        # get the initial resolution level
        if initial_resolution is None and topology_collection is not None:
            initial_resolution = len(topology_collection) - 1
        self.initial_resolution = initial_resolution

        # split apart encoder and decoder from channels
        encoder_channels, decoder_channels = channels
        self.num_levels = len(encoder_channels)

        # crop the number of the levels if it exceeds the number of levels in the topology collection
        if self.initial_resolution is not None and self.initial_resolution + 1 < self.num_levels:
            raise ValueError(f'number of levels in the unet ({self.num_levels}) exceeds the number of levels available '
                             f'in the topology collection, starting at res level ({self.initial_resolution})')

        # convert channel lists into list of lists (per level)
        makelist = lambda x: x if isinstance(x, list) else [x]
        encoder_channels = [makelist(c) for c in encoder_channels]
        split = self.num_levels - 1
        upsampling = [makelist(c) for c in decoder_channels[:split]]
        decoder_channels = upsampling + makelist(decoder_channels[split:])

        if len(decoder_channels) == (self.num_levels - 2):
            decoder_channels.append([])
        elif len(decoder_channels) != (self.num_levels - 1):
            raise ValueError('number of decoder levels must be 1 or 2 less than the '
                             'number of encoder levels, got:\n\n'
                            f'encoder: {encoder_channels}\n'
                            f'decoder: {decoder_channels}')

        # default activation
        activation = kwargs.pop('activation', torch.nn.LeakyReLU(0.3))

        # check if there are any leftover parameters
        if len(kwargs) > 0:
            param = list(kwargs.keys())[0]
            raise TypeError(f' __init__ got an unexpected keyword argument \'{param}\'')

        # configure encoder convolutions
        self.final_channels = in_channels
        res = self.initial_resolution
        channel_history = [self.final_channels]
        self.encoder = torch.nn.ModuleList()
        for i, level in enumerate(encoder_channels):
            blocks = torch.nn.ModuleList()
            for n in level:
                blocks.append(EdgeConv(self.final_channels, n, self.get_num_vertices(res), activation=activation))
                self.final_channels = n
            self.encoder.append(blocks)
            if i < (self.num_levels - 1):
                # decrease resolution for pooling
                channel_history.append(self.final_channels)
                res -= 1
                if topology_collection is not None:
                    # cache zeros tensor for pooling if static topology collection is provided
                    shape = (topology_collection[res].nv, self.final_channels)  # AH: note self.final_channels might be the wrong thing here
                    device = self.encoder[0][0].conv1d.weight.device
                    zeros = torch.zeros(shape, dtype=torch.float32)
                    self.register_buffer(f'pooling_zeros_{res}', zeros, persistent=False)

        # configure decoder convolutions
        self.decoder = torch.nn.ModuleList()
        for i, level in enumerate(decoder_channels):
            self.final_channels += channel_history.pop()
            blocks = torch.nn.ModuleList()
            res += 1
            for n in level:
                blocks.append(EdgeConv(self.final_channels, n, self.get_num_vertices(res), activation=activation))
                self.final_channels = n
            self.decoder.append(blocks)

        # option to add extra convolutions
        self.extra = torch.nn.ModuleList()

        # cache final resolution
        self.final_resolution = res

    def add_convolution(self, channels, activation=None):
        """
        Append a convolutional layer to the end of the decoder.

        Parameters
        ----------
        channels : int
            Number of output channels for the convolutional layer.
        activation : callable, optional
            Activation function to use after the convolution. Default is None (linear).
        """
        nv = self.get_num_vertices(self.final_resolution)
        self.extra.append(EdgeConv(self.final_channels, channels, nv, activation=activation))
        self.final_channels = channels

    def get_num_vertices(self, resolution):
        """
        Return the number of vertices at a given resolution level. This is only available if the
        topology collection was provided during initialization.

        Parameters
        ----------
        resolution : int
            The resolution level.

        Returns
        -------
        int or None
            The number of vertices at the given resolution level. Returns None if the topology collection
            was not provided during initialization.
        """
        if self.cached_topology_collection is None:
            return None
        return self.cached_topology_collection[resolution].nv

    def _zeros(self, level, num_vertices, channels):
        """
        Return a tensor of zeros with the given number of vertices and features. If the topology
        collection was provided during initialization, then this method will return a cached tensor. If
        not, then the tensor will be created on the same device as the first convolutional layer.

        Parameters
        ----------
        level : int
            The resolution level.
        num_vertices : int
            The number of vertices.
        channels : int
            The number of channels per vertex.

        Returns
        -------
        Tensor
            A tensor of zeros with the given number of vertices and channels.
        """
        if self.cached_topology_collection is None:
            device = self.ds_arm[0][0].conv1d.weight.device
            return torch.zeros((num_vertices, features), dtype=torch.float32, device=device)
        return self.get_buffer(f'pooling_zeros_{level}')

    def forward(self, features, topology_collection=None, initial_resolution=None):
        """
        Forward pass of the edge UNet.

        Parameters
        ----------
        features : Tensor
            The input vertex features of shape `(V, C)`.
        topology_collection : TopologyCollection, optional
            The collection of mesh topologies that defines the UNet down and upsampling structure. If this parameter
            was provided during initialization, and the mesh topology has not changed, then it does not need to be set.
        initial_resolution : int, optional
            The initial resolution level. If this parameter was provided during initialization, and the mesh topology
            has not changed, then it does not need to be set.

        Returns
        -------
        Tensor
            Predicted vertex features.
        """
        if topology_collection is None:
            if self.cached_topology_collection is None:
                raise ValueError('no topology collection provided and no cached topology collection found')
            topology_collection = self.cached_topology_collection
            initial_resolution = self.initial_resolution
        elif initial_resolution is None:
            initial_resolution = len(topology_collection) - 1

        # encoder forward pass
        history = []
        res = int(initial_resolution)
        for i, convs in enumerate(self.encoder):
            for conv in convs:
                features = conv(features, topology_collection[res])
            # no pooling on the last level
            if i < (self.num_levels - 1):
                res -= 1
                history.append(features)
                zeros = self._zeros(res, topology_collection[res].nv, features.shape[-1])
                features = topology_collection[res].pool(features, zeros=zeros, reduce=self.pooling_mode)

        # decoder forward pass with upsampling and concatenation
        for i, convs in enumerate(self.decoder):
            features = topology_collection[res].unpool(features)
            features = torch.cat([features, history.pop()], dim=-1)
            res += 1
            for conv in convs:
                features = conv(features, topology_collection[res])

        # extra convolutions
        for conv in self.extra:
            features = conv(features, topology_collection[res])

        return features
