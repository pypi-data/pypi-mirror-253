import numpy as np
import surfa as sf
import torch
import deepsurfer as ds

from deepsurfer.modules.braincrop import load_brain_cropping_model


class TemplateAlignmentModel(ds.io.LoadableModule):

    @ds.io.store_config_args
    def __init__(self,
                 channels=[
                    [16, 16, 32, 32, 32, 32],
                    [32, 32, 32, 32]],
                 points_per_hemi=12,
                 in_channels=1,
                 in_voxsize=2,
                 in_orientation='RAS',
                 template_voxsize=1,
                 template_shape=[256, 256, 256],
                 template_center=[0, 0, 0],
                 template_rotation=[
                    [-1.,  0.,  0.],
                    [ 0.,  0.,  1.],
                    [ 0., -1.,  0.]],
        ):
        """
        An affine estimation model that aligns a template mesh to an input image.
        Using a template mesh instead of an image-to-image alignment is useful entirely
        for optimimzation benefits: it's faster, more stable, and easier to find a cortical
        alignment, since we can use uniformly resampled target surfaces and compute
        a one-to-one mesh simmilarity loss between the template and target vertices.

        The model is trained to predict a set of salient regions in the input image while
        learning a set of template points that correspond to those regions. The predicted
        regions are then used to compute barycenters, which are then used to estimate an
        affine transform, via weighted least-squares, that aligns the template points to
        the barycenters.

        This model was primarily developed to compute a rough initialization of cortical
        surface template meshes for topofit, but it actually doubles as a pretty good
        generic template-alignment method (plus has the benefit of being contrast agnostic).

        The model is also hard-coded to compute hemisphere specific affines, if desired.
        This is potentially (although not tested) useful for anatomies where the combined
        optimal alignment to the cortex of both hemispheres is drastically worse than the
        alignment of each hemisphere individually. Not sure how often that is the case, but
        there are some weird brains out there. The way this is handles is by assuming that
        the first half of the predicted points correspond to the left hemisphere and the
        last half of the points correspond to the right. This can be enforced during training.
        By default at estimation time, all three possible affines are computed.
        """
        super().__init__()

        # this is useful to have cached at inference time
        # important that the model was actually trained with this resolution!
        self.in_channels = in_channels
        self.in_voxsize = in_voxsize
        self.in_orientation = in_orientation

        # another important bit of information to have stores in the model
        # so that we can return affines with accurate embedded geometry
        self.template_geometry = sf.ImageGeometry(
                                        voxsize=template_voxsize,
                                        shape=template_shape,
                                        center=template_center,
                                        rotation=template_rotation)
        
        # number of salient points (features) to predict for each hemisphere
        self.points_per_hemi = points_per_hemi

        # initialize the predictor of image-based features (simple image unet)
        self.unet = ds.image.UNet(3, channels=channels, in_channels=in_channels)
        self.unet.add_convolution(points_per_hemi * 2, activation=torch.nn.ReLU())

        # initialize the embedded 'template' points, ie. the learned points that exist in template
        # space, which are optimized to correspond to the predicted feature points in the input image space.
        # for stability purposes we'll want to keep these parameter values with std close to 1, and scale
        # up their values by 100x to get then into a realistic mm coordinate space
        self.scale = 1e2
        self.normalized_points = torch.nn.Parameter(torch.randn(points_per_hemi * 2, 3), requires_grad=True)

        # these are nice to have around for matrix transforming
        self.register_buffer('ones', torch.ones(points_per_hemi * 2, 1), persistent=False)
        self.register_buffer('template_shape', torch.tensor(template_shape), persistent=False)

        # the grid stuff is used to compute feature barycenters, let's cache it and make sure
        # there's a way to easily update it when the input shape has changed
        self.grid = None
        self.gridshape = None

    def forward(self, image, vox2world):
        """
        Forward pass through the model. This computes predicted features from the input image
        and returns the learned source (template) and predicted target (input) coordinates
        along with mass values to compute a weighted least-squares affine estimate.

        Batched inputs are currently not supported.

        Note that this function is meant to be used under-the-hood and will only return the
        predicted coordinates. To predict the complete affine alignment given an input image,
        use the estimate() method.

        Parameters
        ----------
        image : Tensor
            The input image of shape (W, H, D) to compute features from. Batched inputs
            are currently not supported.
        vox2world : Tensor
            The voxel-to-world affine transform for the input image. This is used to transform
            the predicted feature coordinates from voxel space to world space. The expected
            shape is (4, 4).

        Returns
        -------
        source : (Tensor, Tensor, Tensor)
            A tuple of: source (template) coordinates of shape (N, 3), target (image) coordinates
            of shape (N, 3), and weight values of shape (N,).
        """

        # make sure the input image is in the correct shape
        if image.ndim == 3:
            image = image.unsqueeze(0)
        elif image.ndim != 4:
            raise ValueError(f'expected image to have 3 or 4 dims, got {image.ndim}')

        # precompute and cache mesh grid for computing barycenters. only need to update
        # this when the input image shape changes
        shape = image.shape[1:]
        if self.gridshape != shape:
            mesh = torch.meshgrid([torch.arange(s) for s in shape], indexing='ij')
            self.grid = [m.reshape(1, -1).to(image.device) for m in mesh]
            self.gridshape = shape

        # compute the features from the input image and flatten them
        features = self.unet(image.unsqueeze(0)).squeeze(0)
        flat = features.view(features.shape[0], -1)

        # compute the total mass of each feature - this is used to
        # weight which features are more important for this image
        mass = flat.sum(-1) + 1e-6
        barycenters = torch.stack([(d * flat).sum(-1) / mass for d in self.grid], dim=-1)

        # compute the target points in world space
        target = torch.cat([barycenters, self.ones], dim=-1)
        target = (vox2world @ target.T).T

        # compute the source points in world space
        source = self.world_source_points()
        source = torch.cat([source, self.ones], dim=-1)

        return (source, target, mass)

    def world_source_points(self):
        """
        Get the learned template (source) points in world space.

        Returns
        -------
        Tensor
            Points of shape (N, 3).
        """
        return self.normalized_points * self.scale

    def fit_affine(self, X, Y, M):
        """
        Fit an affine transform to the given source and target points via a weighted
        least-squares estimate.

        Parameters
        ----------
        X : Tensor
            Source points of shape (N, 3).
        Y : Tensor
            Target points of shape (N, 3).
        M : Tensor
            Coordinate saliency weight values of shape (N,).

        Returns
        -------
        Tensor
            Affine transform of shape (4, 4).
        """
        XT = X.T * (M / M.sum())
        B = torch.linalg.inv(XT @ X) @ XT @ Y
        return B.T

    def estimate(self, image, bbox=None, quantile=0.99, debug=False):
        """
        Estimate the affine transform that aligns the cortical template to an input anatomy.
        This method will return a three affines: a transform optimized to align both hemispheres
        at once and two separate transforms for optimized indivudually for each hemisphere.
        It's recommend to just use the combined transform, but the individual transforms can be
        useful for more precise hemispheric alignment.

        Parameters
        ----------
        image : sf.Volume
            The input image volume to align the template to.
        bbox : slicing, optional
            A bounding box around pertinent anatomy in the input image. This is used to crop
            the inputs to the model, speeding up the estimation substantially.
        quantile : float
            The image intensity quantile used as the max value for normalization
            during pre-processing. If None, the max intensity across the entire image
            is used.
        debug : bool, optional
            Show model debugging information and visualizations. Requires that the freeview
            visualization command is available on the system.

        Returns
        -------
        sf.Affine dict
            A dictionary of the estimated Affine transforms. The keys are 'wb' (whole-brain),
            'left', and 'right' (corresponding to the left and right hemispheres).
        """

        # conform the input image to the correct orientation, voxsize, and shape
        conformed = ds.normalize.shape_normalize(image,
                                                 levels=self.unet.num_levels,
                                                 bbox=bbox,
                                                 orientation=self.in_orientation,
                                                 voxsize=self.in_voxsize)

        # merge channels if the input image has more than one
        # TODO: implement a cross-conv version of the model to handle any-channel inputs
        if conformed.nframes > self.in_channels:
            ds.system.warning(f'The affine prediction does not yet support multi-channel inputs, so merging channels')
            conformed = (conformed * np.arange(1, conformed.nframes + 1)).mean(frames=True)

        # cache the current mode so we can reset after inference
        mode = self.training
        self.train(mode=False)
        with torch.no_grad():

            # turn our inputs into tensors and move to the right device
            I = ds.normalize.framed_array_to_tensor(conformed, device=self.device)
            I = ds.normalize.intensity_normalize(I, quantile=quantile, copy=False)
            M = torch.tensor(conformed.geom.vox2world.matrix, dtype=torch.float32, device=self.device)

            # predict the feature maps and compute barycenters of the salient points,
            # we can use this to compute individual affines
            source, target, mass = self(I, M)

            # so we want an affine that aligns the whole-brain, but we can also compute
            # hemisphere specific affines (potentially useful for initializing surfaces)
            # since we have points that were optimized for specific hemispheres
            affines = {}
            pph = self.points_per_hemi

            # first do the whole-brain WLS alignment on all points
            mat = self.fit_affine(source, target, mass).cpu().numpy().squeeze()
            affines['wb'] = sf.Affine(mat, source=self.template_geometry, target=image, space='world')

            # now do the left hemi WLS alignment on the first half of points
            mat = self.fit_affine(source[:pph], target[:pph], mass[:pph]).cpu().numpy().squeeze()
            affines['lh'] = sf.Affine(mat, source=self.template_geometry, target=image, space='world')

            # lastly do the right hemi WLS alignment on the second half of points
            mat = self.fit_affine(source[pph:], target[pph:], mass[pph:]).cpu().numpy().squeeze()
            affines['rh'] = sf.Affine(mat, source=self.template_geometry, target=image, space='world')

        # reset to the previous training/evaluation state
        self.train(mode=mode)

        # visualize
        if debug:
            # load the template meshes and transform them to the image space
            lh = sf.load_mesh(ds.system.resource('template/cortex-int-lh.srf')).transform(affines['lh'])
            rh = sf.load_mesh(ds.system.resource('template/cortex-int-rh.srf')).transform(affines['rh'])
            # view the template alignment on the input image
            fv = sf.vis.Freeview(title='Template Alignment Debugging')
            fv.add_image(image, name='Raw Input Image')
            fv.add_image(conformed, name='Conformed Model Input')
            fv.add_mesh(lh, name='Aligned Left Template')
            fv.add_mesh(rh, name='Aligned Right Template')
            fv.show(background=False)

        return affines


"""
TODO: the training code for this model still needs to be updated to work with the new refactoring
of the framework, so it's been excluded from the package for now.
"""


def load_alignment_model(device, version='1', modelfile=None, verbose=False):
    """
    Load the default cortical template alignment model.
    """
    verbose_print = lambda s: print(s) if verbose else None
    if modelfile is not None:
        verbose_print(f'Using custom alignment model weights from {modelfile}')
    else:
        verbose_print(f'Using alignment model version {version}')
        modelfile = ds.system.resource(f'models/template-alignment-{version}.pt')
    return ds.io.load_model(modelfile, device=device, expected=TemplateAlignmentModel)


def command():
    """
    The template alignment subcommand, which can be run directly from the command line.
    """
    description = '''
    Affinely-align the deepsurfer template to the cortex of an adult brain image
    with any contrast or resolution. The input does not need to be skull-stripped
    or pre-processed in any way. This approach can also adapt to images with only
    one visible hemisphere.

    The output of this tool is an affine transform (in world/scanner coordinates)
    that transforms the deepsurfer template to the input image. So, the inverse
    of this transform could also be used to move the subject into a standardized space.
    Note that the world (RAS) position of this template is the same as the fsaverage
    space of freesurfer.
    '''
    epilog = '''
    Model input and output files can be configured a few different ways on the command
    line. To quickly run the alignment on a single image, the input image and output
    affine can be specified like so:

    <DIM>ds template-align --image image.nii.gz --affine affine.lta

    To run the model on multiple images, you can provide a two-column text file as 
    input using the --list flag. This file is expected to contain a pair of
    image and output affine paths on each row. For example:

    <DIM>/path/to/image-01.nii.gz /path/to/affine-01.lta<BR>
    <DIM>/path/to/image-02.nii.gz /path/to/affine-02.lta

    This multi-image approach is recommended if you're using a GPU, since it will
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
    single.add_argument('-a', '--affine', metavar='file', help='Template-to-image affine output (for single-image processing).')
    # multi-input processing
    multi = parser.add_argument_group('Multi-Image Processing')
    multi.add_argument('--list', metavar='file', help='Input list for multi-image processing. See below for examples.')
    multi.add_argument('--subjs', nargs='+', metavar='subj', help='Subjects to process. Requires that IO type is provided.')
    multi.add_argument('--io', metavar='format', help='IO format type.')
    # other options (help flag will be added automatically)
    parser.add_argument('--cpu', action='store_true', help='Force CPU usage when GPU is available.')
    parser.add_argument('--threads', type=int, help='Number of CPU threads. Default is max available.')
    parser.add_argument('--debug', action='store_true', help='View debugging information.')
    parser.add_argument('--model', metavar='file', help='Alternative model file to load.')
    parser.add_argument('--suffix', metavar='suffix', help='Optional suffix to append to output filenames.')
    args = parser.parse_args()

    # parse a docket of inputs to process
    docket = ds.system.parse_io_docket(
        parser=parser,
        listed_columns=['image_input', 'template_affine'],
        single_input_args=['image', 'affine'],
    )

    # configure the device
    device = ds.device.configure_device(cpu=args.cpu, threads=args.threads, verbose=True)

    # initialize the registration model
    alignment_model = load_alignment_model(device=device, modelfile=args.model, verbose=True)

    # initialize the brain cropping model used for preprocessing (not strictly necessary but
    # can speed up the alignment process for larger images)
    braincrop_model = load_brain_cropping_model(device=device, verbose=True)

    # loop through our input images
    for item in docket:

        # load input volume
        filename = item['image_input']
        image = sf.load_volume(filename)
        print(f'Aligning to input image {filename}')

        # compute a bounding box around the brain area
        bbox = braincrop_model.estimate(image)

        # predict the alignment
        affines = alignment_model.estimate(image, bbox=bbox, debug=args.debug)

        # only save the whole brain alignment (no need to write hemi-specific affines here)
        affines['wb'].save(ds.system.add_suffix(item['template_affine'], args.suffix))
