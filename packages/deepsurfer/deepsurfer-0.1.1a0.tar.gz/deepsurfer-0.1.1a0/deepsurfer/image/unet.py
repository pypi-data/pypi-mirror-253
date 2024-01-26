import numpy as np
import torch


def make_channel_lists(
    num_levels,
    base_channels,
    convs_per_level=1,
    multiplier=2,
    max_channels=None,
    min_dec_channels=None):
    """
    Helper to create a list of channels for the encoder and decoder of the UNet.

    Parameters
    ----------
    num_levels : int
        Number of levels in the UNet.
    base_channels : int
        Number of channels in the lowest level of the UNet.
    convs_per_level : int, optional
        Number of convolutions per level of the UNet.
    multiplier : int, optional
        The multiplier for the number of channels at each level of the UNet.
    max_channels : int, optional
        Maximum number of channels in the UNet. If None, then there is no maximum.
    min_dec_channels : int, optional
        Minimum number of channels in the decoder part of the UNet. If None, then
        there is no minimum.

    Returns
    -------
    channels : list
        List of lists containing the number of channels for each level of the encoder and decoder.
    """
    if max_channels is None:
        max_channels = base_channels * multiplier ** (num_levels - 1)
    if min_dec_channels is None:
        min_dec_channels = base_channels
    channels = lambda i : min(max_channels, base_channels * multiplier ** i)
    encoder = [[channels(i)] * convs_per_level for i in range(num_levels)]
    channels = lambda i : min(max_channels, max(min_dec_channels, base_channels * multiplier ** (num_levels - i - 2)))
    decoder = [[channels(i)] * convs_per_level for i in range(num_levels - 1)]
    return [encoder, decoder]


class UNet(torch.nn.Module):
    """
    Image UNet architecture.

    Parameters
    ----------
    ndim : int
        Dimensionality of the input data. 2 for images and 3 for volumes.
    channels : tuple
        Tuple containing the number of channels for each level of the encoder and decoder.
    in_channels : int, optional
        Number of channels for the input data. Default is 1.
    pooling_size : int, optional
        Size of the pooling kernel used in the encoder. Default is 2.
    pooling_mode : str, optional
        Type of pooling used in the encoder, either 'max' or 'avg'. Default is 'max'.
    activation : callable, optional
        Activation to apply after each convolution. Default is Leaky-ReLU with slope of 0.2.

    Attributes
    ----------
    num_levels : int
        Total number of levels in the UNet.
    final_channels : int
        Number of channels of the last convolutional layer in the UNet.
    encoder : torch.nn.ModuleList
        List of convolutional blocks in the encoder part of the UNet.
    decoder : torch.nn.ModuleList
        List of convolutional blocks in the decoder part of the UNet.
    """
    def __init__(self,
                 ndim,
                 channels,
                 in_channels=1,
                 pooling_size=2,
                 pooling_mode='max',
                 **kwargs):

        super().__init__()

        # dimensionality
        self.ndim = ndim

        # split apart encoder and decoder from channels
        encoder_channels, decoder_channels = channels
        self.num_levels = len(encoder_channels)
        self.in_channels = in_channels

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
        activation = kwargs.pop('activation', torch.nn.LeakyReLU(0.2))

        # check if there are any leftover parameters
        if len(kwargs) > 0:
            param = list(kwargs.keys())[0]
            raise TypeError(f' __init__ got an unexpected keyword argument \'{param}\'')

        # cache downsampling / upsampling operations
        if pooling_mode == 'max':
            mode = 'Max'
        elif pooling_mode in ('avg', 'mean'):
            mode = 'Avg'
        else:
            raise ValueError(f'unknown pooling mode \'{pooling_mode}\'')
        Pooling = getattr(torch.nn, f'{mode}Pool{ndim}d')
        self.pooling = Pooling(pooling_size)
        self.upsampling = torch.nn.Upsample(scale_factor=pooling_size, mode='nearest')

        # configure encoder convolutions
        self.final_channels = in_channels
        channel_history = [self.final_channels]
        self.encoder = torch.nn.ModuleList()
        for i, level in enumerate(encoder_channels):
            blocks = torch.nn.ModuleList()
            for n in level:
                blocks.append(ConvBlock(ndim, self.final_channels, n, activation=activation))
                self.final_channels = n
            self.encoder.append(blocks)
            if i < (self.num_levels - 1):
                channel_history.append(self.final_channels)

        # configure decoder convolutions
        self.decoder = torch.nn.ModuleList()
        for i, level in enumerate(decoder_channels):
            self.final_channels += channel_history.pop()
            blocks = torch.nn.ModuleList()
            for n in level:
                blocks.append(ConvBlock(ndim, self.final_channels, n, activation=activation))
                self.final_channels = n
            self.decoder.append(blocks)

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
        self.decoder[-1].append(ConvBlock(self.ndim, self.final_channels, channels, activation=activation))
        self.final_channels = channels

    def forward(self, features):
        """
        Foward pass through the unet.

        Parameters
        ----------
        features : tensor
            Input tensor of shape (batch, channels, width, height) for 2D or
            (batch, channels, width, height, depth) for 3D.

        Returns
        -------
        Tensor
            Predicted image features.
        """
        if features.shape[1] != self.in_channels:
            raise ValueError(f'unet expected input features with {self.in_channels} '
                             f'channels, but got {features.shape[1]}')
        if features.ndim != self.ndim + 2:
            raise ValueError(f'unet expected input with {self.ndim + 2} dimensions, '
                             f'but got shape {features.shape}')

        # encoder forward pass
        history = []
        for i, convs in enumerate(self.encoder):
            for conv in convs:
                features = conv(features)
            # no pooling on the last level
            if i < (self.num_levels - 1):
                history.append(features)
                features = self.pooling(features)

        # decoder forward pass with upsampling and concatenation
        for i, convs in enumerate(self.decoder):
            features = self.upsampling(features)
            features = torch.cat([features, history.pop()], dim=1)
            for conv in convs:
                features = conv(features)

        return features


class ConvBlock(torch.nn.Module):
    """
    Convolutional block utility with activation function.

    Parameters
    ----------
    ndim : int
        The dimensionality of the convolution. Must be 1, 2, or 3.
    in_channels : int
        The number of input channels.
    out_channels : int
        The number of output channels.
    kernel : int or tuple of ints, optional
        The size of the convolutional kernel.
    stride : int or tuple of ints, optional
        The stride of the convolution.
    activation : callable, optional
        The activation function to use. Default is None.
    """
    def __init__(self, ndim, in_channels, out_channels, kernel=3, stride=1, activation=None):
        super().__init__()
        Conv = getattr(torch.nn, f'Conv{ndim}d')
        self.conv = Conv(in_channels, out_channels, kernel, stride, 1)
        self.activation = activation

    def forward(self, features):
        """
        Forward pass of the convolution.

        Parameters
        ----------
        features : torch.Tensor
            The batched input features.

        Returns
        -------
        torch.Tensor
            The predicted output features.
        """
        features = self.conv(features)
        if self.activation is not None:
            features = self.activation(features)
        return features
