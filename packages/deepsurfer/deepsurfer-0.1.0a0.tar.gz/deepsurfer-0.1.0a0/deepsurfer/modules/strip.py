import numpy as np
import surfa as sf
import torch
import deepsurfer as ds

from deepsurfer.modules.braincrop import load_brain_cropping_model


class StripModel(ds.io.LoadableModule):

    @ds.io.store_config_args
    def __init__(self,
                 channels=[
                    [16, 32, 64, 64, 64, 64, 64],
                    [64, 64, 64, 64, 32, 16]
                 ],
                 in_voxsize=1,
                 in_orientation='LIA',
                 use_sdt=True,
                 max_border=4):
        """
        A model for brain extraction that can be used to estimate a binary brain mask from an
        single input image. It's a fairly straightfoward model architecture that uses a U-Net to
        predict either a signed distance transform (SDT) representing brain matter or a probabilistic
        segmentation map. In the original SynthStrip paper, the model was trained with the SDT
        configuration, which tended to increase smoothness of the mask along the brain boundary.
        However, just predicted probabilistic labels is fine too, and might be better for predicted
        multiple classes of relevant matter simultaneously, i.e. CSF, dura, vessels, and brain.
        """
        super().__init__()

        # this is useful to have cached at inference time
        # important that the model was actually trained with this resolution!
        self.in_voxsize = in_voxsize
        self.in_orientation = in_orientation

        # model architectural settings
        self.use_sdt = use_sdt
        self.max_border = max_border

        # simple unet
        self.unet = ds.image.UNet(ndim=3, channels=channels)

        if self.use_sdt:
            # if using the SDT loss, we need to output a single distance channel
            self.unet.add_convolution(1, activation=None)
        else:
            # if using the dice-based configuration, output three segmentation channels,
            # one for non-brain, one for brain, and one for CSF and dura
            self.unet.add_convolution(3, activation=torch.nn.Softmax(dim=-4))

    def forward(self, image):
        """
        Straight-forward forward pass that calls the underlying unet. Expects the input to be
        batched with shape (B, 1, W, H, D).

        Note that this function is meant to be used under-the-hood and will only return the
        predicted feature map. To predict a complete skull-strip given an input image, use the
        estimate() method.

        Parameters
        ----------
        image : Tensor
            The input image of shape (B, 1, W, H, D) to compute features from.

        Returns
        -------
        Tensor
            The predicted features of shape (B, C, W, H, D) where C is either
            1 for SDT-estimating models or 3 for label-estimating models.
        """
        if image.ndim != 5:
            raise ValueError('expected 5-dimensional batched input of shape (B, 1, W, H, D), '
                            f'but got input with shape {image.shape}')
        return self.unet(image)

    def estimate(self, image, bbox=None, border=1, quantile=0.999, debug=False):
        """
        Compute a brain matter mask.

        Parameters
        ----------
        image : sf.Volume
            The input image volume to align the template to.
        bbox : slicing, optional
            A bounding box around pertinent anatomy in the input image. This is used to crop
            the inputs to the model, speeding up the estimation substantially.
        border : int, optional
            The border distance to use for the signed distance transform. This is only used
            if the model was trained with the SDT loss function.
        quantile : float
            The image intensity quantile used as the max value for normalization
            during pre-processing. If None, the max intensity across the entire image
            is used.
        debug : bool, optional
            Show model debugging information and visualizations. Requires that the freeview
            visualization command is available on the system.

        Returns
        -------
        mask : sf.Volume
            A binary mask of brain matter in the input image space.
        """
        if image.nframes > 1:
            ds.system.fatal(f'Input image has {image.nframes} frames, but expected only 1')

        if self.use_sdt and border > self.max_border:
            ds.system.fatal(f'Brain extraction border distance cannot be greater than {self.max_border} mm')

        # conform the input image to the model voxel size. the network should be trained to be
        # orientation-agnostic so no need to worry about reorienting
        conformed = ds.normalize.shape_normalize(image,
                                                 levels=self.unet.num_levels,
                                                 bbox=bbox,
                                                 orientation=self.in_orientation,
                                                 voxsize=self.in_voxsize)

        # cache the current model mode so we can reset after it inference is done
        mode = self.training
        self.train(mode=False)
        with torch.no_grad():

            # turn our inputs into tensors and move to the right device
            I = ds.normalize.framed_array_to_tensor(conformed, device=self.device)
            I = ds.normalize.intensity_normalize(I, quantile=quantile, copy=False)
            
            # predict the feature map and convert tensor back to a surfa volume
            pred = self(I.unsqueeze(0)).squeeze()

            if self.use_sdt:
                # unconform the sdt and extract mask (use arbitrarily large fill of 100
                # to avoid edge effects when resampling back to target space)
                pred = pred.cpu().numpy()
                sdt = conformed.new(pred).resample_like(image, fill=100)
                # find largest CC (just do this to be safe for now)
                mask = (sdt < border).connected_component_mask(fill=True)
            else:
                # collapse the labels into a discrete segmentation
                pred = pred.argmax(dim=-4).cpu().numpy()
                mask = conformed.new(pred).resample_like(image, method='nearest') > 0

            # visualize
            if debug:
                fv = sf.vis.Freeview(title='Skull-Strip Debugging')
                fv.add_image(image, name='Raw Input Image')
                fv.add_image(conformed, name='Conformed Model Input')
                fv.add_image(pred, name='SDT' if self.use_sdt else 'Predicted Segmentation')
                fv.add_image(mask, name='Computed Mask', colormap='heat')
                fv.show(background=False)

        # reset to the previous training/evaluation state
        self.train(mode=mode)

        return image.new(mask)


"""
TODO: the training code for this model still needs to be updated to work with the new refactoring
of the framework, so it's been excluded from the package for now.
"""


def load_strip_model(device, version=1, modelfile=None, verbose=False):
    """
    Load the default skull-stripping model.
    """
    verbose_print = lambda s: print(s) if verbose else None
    if modelfile is not None:
        verbose_print(f'Using custom skull-strip model weights from {modelfile}')
    else:
        verbose_print(f'Using skull-strip model version {version}')
        modelfile = ds.system.resource(f'models/synthstrip-{version}.pt')
    return ds.io.load_model(modelfile, device=device, expected=StripModel)


def command():
    """
    The skull-stripping subcommand, which can be run directly from the command line.
    """
    description = '''
    Robust skull-stripping for brain images of any contrast or resolution. The input
    does not need to be pre-processed in any way. This method can be applied to
    both infant and adult subjects. If you use SynthStrip in your analysis, please cite:

    <DIM>A. Hoopes, J.S. Mora, A.V. Dalca, B. Fischl, M. Hoffmann<BR>
    <DIM>SynthStrip: Skull-Stripping for Any Brain Image<BR>
    <DIM>NeuroImage 206 (2022), 119474
    '''
    epilog = '''
    Model input and output files can be configured a few different ways on the command
    line. To quickly skull-strip a single image, the input image and output volumes
    can be specified like so:

    <DIM>ds skull-strip --image image.nii.gz --out stripped.nii.gz

    To run the model on multiple images, you can provide a two-column text file as 
    input using the --list flag. This file is expected to contain a pair of
    image and output volume paths on each row. For example:

    <DIM>/path/to/image-01.nii.gz /path/to/stripped-01.mgz<BR>
    <DIM>/path/to/image-02.nii.gz /path/to/stripped-02.mgz

    This multi-image approach is recommended if you're using a GPU, since it will
    avoid repeating a time-consuming initialization on the device.
    '''
    parser = ds.system.SubcommandParser(description=description, epilog=epilog)
    # single-input processing
    single = parser.add_argument_group('Single-Image Processing')
    single.add_argument('-i', '--image', metavar='file', help='Input image (for single-image processing).')
    single.add_argument('-o', '--out', metavar='file', help='Masked image output file (for single-image processing).')
    # multi-input processing
    multi = parser.add_argument_group('Multi-Image Processing')
    multi.add_argument('--list', metavar='file', help='Input list for multi-image processing. See below for examples.')
    # other options (help flag will be added automatically)
    parser.add_argument('-b', '--border', default=1, type=int, help='Mask border threshold in mm. Default is 1.')
    parser.add_argument('--cpu', action='store_true', help='Force CPU usage when GPU is available.')
    parser.add_argument('--threads', type=int, help='Number of CPU threads. Default is max available.')
    parser.add_argument('--debug', action='store_true', help='View debugging information.')
    parser.add_argument('--model', metavar='file', help='Alternative model file to load.')
    parser.add_argument('--no-cite', action='store_true', help='Remove that pesky citation request.')
    args = parser.parse_args()

    # parse a docket of inputs to process
    docket = ds.system.parse_io_docket(
        parser=parser,
        listed_columns=['image_input', 'image_stripped'],
        single_input_args=['image', 'out'],
    )

    # configure the device
    device = ds.device.configure_device(cpu=args.cpu, threads=args.threads, verbose=True)

    # initialize the model
    strip_model = load_strip_model(device=device, modelfile=args.model, verbose=True)

    # initialize the brain cropping model used for preprocessing (not strictly necessary but
    # can speed up the stripping process for larger images)
    braincrop_model = load_brain_cropping_model(device=device, verbose=True)

    # loop through our input images
    for item in docket:

        # load input volume
        filename = item['image_input']
        image = sf.load_volume(filename)
        print(f'Stripping image {filename}')

        # compute a bounding box around the brain area
        bbox = braincrop_model.estimate(image, debug=args.debug, margin=20)

        # predict the mask
        mask = strip_model.estimate(image, bbox=bbox, border=args.border, debug=args.debug)

        # crop the input image with the mask
        image[mask == 0] = np.min([0, image.min()])
        image.save(item['image_stripped'])

    if not args.no_cite:
        print('If you use this tool in your analysis, please cite:')
        print('Hoopes et al. "SynthStrip: Skull-Stripping for Any Brain Image" NeuroImage (2022)')
