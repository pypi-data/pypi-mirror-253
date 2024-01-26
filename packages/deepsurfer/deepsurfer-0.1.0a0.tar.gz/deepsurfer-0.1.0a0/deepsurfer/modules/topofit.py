import os
import numpy as np
import surfa as sf
import torch
import deepsurfer as ds

from deepsurfer.optional import voxynth
from deepsurfer.modules.aligntemplate import load_alignment_model


class TopoFitModel(ds.io.LoadableModule):

    @ds.io.store_config_args
    def __init__(self,
                 image_unet_channels=[
                    [16, 32, 32, 64, 64],
                    [64, 64, 64, 64]],
                 image_in_channels=1,
                 graph_block_resolutions=[0, 1, 2, 3, 4, 5, 6],
                 graph_block_channels=64,
                 graph_block_convs_per_level=2,
                 graph_block_levels=3,
                 graph_block_scale=10,
                 graph_block_steps=1,
                 quad_block_channels=[16],
                 quad_block_iterations=10,
                 in_voxsize=1,
                 include_positions=False,
        ):
        """
        TopoFit is a cortical surface reconstruction model that predicts meshes
        corresponding to interior white-matter and exterior gray-matter (pial) cortical
        boundaries.

        The model involves a joint image and graph-based convolutional architecture
        that deforms a roughly aligned template mesh to the anatomy of the input
        image. An image-based UNet first predicts the features that are later
        interpolated at the positions of mesh coordinates. These sampled features are
        passed through a series of graph-based (or edge-based) UNets that each predict
        a set of deformation vectors for the mesh. The mesh is upsampled after every
        few steps (or blocks), and this series of steps maps the template mesh to the
        white-matter boundary of the input image. The exterior pial surface is estimated
        as a single deformation of the predicted white-matter surface. To maximize the
        smoothness of this final deformation, a quadrature-based update scheme is used.

        Since the resulting surfaces are derived from a precomputed template mesh, the
        output is guaranteed to have a valid explicit topology (e.g. connectivity), which
        avoids the need for a time-consuming topology correction step. Note that this
        doesn't necessarily prevent implicit topological errors (e.g. self-intersections),
        but these types of error are generally small and very rare since we use a mesh
        regularization loss during training. As a last contigency to remove these small
        intersections, a final edge-based convolution layer is applied to smooth problematic
        regions of the surface, while preserving the overall shape.

        The model is described in further detail in "TopoFit: Rapid Reconstruction of
        Topologically-Correct Cortical Surfaces" by Hoopes et al. (2022).

        Parameters
        ----------
        image_unet_channels : list of lists of ints
            Tuple containing the number of channels for each level of the image
            UNet encoder and decoder.
        image_in_channels : int
            Number of channels for the input image.
        graph_block_resolutions : list of ints
            The resolution level of the mesh to use for each deformation block. The
            first block operates on the input template mesh, and each subsequent
            block operates on the output of the previous block.
        graph_block_channels : int or list of ints
            The number of channels to use at each level of the graph-based UNet.
            Can be a single value or a list the same length as the graph-block
            resolutions.
        graph_block_convs_per_level : int or list of ints
            The number of convolutions to use at each level of the graph-based
            UNet. Can be a single value or a list the same length as the
            graph-block resolutions.
        graph_block_levels : int or list of ints
            The number of levels to use in the graph-based UNet. Can be a single
            value or a list the same length as the graph-block resolutions.
        graph_block_scale : int or list of ints
            The amount to scale the deformation of each block (to control gradients).
            This is more useful for the first few blocks, which often deform across
            large distances. Can be a single value or a list the same length as
            the graph-block resolutions.
        graph_block_steps : int or list of ints
            The number of times to run each block. This is useful for attaining a more
            accurate fit at higher resolution levels. Can be a single value or a list
            the same length as the graph-block resolutions.
        quad_block_channels : list of ints
            The number of channels for each linear layer in the quadrature-based
            deformation block.
        quad_block_iterations : int
            The number of quadrature iterations for pial surface estimation. For 1mm
            voxel size images, 10 iterations is sufficient.
        """
        super().__init__()
        self.in_voxsize = in_voxsize

        # initialize the predictor of image-based features (simple image unet)
        self.image_net = ds.image.UNet(ndim=3, channels=image_unet_channels, in_channels=image_in_channels)
        self.image_in_channels = image_in_channels

        # we need to know how many features the image net outputs
        image_final_channels = self.image_net.final_channels

        # import the base template surface (the left hemisphere is the base mesh, arbitrarily chosen)
        self.template_mesh = sf.load_mesh(ds.system.resource('template/cortex-int-lh.srf')).convert(space='image')

        # load the collection of topologies (eg. connectivity) for each mesh resolution
        filename = ds.system.resource('template/surf-topology.npz')
        self.topology_collection = ds.surf.template.load_topology_collection(filename)

        # load the affine transform that maps the template mesh vertices from the left
        # to the right hemisphere (the mesh is the same across sides of the brain)
        filename = ds.system.resource('template/left-to-right.lta')
        self.left2right = sf.load_affine(filename).convert(space='world')

        # first, initialize the set of learnable deformation blocks, that operate in
        # the mesh domain and sample from the predicted image-space features
        self.deformation_blocks = torch.nn.ModuleList()

        # utility to ensure that graph block parameters are a single value or a list with correct length
        def conform_block_param(parameter):
            if not np.iterable(parameter):
                return [parameter for _ in graph_block_resolutions]
            elif len(parameter) != len(graph_block_resolutions):
                raise ValueError(f'expected a single value or a list of values with the '
                                  'same length as graph_block_resolutions')
            return parameter

        graph_block_scale = conform_block_param(graph_block_scale)
        graph_block_convs_per_level = conform_block_param(graph_block_convs_per_level)
        graph_block_channels = conform_block_param(graph_block_channels)
        graph_block_levels = conform_block_param(graph_block_levels)
        graph_block_steps = conform_block_param(graph_block_steps)

        # configure the full graph (edge) convolutional blocks to predict deformations
        for i, resolution in enumerate(graph_block_resolutions):
            # configure the channel specification for the edge-conv unet
            channels = ds.image.unet.make_channel_lists(
                    num_levels=min(resolution + 1, graph_block_levels[i]),
                    base_channels=graph_block_channels[i],
                    convs_per_level=graph_block_convs_per_level[i],
                    multiplier=1)
            # initialize the deformation block
            self.deformation_blocks.append(
                ds.surf.deform.GraphDeformationBlock(
                    channels=channels,
                    in_channels=image_final_channels,
                    scale=graph_block_scale[i],
                    topology_collection=self.topology_collection,
                    resolution=resolution,
                    steps=graph_block_steps[i],
                    include_positions=include_positions,
                    ))

        # lastly we want a seperate block to estimate the exterior pial boundary
        # as a deformation of the interior surface. for this we use a
        # quadrature deformation block, which is more likely to enforce
        # diffeomorphisms but is less useful for complex transformations. since
        # the pial surface is just a short outward extension of the interior mesh, this
        # type of deformation estimation is quite practical
        self.pial_deformation_block = ds.surf.deform.QuadDeformationBlock(
                                        channels=quad_block_channels,
                                        in_channels=image_final_channels,
                                        iterations=quad_block_iterations)

        # easiest way to track the resolution level corresponding to each deformation block
        # plus it's easier to just precompute which blocks should upsample the mesh afterwards
        self.graph_block_resolutions = graph_block_resolutions
        upsample_steps = np.diff(self.graph_block_resolutions)
        if np.any(upsample_steps > 1):
            raise ValueError('resolution level should increase by no more than 1 at each step')
        self.block_should_upsample = np.append(upsample_steps, 0).astype(np.bool8)

        # construct the downsampled template mesh vertices that will be aligned
        # to each subject and used as the initial starting point for the surface
        nv = self.topology_collection[graph_block_resolutions[0]].nv
        vs = np.ones((nv, 4), dtype=np.float32)
        vs[:, :-1] = self.template_mesh.vertices[:nv]
        self.register_buffer('template_vertices', torch.from_numpy(vs), persistent=False)

    def to(self, device):
        """
        Move the model and associated mesh topology collection to a device.

        Parameters
        ----------
        device : torch.device
            The device to move the model to.

        Returns
        -------
        self : TopoFitModel
        """
        super().to(device)
        for topo in self.topology_collection:
            topo.to(device)
        return self

    def forward(self, image, affine, skip=0):
        """
        Forward pass through the model. This predicts features from the input image,
        predicts deformation steps from the image features, and returns the resulting
        interior surface coordinates, exterior surface coordinates, and final mesh topology.

        Batched inputs are currently not supported.

        Note that this function is meant to be used under-the-hood and will only return the
        predicted coordinates. To return complete surface objects, use the estimate() method.

        Parameters
        ----------
        image : torch.Tensor
            The input image tensor of shape (channels, width, height, depth).
        affine : torch.Tensor
            The voxels-space affine transform tensor of shape (4, 4), which roughly maps
            the template to the input image.
        skip : int
            The number of graph deformation blocks to skip at the end of the network. This
            is useful for speeding up the initial training stage, since we can skip the last
            high-resolution deformation and still learn a good alignment.

        Returns
        -------
        dict
            Returns a dictionary with the predicted interior surface vertices ('interior') of
            shape (V, 3), the exterior surface vertices ('exterior') of shape (V, 3), and the
            associated mesh topology for the final resolution ('topology').
        """

        # sanity checks on input shape
        if image.ndim != 4 or image.shape[0] != self.image_in_channels:
            raise ValueError('expected input image of shape (C, W, H, D)')
        if affine.shape != (4, 4):
            raise ValueError('expected input affine of shape (4, 4)')

        # extract image shape as tensor to use later on for point sampling
        image_shape = torch.tensor(image.shape[1:]).to(image.device)

        # apply the affine alignment to the initial templace surface
        int_vertices = (affine @ self.template_vertices.T).T[:, :-1]

        # predict the image-space features to sample from. the unet expects
        # inputs with a batch dimension so we mess with the axes a bit here
        image_features = self.image_net(image.unsqueeze(0)).squeeze(0)

        # now iterate over the set of deformation 'blocks', which involve
        # sampling image features at the corresponding surface points and using
        # those sampled mesh-based features to predict a mesh deformation
        for i, deformation_block in enumerate(self.deformation_blocks):

            # predict and apply the deformation
            int_vertices = deformation_block(image_features, int_vertices, image_shape=image_shape)

            # cache the topology of the current mesh resolution level
            res = self.graph_block_resolutions[i]
            topology = self.topology_collection[res]

            # skip the last few deformation blocks if requested
            if skip > 0 and i == (len(self.deformation_blocks) - 1 - skip):
                break

            # upsample to the next mesh resolution if necessary
            if self.block_should_upsample[i]:
                int_vertices = topology.upsample(int_vertices)

        # include face indices in the result for quick mesh construction
        result = {
            'interior': int_vertices,
            'topology': topology,
        }

        # deform the final interior surface outward to the pial boundary
        ext_vertices = self.pial_deformation_block(image_features, int_vertices, image_shape=image_shape)
        result['exterior'] = ext_vertices

        return result

    def estimate(self, image, affine, hemi, quantile=None):
        """
        Predict the interior (white-matter) and exterior (gray-matter) surface boundary
        of the cortex for a given hemisphere. This method expects that an affine transform
        has already been computed to to roughly align the template to the input image space.
        If this has not been computed, it can be quickly estimated using the trained
        `TemplateAlignmentModel` model.

        Parameters
        ----------
        image : sf.Volume
            The input image volume.
        affine : sf.Affine
            The affine transform mapping the template space to the input image space.
        hemi : str
            The hemisphere to reconstruct ('L' or 'R').
        quantile : float
            The image intensity quantile used as the max value for normalization
            during pre-processing. If None, the max intensity across the entire image
            is used.

        Returns
        -------
        dict of sf.Mesh
            Returns a dictionary with the predicted white-matter surface mesh ('interior') the pial
            surface mesh ('exterior').

        See Also
        --------
        TemplateAlignmentModel
        """

        if image.nframes > self.image_in_channels:
            ds.system.fatal(f'input image has {image.nframes} frames but model expects {self.image_in_channels}')

        # since the default template mesh orientation is aligned to the left hemisphere (this was arbitrarily
        # chosen), we first convert the affine to world space so we can modify the orientation if we're fitting
        # surfaces to the right hemisphere
        affine = affine.convert(space='world', source=self.template_mesh, target=image)
        if hemi[0].upper() == 'R':
            # TODO: shouldn't surfa account for this type of thing??
            affine = sf.Affine(affine @ self.left2right, source=affine.source,
                               target=affine.target, space='world')
            orientation = 'RIA'
        elif hemi[0].upper() == 'L':
            orientation = 'LIA'
        else:
            raise ValueError(f'hemi must be \'L\' or \'R\' but got \'{hemi}\'')

        # crop the input image to a bounding box of the affinely-aligned template mesh, but
        # add some extra padding to be safe (this padding was determined empirically)
        coords = self.template_mesh.transform(affine).vertices
        bbox = sf.slicing.coords_to_slicing(np.asarray([coords.min(0), coords.max(0)]))
        bbox = sf.slicing.expand_slicing(bbox, image.baseshape, (14, 14, 12))

        # conform the input image to the correct orientation, voxsize, and shape
        conformed = ds.normalize.shape_normalize(image,
                                                 levels=self.image_net.num_levels,
                                                 bbox=bbox,
                                                 orientation=orientation,
                                                 voxsize=self.in_voxsize)

        # convert the affine to the template and connformed voxel spaces
        affine = affine.convert(space='image', source=self.template_mesh, target=conformed)

        # cache the current model mode so we can reset after it inference is done
        mode = self.training
        self.train(mode=False)
        with torch.no_grad():

            # turn our inputs into tensors and move to the right device
            I = ds.normalize.framed_array_to_tensor(conformed, device=self.device)
            I = ds.normalize.intensity_normalize(I, quantile=quantile, copy=False)
            M = torch.tensor(affine.matrix, dtype=torch.float32, device=self.device)

            # estimate and extract the results
            result = self(I, M)

        # reset to the previous training/evaluation state
        self.train(mode=mode)

        # mesh face indices
        faces = result['topology'].faces.cpu().numpy()

        # since we flipped thr orientation of the right hemisphere, we also need to
        # flip the face indices so the mesh is still oriented correctly
        # TODO: maybe this should be built into the surfa mesh convert method
        if hemi[0].upper() == 'R':
            faces = faces[:, ::-1]

        # convert white matter surface coordinate to a mesh with correct image geometry
        int_vertices = result['interior'].cpu().numpy()
        int_mesh = sf.Mesh(int_vertices, faces, geometry=conformed, space='image').convert(geometry=image, space='surf')
        surfaces = {'interior': int_mesh}

        # now do the same for the exterior gray matter (pial) surface
        ext_vertices = result['exterior'].cpu().numpy()
        ext_mesh = sf.Mesh(ext_vertices, faces, geometry=conformed, space='image').convert(geometry=image, space='surf')
        surfaces['exterior'] = ext_mesh

        return surfaces


class Trainer(ds.training.BaseModelTrainer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # necessary for training speed gains
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.deterministic = True

        # initialize the model
        model_parameters = self.config.opt('model', {})
        self.model = TopoFitModel(**model_parameters).to(self.device)

        # 
        def init(m):
            if isinstance(m, (torch.nn.Conv1d, torch.nn.Conv3d, torch.nn.Linear)):
                fan = torch.nn.init._calculate_correct_fan(m.weight, mode='fan_in')
                std = np.sqrt(2) / np.sqrt(fan)
                torch.nn.init.trunc_normal_(m.weight, std=std, a=(-2 * std), b=(2 * std))
                torch.nn.init.zeros_(m.bias)
        self.model.apply(init)

        # 
        for block in self.model.deformation_blocks:
            torch.nn.init.normal_(block.edgenet.extra[-1].conv1d.weight, mean=0.0, std=1e-4)
        torch.nn.init.normal_(self.model.pial_deformation_block.layers[-1].weight, mean=0.0, std=1e-4)

        # initialize the optimizer (start with the guided learning rate)
        guided_lr = self.config.opt('optimization/guided_lr', 1e-4)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=guided_lr)

        # learning rate to use after the guided stages are complete
        self.lr = self.config.opt('optimization/lr', 5e-5)

        # 
        if self.config.opt('optimization/half_precision', False):
            self.mixed_type = torch.float16
            self.grad_scaler = torch.cuda.amp.GradScaler()

        # 
        self.stage_1_end = self.config.opt('optimization/stage_1_end', 400)
        self.stage_2_end = self.config.opt('optimization/stage_2_end', 800)

        # stage 1 - initial 'guided' loss weights
        self.loss_weights_stage_1 = {
            'Int One-To-One': 1,
            'Int Chamfer':    1,
            'Ext Chamfer':    1,
            'Int Hinge':      100,
            'Ext Hinge':      100,
        }

        # stage 2 - partially 'guided' loss weights
        self.loss_weights_stage_2 = {
            'Int One-To-One': 0.1,
            'Int Chamfer':    1,
            'Ext Chamfer':    1,
            'Int Hinge':      10,
            'Ext Hinge':      10,
        }

        # stage 3 - final loss weights
        self.loss_weights_stage_3 = {
            'Int One-To-One': 0.0001,
            'Int Chamfer':    1,
            'Ext Chamfer':    1,
            'Int Hinge':      self.config.opt('optimization/int_hinge_loss_weight', 0.5),
            'Ext Hinge':      self.config.opt('optimization/ext_hinge_loss_weight', 0.5),
        }

        # 
        self.loss_weights = self.loss_weights_stage_1

        # 
        self.skipped_hires_epochs = self.config.opt('optimization/skipped_hires_epochs', 2000)

        # 
        self.scheduler_starting_epoch = self.config.opt('optimization/scheduler_starting_epoch', 2000)

        # configure the learning rate scheduler which will reduce
        # as a function of the validation distance
        patience = self.config.opt('optimization/validation_patience', 20)
        self.scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer,
            mode='min',
            factor=0.5,
            patience=patience,
            threshold=1e-3,
            min_lr=1e-8,
            verbose=True)

        # data locations
        datadir = self.config.opt('data/directory')

        # 
        validation_info = ds.system.read_list_to_column_dict(self.config.opt('data/validation'))
        self.validation_subjects = [os.path.join(datadir, p) for p in validation_info['path']]

        # 
        training_info = ds.system.read_list_to_column_dict(self.config.opt('data/training'))
        self.training_subjects = [os.path.join(datadir, p) for p in training_info['path']]
        self.validation_subject_images = validation_info.get('image')
        
        # 
        self.training_probs = training_info.get('prob')
        if self.training_probs is not None:
            self.training_probs = np.asarray(self.training_probs, dtype=np.float32)
            self.training_probs /= np.sum(self.training_probs)

        # 
        self.subject_specific_images = False
        self.image_files = ['t1w.mgz', 't1w-bias-corrected.mgz', 't1w-normalized.mgz']

        # 
        if training_info.get('images') is not None:
            self.subject_specific_images = True
            self.image_files = [line.split(',') for line in training_info['images']]
            if self.validation_subject_images is None:
                ds.system.fatal('Validation subjects must have specific image files specified in '
                                'an `image` column when using subject-specific training images.')

        # 
        self.image_files = self.config.opt('data/images', self.image_files)
        if isinstance(self.image_files, str):
            self.image_files = [self.image_files]

        # the model doesn't support batch sizes greater than 1 yet so easier to
        # just ignore batches completely for now
        self.unbatched = True

        # 
        self.training_image_shape = self.config.opt('data/training_image_shape', (96, 144, 192))

        # 
        self.augmentation = self.config.opt('data/augmentation', None)
        self.mask_probability = self.config.opt('data/mask_probability', 0.0)

        # 
        self.synth_exvivo_probability = self.config.opt('data/synth_exvivo_probability', 0.0)
        self.synth_exvivo_hemi_probability = self.config.opt('data/synth_exvivo_hemi_probability', 0.0)

    def update_loss_weights(self, epoch):
        """
        """
        if self.current_epoch < self.stage_1_end:
            self.loss_weights = self.loss_weights_stage_1
        elif self.current_epoch < self.stage_2_end:
            self.loss_weights = self.loss_weights_stage_2
        else:
            self.loss_weights = self.loss_weights_stage_3

    def on_epoch_end(self, epoch):
        """
        """
        # update the lr if we just reached the end of the guided stage
        if epoch == self.stage_2_end:
            for param_group in self.optimizer.param_groups:
                param_group['lr'] = self.lr
        # update loss weights based on current stage
        self.update_loss_weights(epoch)

    def on_checkpoint_loaded(self, epoch):
        """
        """
        # set the lr based on the loaded stage
        if epoch >= self.stage_2_end:
            for param_group in self.optimizer.param_groups:
                param_group['lr'] = self.lr
        # update loss weights based on loaded stage
        self.update_loss_weights(epoch)

    def sample(self, index=None, hemi=None, include_faces=False):
        """
        """
        # sample random training subject
        if index is None:
            index = np.random.choice(len(self.training_subjects), p=self.training_probs)
        subj = self.training_subjects[index]

        # 
        files = self.image_files[index] if self.subject_specific_images else self.image_files
        filename = np.random.choice(files)
        image = sf.load_volume(f'{subj}/{filename}').conform(copy=False, orientation='LIA', dtype='float32',
                                                             voxsize=self.model.in_voxsize)

        # sample random cortical hemisphere
        if hemi is None:
            hemi = np.random.choice(['lh', 'rh'])

        # 
        exterior = sf.load_mesh(f'{subj}/cortex-ext-{hemi}.srf').convert(space='image', geometry=image)

        # 
        cropping = sf.slicing.coords_to_slicing(exterior.bbox())

        # 
        bbox_shape = np.asarray(sf.slicing.slicing_shape(cropping))
        if np.any(bbox_shape > self.training_image_shape):
            ds.system.fatal(f'The cortical bounding box for subject {subj} exceeds the training image shape.'
                            f'\ncortical bounding box: {tuple(bbox_shape)}'
                            f'\ntraining image shape: {tuple(self.training_image_shape)}')

        # 
        cropping = sf.slicing.fit_slicing_to_shape(cropping, image.baseshape, self.training_image_shape)
        image = image[cropping].reshape(self.training_image_shape)

        # 
        if hemi == 'rh':
            image = image.reorient('RIA')

        # 
        exterior = exterior.convert(space='image', geometry=image)

        # load the remaining resampled white matter surface and precomputed affine template alignment
        interior = sf.load_mesh(f'{subj}/cortex-int-resampled-to-template-{hemi}.srf').convert(space='image', geometry=image)
        affine = sf.load_affine(f'{subj}/cortex-template-alignment-{hemi}.lta').convert(space='image', target=image)

        # 
        ext_vertices = exterior.vertices
        if exterior.nvertices < interior.nvertices:
            selected = np.random.randint(exterior.nvertices, size=interior.nvertices - exterior.nvertices)
            ext_vertices = np.concatenate([ext_vertices, ext_vertices[selected]])
        ext_vertices = ext_vertices[:interior.nvertices]

        # 
        mask = None
        if voxynth.chance(self.mask_probability):
            mask = ds.preprocess.load_brain_mask(subj,
                synth_exvivo_probability=self.synth_exvivo_probability,
                synth_exvivo_hemi_probability=self.synth_exvivo_hemi_probability,
                synth_exvivo_hemi=hemi).resample_like(image, method='nearest')

        # make a copy of the augmentation parameters so we can modify them if necessary
        augmentation = self.augmentation.copy() if self.augmentation is not None else None

        # convert the volume to a tensor, but if it's a map of tissue densities for synthesis,
        # we need to convert it to a valid image first (disable auto-normalization for this)
        if 'synth-densities' in filename:
            image = ds.normalize.framed_array_to_tensor(image)
            image = voxynth.synth.densities_to_image(image).to(self.device)
            augmentation['normalize'] = False
        else:
            image = ds.normalize.framed_array_to_tensor(image, device=self.device)

        # augment image intensities - no spatial transforming necessary
        if augmentation is not None:
            mask = ds.normalize.framed_array_to_tensor(mask, device=self.device).squeeze(0) if mask is not None else None
            image = voxynth.augment.image_augment(image=image, mask=mask, **augmentation)

        sample = {
            'image': image,
            'interior': torch.tensor(interior.vertices, dtype=torch.float32),
            'exterior': torch.tensor(ext_vertices, dtype=torch.float32),
            'affine': torch.tensor(affine.matrix, dtype=torch.float32),
        }

        if include_faces:
            # TODO: if hemi is the right hemisphere, need to flip the face ordering
            # maybe this should be built into the surfa mesh convert method somehow
            sample['interior_faces'] = interior.faces
            sample['exterior_faces'] = exterior.faces

        return sample

    def inspect(self):
        """
        """
        index = self.config.opt('data/inspection_index', 0)
        hemi = self.config.opt('data/inspection_hemi', 'rh')

        fv = sf.vis.Freeview()
        for i in range(10):
            sample = self.sample(index=index, hemi=hemi, include_faces=True)
            image = sf.Volume(sample['image'].cpu().movedim(0, -1).numpy())
            fv.add_image(image, name=f'image-{i + 1}')

        interior = sf.Mesh(sample['interior'], sample['interior_faces'], space='image', geometry=image)
        exterior = sf.Mesh(sample['exterior'], sample['exterior_faces'], space='image', geometry=image)
        fv.add_mesh(interior, edgecolor='pink', name='interior')
        fv.add_mesh(exterior, edgecolor='white', name='exterior')
        fv.show()

    def step(self, sample):
        """
        """
        # 
        skip = 1 if self.current_epoch < self.skipped_hires_epochs else 0

        # 
        outputs = self.model(sample['image'], sample['affine'], skip=skip)

        # 
        int_pred = outputs['interior']
        ext_pred = outputs['exterior']
        
        # 
        topology = outputs['topology']
        faces = topology.faces
        face_adjacency = topology.face_adjacency
        
        # 
        int_true = sample['interior']
        ext_true = sample['exterior']

        # 
        int_true = int_true[:topology.nv]

        # 
        losses = {
            'Int One-To-One': torch.mean((int_true - int_pred) ** 2),
            'Int Hinge': torch.mean(ds.surf.mesh.hinge_distances(int_pred, faces, face_adjacency, square=True)),
            'Ext Hinge': torch.mean(ds.surf.mesh.hinge_distances(ext_pred, faces, face_adjacency, square=True)),
        }

        # 
        if self.loss_weights.get('Int Chamfer') is not None:
            losses['Int Chamfer'] = torch.mean(ds.surf.mesh.chamfer_distances(int_true, int_pred, square=True))

        # 
        if self.loss_weights.get('Ext Chamfer') is not None:
            losses['Ext Chamfer'] = torch.mean(ds.surf.mesh.chamfer_distances(ext_true, ext_pred, square=True))

        return losses

    def validate(self):
        """
        """
        int_distances = []
        ext_distances = []
        int_intersections = []
        ext_intersections = []

        # loop over validation subjects and both hemispheres
        for n, subj in enumerate(self.validation_subjects):
            for hemi in ('lh', 'rh'):

                if self.validation_subject_images is not None:
                    filename = self.validation_subject_images[n]
                else:
                    filename = self.image_files[0]

                # 
                image = sf.load_volume(f'{subj}/{filename}')
                int_true = sf.load_mesh(f'{subj}/cortex-int-{hemi}.srf')
                ext_true = sf.load_mesh(f'{subj}/cortex-ext-{hemi}.srf')

                # should always be LH (or anything)
                affine = sf.load_affine(f'{subj}/cortex-template-alignment-{hemi}.lta')

                # 
                if hemi == 'rh':
                    affine = sf.Affine(affine @ self.model.left2right.inv(),
                        space='world',
                        source=self.model.template_mesh,
                        target=image)

                # 
                surfaces = self.model.estimate(image, affine, hemi)
                int_pred = surfaces['interior']
                ext_pred = surfaces['exterior']

                # 
                outdir = f'{self.basedir}/validation/{n+1}-{os.path.basename(subj)}'
                os.makedirs(outdir, exist_ok=True)
                image.save(f'{outdir}/image.mgz')
                int_pred.save(f'{outdir}/cortex-int-pred-{hemi}.srf')
                int_true.save(f'{outdir}/cortex-int-true-{hemi}.srf')
                ext_pred.save(f'{outdir}/cortex-ext-pred-{hemi}.srf')
                ext_true.save(f'{outdir}/cortex-ext-true-{hemi}.srf')

                # compute interior distance and intersection metrics
                int_distances.append(sf.mesh.surface_distance(int_true, int_pred))
                int_distances.append(sf.mesh.surface_distance(int_pred, int_true))
                int_intersections.append(len(int_pred.find_self_intersecting_faces()))

                # compute exterior distance and intersection metrics
                ext_distances.append(sf.mesh.surface_distance(ext_true, ext_pred))
                ext_distances.append(sf.mesh.surface_distance(ext_pred, ext_true))
                ext_intersections.append(len(ext_pred.find_self_intersecting_faces()))

        # return some metrics - these will be logged and used to decay LR
        int_distances = np.concatenate(int_distances)
        ext_distances = np.concatenate(ext_distances)
        combined_distances = np.concatenate([int_distances, ext_distances])
        result = {
            'Mean Int Distance': np.mean(int_distances),
            'Mean Ext Distance': np.mean(ext_distances),
            'Mean Combined Distance': np.mean(combined_distances),
            '95-P Int Distance': np.percentile(int_distances, 95),
            '95-P Ext Distance': np.percentile(ext_distances, 95),
            '95-P Combined Distance': np.percentile(combined_distances, 95),
            '99-P Int Distance': np.percentile(int_distances, 99),
            '99-P Ext Distance': np.percentile(ext_distances, 99),
            '99-P Combined Distance': np.percentile(combined_distances, 99),
            'Int Intersections': np.mean(int_intersections),
            'Ext Intersections': np.mean(ext_intersections),
        }

        # 
        if self.current_epoch > self.scheduler_starting_epoch:
            self.scheduler.step(result['95-P Combined Distance'])

        return result


def validate_training_subjects(config_file, reference_image='t1w.mgz'):
    """
    Utility that validates each training subject by checking whether
    the pial surface exceeds the bounds of the training image shape.
    Invalid subjects should be excluded from training.
    """
    config = ds.config.load_config(config_file)
    datadir = config.opt('data/directory')
    training_file = config.opt('data/training')
    training_info = ds.system.read_list_to_column_dict(config.opt('data/training'))
    training_subjects = [os.path.join(datadir, p) for p in training_info['path']]
    training_image_shape = config.opt('data/training_image_shape', (96, 144, 192))  # TODO: move the default as a global variable

    for subj in training_subjects:
        for hemi in ('lh', 'rh'):
            geometry = sf.load_volume(f'{subj}/{reference_image}').reorient('LIA').geom
            exterior = sf.load_mesh(f'{subj}/cortex-ext-{hemi}.srf').convert(space='image', geometry=geometry)
            cropping = sf.slicing.coords_to_slicing(exterior.bbox())
            bbox_shape = np.asarray(sf.slicing.slicing_shape(cropping))
            if np.any(bbox_shape > training_image_shape):
                print(f'invalid: {subj} surface exceeds training image shape, has bounds {bbox_shape}')


def load_topofit_model(device, version='beta-5', modelfile=None):
    """
    Load the default topofit model.
    """
    if modelfile is not None:
        print(f'Using custom model weights from {modelfile}')
    else:
        modelfile = ds.system.resource(f'models/topofit-{version}.pt')
    return ds.io.load_model(modelfile, device=device, expected=TopoFitModel)


def command():
    """
    The surface reconstruction subcommand, which can be run directly from the command line.
    """
    description = '''
    Estimate the interior (white-matter) and exterior (pial) cortical surfaces from a
    T1-weighted image. The input image does not need to be pre-processed in any way.

    <DIM>TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces<BR>
    <DIM>Andrew Hoopes, Juan Eugenio Iglesias, Bruce Fischl, Douglas Greve, Adrian Dalca<BR>
    <DIM>MIDL: Medical Imaging with Deep Learning. 2022.
    '''
    epilog = '''
    Command line input and output files can be configured a few different ways. Since this tool
    will produce multiple outputs, it is necessary to specify the desired IO format using the --io
    flag. The allowed IO formats are:

    - fs: FreeSurfer directory structure. The output directory mirrors a standard FreeSurfer subject,
    and outputs are saved in the corresponding recon-style files formats.
    - si: All files are written to a single output directory using nifti compatible file formats.

    For example, to quickly fit surfaces to a single image, the input image, output directory, and
    output format can be specified like:

    <DIM>ds fit-cortex --image image.nii.gz --out processed --io si

    To efficiently run the model on multiple images, you can provide a two-column text file as input
    using the --list flag. This file is expected to contain a pair of image and output directory paths
    on each row. For example:

    <DIM>/path/to/image-01.nii.gz /path/to/output-directory-01
    <DIM>/path/to/image-02.nii.gz /path/to/output-directory-02

    This multi-image approach is recommended if you’re using a GPU, since it will avoid repeating a
    time-consuming initialization on the device.
    '''
    parser = ds.system.SubcommandParser(description=description, epilog=epilog)
    # single-input processing
    single = parser.add_argument_group('Single-Image Processing')
    single.add_argument('-i', '--image', metavar='file', help='Input image (for single-image processing).')
    single.add_argument('-o', '--outdir', metavar='dir', help='Output directory (for single-image processing).')
    # multi-input processing
    multi = parser.add_argument_group('Multi-Image Processing')
    multi.add_argument('--list', metavar='file', help='Input list for multi-image processing. See below for examples.')
    # other options (help flag will be added automatically)
    parser.add_argument('--io', metavar='format', required=True, help='IO format type.')
    parser.add_argument('--hemi', metavar='L/R', help='Reconstruct only a single hemisphere.')
    parser.add_argument('--cpu', action='store_true', help='Force CPU usage when GPU is available.')
    parser.add_argument('--threads', type=int, help='Number of CPU threads. Default is max available.')
    parser.add_argument('--debug', action='store_true', help='View debugging information.')
    parser.add_argument('--model', metavar='file', help='Alternative model file to load.')
    parser.add_argument('--suffix', metavar='suffix', help='Optional suffix to append to output filenames.')
    parser.add_argument('--no-cite', action='store_true', help='Remove that pesky citation request.')
    args = parser.parse_args()

    # parse the docket of images to process
    docket = ds.system.parse_io_docket(
        parser=parser,
        listed_columns=['image_input', 'output_directory'],
        single_input_args=['image', 'outdir'],
    )

    # sanity check when specifying individual hemispheres
    hemispheres = ['lh', 'rh']
    if args.hemi is not None:
        hemi_code = args.hemi[0].lower()
        if hemi_code not in ('l', 'r'):
            ds.system.fatal(f'Unknown --hemi option \'{args.hemi}\'. Must be \'L\' or \'R\'.')
        side = 'left' if hemi_code == 'L' else 'right'
        print(f'Reconstructing only the {side} hemisphere')
        hemispheres = [f'{hemi_code}h']

    # filename suffix
    suffix = args.suffix if args.suffix is not None else ''

    # configure torch device
    device = ds.device.configure_device(cpu=args.cpu, threads=args.threads, verbose=True)

    # initialize the template alignment model
    aligment_model = load_alignment_model(device=device)

    # initialize the topofit model
    topofit_model = load_topofit_model(device=device, modelfile=args.model)

    # loop through our inputs
    for item in docket:

        # load input volume
        filename = item['image_input']
        image = sf.load_volume(filename)
        print(f'Processing input image {filename}')

        # first we compute the affine alignment from the template space to the image
        # in order to place the initial surface mesh
        affines = aligment_model.estimate(image, debug=args.debug)

        # loop over hemispheres
        for hemi in hemispheres:

            # predict the surfaces using the hemi-specific affines as initializations (probably overkill)
            surfaces = topofit_model.estimate(image, affines[hemi], hemi=hemi)

            outdir = item['output_directory']
            if outdir is not None:
                os.makedirs(outdir, exist_ok=True)
                if args.io == 'fs':
                    # save the surfaces in freesurfer format
                    surfaces['interior'].save(os.path.join(outdir, f'{hemi}.white{suffix}'))
                    surfaces['exterior'].save(os.path.join(outdir, f'{hemi}.pial{suffix}'))
                elif args.io == 'si':
                    # save the surfaces in the si format
                    surfaces['interior'].save(os.path.join(outdir, f'cortex-int-{hemi}{suffix}.srf'))
                    surfaces['exterior'].save(os.path.join(outdir, f'cortex-ext-{hemi}{suffix}.srf'))
                else:
                    raise ValueError(f'Unknown IO format \'{args.io}\'')

    if not args.no_cite:
        print('If you use this tool in your analysis, please cite:')
        print('Hoopes et al. "TopoFit: Rapid Reconstruction of Topologically-Correct Cortical Surfaces" MIDL (2022)')
