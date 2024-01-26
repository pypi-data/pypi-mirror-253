import numpy as np
import surfa as sf
import torch
import deepsurfer as ds


class BrainCroppingModel(ds.io.LoadableModule):

    @ds.io.store_config_args
    def __init__(self,
                 channels=[
                    [16, 16, 32, 32, 32, 32],
                    [32, 32, 32, 32]],
                 in_channels=1,
                 in_voxsize=4,
        ):
        """
        A simple convolutional network used to predict a bounding-box around the brain.
        This is useful as a preprocessing step to reduce image sizes as much as possible
        before using them as input to larger, more time-consuming networks. For example,
        a whole-brain segmentation network that expects 1mm resolution input images can
        take a very long time operating on standard (256 x 256 x 256) input images. However,
        if the image was cropped around the brain, for example to a shape of (160, 160, 224),
        this offers a huge runtime and memory improvement.

        This network is meant to be super fast, so it's (relatively) small and trained
        on heavily downsampled images. The architecture is a simple unet, which predicts
        a rough segmentation of the skull interior (with CSF). The idea is that at test time,
        the input is downsampled to a predefined voxel size and passed to the network, which
        predicts a low-res segmentation of everything inside the skull. A bounding box is
        computed on the largest connected-component of this segmentation and then converted 
        back to the input-resolution space. Take a look at the estimate() method for the
        test-time implementation.

        But wait there's more! We can also use this small network to quickly infer information
        about the underlying anatomical brain orientation: instead of just predicting a binary
        mask of the interior skull volume, the network also predicts a small set of rough interior
        brain labels along the midline. The barycenters of these predicted labels can then be
        point-to-point aligned with template points in world space to compute a rough
        image-coordinate-to-world-coordinate rotation. This is useful for catching corrupted
        image header matrices, which are extremely problematic for most tools that expect correctly
        oriented images. So, during training, it is important to vary the image orientation.
        """
        super().__init__()

        # this is useful to have cached at inference time
        # important that the model was actually trained with this resolution!
        self.in_voxsize = in_voxsize
        self.in_channels = in_channels

        # here we load and cache the template barycenters of the template midline segmentation
        # used to infer the orientation of the input image. it's important that these barycenters
        # are in world (RAS) coordinate space
        seg = sf.load_volume(ds.system.resource('template/orienting-seg.mgz'))
        self.orienting_labels = np.arange(1, seg.max() + 1)
        self.template_points = seg.barycenters(labels=self.orienting_labels, space='world')
        self.template_points -= self.template_points.mean(0)

        # this model is just a straight-forward unet
        self.unet = ds.image.UNet(ndim=3, channels=channels, in_channels=in_channels)

        # add the final softmax layer to the unet to predict the segmentation. the final segmentation
        # will have labels corresponding to each of the 'orienting midline labels' as well as a label
        # for the 'rest of the skull interior'
        num_labels = len(self.template_points) + 2
        self.unet.add_convolution(num_labels, activation=torch.nn.Softmax(dim=1))

    def forward(self, image):
        """
        Straight-forward forward pass that calls the underlying unet. Expects the input to be
        batched with shape (B, 1, W, H, D).

        Note that this function is meant to be used under-the-hood and will only return the
        predicted feature map. To predict a complete cropping given an input image, use the
        estimate() method.

        Parameters
        ----------
        image : Tensor
            The input image of shape (B, 1, W, H, D) to compute features from.

        Returns
        -------
        Tensor
            The predicted probability segmentation of shape (B, C, W, H, D) where C is the
            number of the predicted classes.
        """
        if image.ndim != 5:
            raise ValueError('expected 5-dimensional batched input of shape (B, 1, W, H, D), '
                            f'but got input with shape {image.shape}')
        return self.unet(image)

    def estimate(self, image, margin=10, check_orientation=True, return_seg=False, quantile=0.99, debug=False):
        """
        Crop around the brain region of an image and check the accuracy of the image world
        transform by predicting coarse brain segmentations. This is useful for catching
        corrupted image headers, which are problematic for most tools that expect
        uniformly oriented images.

        Parameters
        ----------
        image : Volume
            The input image to crop around the brain.
        margin : int, optional
            Bounding box padding from the brain boundary, in mm.
        check_orientation : bool, optional
            Whether to check the orientation of the input image. If the orientation embedded in
            the image header does not match up with the estimated brain orientation, an error will
            be thrown.
        return_seg : bool, optional
            Whether to additionally return the predicted segmentation labels.
        quantile : float
            The image intensity quantile used as the max value for normalization
            during pre-processing. If None, the max intensity across the entire image
            is used.
        debug : bool, optional
            Show model debugging information and visualizations. Requires that the freeview
            visualization command is available on the system.

        Returns
        -------
        slicing or (slicing, Volume)
            The boundary box as a tuple of slice objects. If return_seg is True, then the predicted
            label map is returned as a second output.
        """

        if image.nframes > self.in_channels:
            ds.system.fatal(f'input image has {image.nframes} frames but model expects {self.in_channels}')

        # conform the input image to the model voxel size. the network should be trained to be
        # orientation-agnostic so no need to worry about reorienting
        conformed = ds.normalize.shape_normalize(image, levels=self.unet.num_levels, voxsize=self.in_voxsize)

        # cache the current model mode so we can reset after it inference is done
        mode = self.training
        self.train(mode=False)
        with torch.no_grad():

            # turn our inputs into tensors and move to the right device
            I = ds.normalize.framed_array_to_tensor(conformed, device=self.device)
            I = ds.normalize.intensity_normalize(I, quantile=quantile, copy=False)
            
            # predict the feature map and convert tensor back to a surfa volume
            probseg = self(I.unsqueeze(0)).squeeze(0)
            probseg = conformed.new(probseg.moveaxis(0, -1).cpu().numpy())

            # collapse the labels into a discrete segmentation
            seg = probseg.collapse()

            # visualize
            if debug:
                fv = sf.vis.Freeview(title='Brain Crop Debugging')
                fv.add_image(image, name='Raw Input Image')
                fv.add_image(conformed, name='Conformed Model Input')
                fv.add_image(probseg, name='Probabilistic Seg', colormap='heat', visible='false')
                fv.add_image(seg, name='Collapsed Seg', colormap='lut')
                fv.show(background=False)

            # here we will run the orientation check, to ensure that the actual anatomical data
            # correctly corresponds to the anatomical orientation encoded in the image header.
            # it's pretty important that the header matrix is correct, so this block will throw
            # a hard error if the check fails
            if check_orientation:

                # extract the barycenters of the predicted 'orienting' labels. remember the last
                # predicted label is just the 'rest of the brain', so we can exclude it for the
                # orientation check here
                subject_points = probseg.barycenters()[1:-1]
                subject_points -= subject_points.mean(0)

                # now that we have the orientating barycenter points for the input (in image coordinate
                # space), we can rigidly align them to the corresponding barycenters of the template points
                # (in world coordinate space) and compute a rotation to infer orientation type
                C = np.dot(np.transpose(self.template_points), subject_points) / len(subject_points)
                V, S, W = np.linalg.svd(C)
                if (np.linalg.det(V) * np.linalg.det(W)) < 0.0:
                    S[-1] = -S[-1]
                    V[:, -1] = -V[:, -1]
                rotation = np.dot(V, W)
                inferred_orientation = sf.transform.orientation.rotation_matrix_to_orientation(rotation)

                # okay now we check if the predicted orientation is the same as the orientation encoded
                # in the header cosine direction matrix. we can't reasonably make any assumptions about
                # which side of the brain is the left or right, so we'll have to ignore that axis and
                # leave it up to the user to figure out (wouldn't want to be them...)
                predicted = inferred_orientation.replace('L', 'H').replace('R', 'H')
                current = image.geom.orientation.replace('L', 'H').replace('R', 'H')
                if predicted != current:
                    pred_left  = predicted.replace('H', 'L')
                    pred_right = predicted.replace('H', 'R')
                    current = image.geom.orientation
                    ds.system.fatal('Detected potentially incorrect cosine direction matrix in the image header! '
                                    'The matrix implies anatomical orientation '
                                   f'{sf.transform.orientation.complete_name(current)} ({current}), but based on '
                                    'the image data, it seems more likely to be in '
                                   f'{sf.transform.orientation.complete_name(pred_left)} ({pred_left}) or '
                                   f'{sf.transform.orientation.complete_name(pred_right)} ({pred_right}) orientation')

            # compute the bounding box on the largest connected component
            cropping = (seg > 0).connected_component_mask().bbox()

            # grow or shrink the bounding box by some set margin (in mm)
            margin = np.asarray(margin) / seg.geom.voxsize
            cropping = sf.slicing.expand_slicing(cropping, image.baseshape, margin)

            # now get the cropping bbox coordinates into the space of the original input resolution
            vox2vox = image.geom.world2vox @ seg.geom.vox2world
            cropping = sf.slicing.convert_slicing(cropping, image.baseshape, vox2vox)

        # reset to the previous training/evaluation state
        self.train(mode=mode)

        if return_seg:
            return (cropping, seg)
        return cropping


"""
TODO: the training code for this model still needs to be updated to work with the new refactoring
of the framework, so it's been excluded from the package for now.
"""


def load_brain_cropping_model(device, version=1, modelfile=None, verbose=False):
    """
    Load the default brain cropping model.
    """
    verbose_print = lambda s: print(s) if verbose else None
    if modelfile is not None:
        verbose_print(f'Using custom cropping model weights from {modelfile}')
    else:
        verbose_print(f'Using cropping model version {version}')
        modelfile = ds.system.resource(f'models/brain-cropping-{version}.pt')
    return ds.io.load_model(modelfile, device=device, expected=BrainCroppingModel)


def command():
    """
    The brain cropping subcommand, which can be run directly from the command line.
    """
    description = '''
    Rapidly crop the image closely around the interior skull volume. Useful for preprocessing
    inputs for size-sensitive tools or for efficient file storage. This tool works on
    adult brain scans with any contrast, resolution, or orientation. The input does
    not need to be skull-stripped or pre-processed in any way. This approach can also
    adapt to images with only one visible hemisphere.

    To increase or decrease the size of the cropping bounding-box around the brain, use
    the --margin flag, detailed below.
    '''
    epilog = '''
    Model input and output files can be configured a few different ways on the command
    line. To quickly crop a single image, the input image and cropped output image can be
    specified like:

    <DIM>ds brain-crop --image image.nii.gz --cropped cropped.nii.gz

    To run the model on multiple images, you can provide a two-column text file as 
    input using the --list flag. This file is expected to contain a pair of
    image and output paths on each row. For example:

    <DIM>/path/to/image-01.nii.gz /path/to/cropped-01.nii.gz<BR>
    <DIM>/path/to/image-02.nii.gz /path/to/cropped-02.nii.gz

    This multi-input approach is recommended if you're using a GPU, since it will
    avoid repeating a time-consuming initialization on the device.

    Another way to provide multiple inputs is by specifying a set of subjects,
    either via the --subjs flag or pointing to a list of subjects with --list. For
    this approach, the --io flag must be used to indicate a subject type, such as
    'fs' (which corresponds to freesurfer-style subjects). It's recommended to use
    the --suffix option if you don't want to overwrite standard subject files.
    '''
    parser = ds.system.SubcommandParser(description=description, epilog=epilog)
    # single-input processing
    single = parser.add_argument_group('Single-Image Processing')
    single.add_argument('-i', '--image', metavar='file', help='Input image (for single-image processing).')
    single.add_argument('-c', '--cropped', metavar='file', help='Cropped output image (for single-image processing).')
    # multi-input processing
    multi = parser.add_argument_group('Multi-Image Processing')
    multi.add_argument('--list', metavar='file', help='Input list for multi-image processing. See below for examples.')
    multi.add_argument('--subjs', nargs='+', metavar='subj', help='Subjects to process. Requires that IO type is provided.')
    multi.add_argument('--io', metavar='format', help='IO format type.')
    # other options (help flag will be added automatically)
    parser.add_argument('--margin', type=float, default=10, help='Crop margin from brain boundary in mm.')
    parser.add_argument('--shape', nargs=3, type=int, help='Fix the cropped image shape (centered around brain).')
    parser.add_argument('--cpu', action='store_true', help='Force CPU usage when GPU is available.')
    parser.add_argument('--threads', type=int, help='Number of CPU threads. Default is max available.')
    parser.add_argument('--debug', action='store_true', help='View debugging information.')
    parser.add_argument('--model', metavar='file', help='Alternative model file to load.')
    parser.add_argument('--suffix', metavar='suffix', help='Optional suffix to append to output filenames.')
    args = parser.parse_args()

    # parse a docket of inputs to process
    docket = ds.system.parse_io_docket(
        parser=parser,
        listed_columns=['image_input', 'image_cropped'],
        single_input_args=['image', 'cropped'],
    )

    # configure the device
    device = ds.device.configure_device(cpu=args.cpu, threads=args.threads, verbose=True)

    # initialize the model
    model = load_brain_cropping_model(device=device, modelfile=args.model, verbose=True)

    # loop through our input images
    for item in docket:

        # load input volume
        filename = item['image_input']
        image = sf.load_volume(filename)
        print(f'Cropping input image {filename}')

        # predict and save the cropping
        cropping = model.estimate(image, margin=args.margin, debug=args.debug)

        # crop the image
        if args.shape is not None:
            cropping = sf.slicing.fit_slicing_to_shape(cropping, image.baseshape, args.shape)
            cropped = image[cropping].reshape(args.shape, copy=False)
        else:
            cropped = image[cropping]

        cropped.save(ds.system.add_suffix(item['image_cropped'], args.suffix))
