import numpy as np
import surfa as sf
import torch


def compute_ds_shape(baseshape, levels, dmin=None, dmax=None):
    """
    Compute the smallest possible grid shape, no smaller than the input base shape,
    that can be cleanly downsampled to a particular number of resolution levels.

    Parameters
    ----------
    baseshape : tuple of int
        Shape of the base grid to extend. The computed downsampleable shape must be
        equal to or greater than this base shape.
    levels : int
        Maximum number of resolution levels in the downsampling pyramid. For example, one level
        corresponds to a single resolution, without downsampling. Two levels corresponds to a
        pyramid with only one downsampling step.
    dmin : int or tuple of int
        Minimum size of the computed shape. If tuple, the dimensionality must match baseshape.
    dmax : int or tuple of int
        Maximum size of the computed shape. If tuple, the dimensionality must match baseshape.

    Returns
    -------
    tuple of int
        Computed downsampleable shape.
    """
    ds_base = 2 ** (levels - 1)
    ds_factor = np.asarray(baseshape) / ds_base
    target_shape = np.ceil(ds_factor).astype(int) * ds_base

    if dmin is not None:
        target_shape = np.clip(target_shape, dmin, None)
    if dmax is not None:
        target_shape = np.clip(target_shape, None, dmax)

    return target_shape


def shape_normalize(
    image,
    levels,
    bbox=None,
    orientation=None,
    voxsize=None,
    dmin=None,
    dmax=None,
    copy=True):
    """
    Normalize an image to an appropriate shape that can be correctly passed through
    a model with multiple resolution levels. This can also be used to normalize the
    orientation of the image data as well as the voxel size.

    Parameters
    ----------
    image : Volume
        Image to normalize.
    levels : int
        Maximum number of resolution levels in the downsampling pyramid. For example, one level
        corresponds to a single resolution, without downsampling. Two levels corresponds to a
        pyramid with only one downsampling step.
    bbox : slicing, optional
        Bounding box that represents the pertinent region of the image. Any data
        outside this box could potentially be cropped during the shape normalization.
    orientation : str, optional
        Anatomical orientation to conform the data layout to.
    voxsize : int or tuple of int, optional
        Voxel size () to conform the image to.
    dmin : int or tuple of int
        Minimum size of the computed shape.
    dmax : int or tuple of int
        Maximum size of the computed shape.
    copy : bool, optional
        Return a copy of the volume even if no modifications need to be made.

    Returns
    -------
    Volume
        Normalized image.
    """
    original_image = image

    # TODO: could probably just build this correctly into the conform function
    if copy:
        image = image.copy()

    if orientation is not None:
        image = image.reorient(orientation, copy=False)

    if voxsize is not None:
        image = image.resize(voxsize, copy=False)

    if bbox is not None:
        if voxsize is not None or orientation is not None:
            vox2vox = image.geom.world2vox @ original_image.geom.vox2world
            bbox = sf.slicing.convert_slicing(bbox, image.baseshape, vox2vox)
        baseshape = sf.slicing.slicing_shape(bbox)
    else:
        baseshape = image.baseshape

    target_shape = compute_ds_shape(baseshape, levels, dmin, dmax)

    if bbox is not None:
        cropping = sf.slicing.fit_slicing_to_shape(bbox, image.baseshape, target_shape)
        image = image[cropping]

    return image.reshape(target_shape, copy=False)


def compute_quantile(arr, q):
    """
    Compute the quantile of a tensor.

    Parameters
    ----------
    arr : tensor
        Tensor to compute the quantile of.
    q : float
        Quantile to compute.

    Returns
    -------
    float
        Quantile value.
    """
    if q < 0 or q > 1:
        raise ValueError(f'quantile must be between 0 and 1, got {q}')
    if q == 0:
        return arr.min()
    if q == 1:
        return arr.max()
    arr = arr.flatten()
    if q > 0.5:
        k = int(arr.numel() * (1.0 - q)) + 1
        return arr.topk(k, largest=True, sorted=False).values.min()
    else:
        k = int(arr.numel() * q) + 1
        return arr.topk(k, largest=False, sorted=False).values.max()


def intensity_normalize(tensor, quantile=None, clip=True, copy=True):
    """
    Normalize the signal intensities of an image between zero and one.

    Parameters
    ----------
    tensor : tensor
        Image tensor to normalize.
    quantile : float, optional
        The quantile value used as the max value to scale the intensities by.
        If none (default), a min-max normalization will be used.
    clip : bool, optional
        Clip the intensity values between zero and one.
    dtype : str or np.dtype, optional
        Expected data type of the modified image.
    copy : bool, optional
        Return a copy of the tensor even if no modifications need to be made.

    Returns
    -------
    Volume
        Normalized image.
    """
    if copy:
        tensor = tensor.clone()

    tensor -= tensor.min()
    if quantile is not None:
        tensor /= compute_quantile(tensor, quantile)
        if clip:
            tensor.clamp_(0, 1)
    else:
        tensor /= tensor.max()

    return tensor


def framed_array_to_tensor(array, dtype=torch.float32, device=None):
    """
    Utility for converting a surfa Volume to a torch tensor with a channel
    axis represented by the first dimension.

    Parameters
    ----------
    array : Volume
        Surface framed array to convert to a torch tensor.
    dtype : torch.dtype, optional
        Expected torch data type of the modified image.
    device : str or torch.device, optional
        Device to place the tensor on.

    Returns
    -------
    Tensor
        Tensor with shape (channels, width, height, depth).
    """
    # check if data has correct native byte order and switch if necessary
    framed_data = array.framed_data
    if framed_data.dtype.byteorder not in ('=', '|'):
        framed_data = framed_data.byteswap().newbyteorder()
    # TODO: the copy is to avoid negative strides, but this is not ideal
    return torch.tensor(framed_data.copy(), dtype=dtype, device=device).moveaxis(-1, 0)
