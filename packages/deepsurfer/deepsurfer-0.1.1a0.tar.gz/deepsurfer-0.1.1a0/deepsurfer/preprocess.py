import os
import shutil
import numpy as np
import surfa as sf
import torch

from . import system


def command():
    """
    Command line utility for preprocessing a freesurfer recon subject for training
    various deepsurfer tools. All of the preprocessed data will be saved to the `dsprep`
    subdirectory of the freesurfer subject.
    """
    description = '''
    Preprocess a freesurfer subject for training of various deepsurfer models.

    All preprocessed outputs will be saved to the `dsprep` subdirectory of the
    freesurfer subject. Individual preprocessing components can be specified via
    the flags described below, but it is generally best to use the --all flag to
    run all of the preprocessing components at once. Note that this can take an hour
    or more per subject.
    '''
    parser = system.SubcommandParser(description=description)
    parser.add_argument('subj', metavar='DIR', help='Path to a processed freesurfer recon subject directory.')
    parser.add_argument('outdir', metavar='DIR', help='Directory to save preprocessed outputs to.')
    parser.add_argument('--all', action='store_true', help='Run all of the preprocessing components.')
    parser.add_argument('--img-copy', action='store_true', help='Run image copying steps.')
    parser.add_argument('--img-seg', action='store_true', help='Run whole brain segmentation using synthseg.')
    parser.add_argument('--img-crop', action='store_true', help='Compute cropping and orientation segmentation.')
    parser.add_argument('--img-mask', action='store_true', help='Run brain masking steps.')
    parser.add_argument('--synth-density', action='store_true', help='Compute rough tissue densities using samseg.')
    parser.add_argument('--synth-density-source', default='t1w', help='Source for the tissue density creation. Default is t1w.')
    parser.add_argument('--surf-resample', action='store_true', help='Run the cortical surface resampling steps.')
    parser.add_argument('--surf-seg', action='store_true', help='Run the cortical surface segmentation steps.')
    args = parser.parse_args()

    # configure the subject path and ensure that SUBJECTS_DIR is configured properly
    subj = os.path.abspath(args.subj)
    prepdir = os.path.abspath(args.outdir)
    tmpdir = os.path.join(prepdir, 'tmp')
    subjects_dir = os.path.dirname(subj)
    os.environ['SUBJECTS_DIR'] = subjects_dir
    basename = os.path.basename(subj)

    # check input subject
    if not os.path.isdir(subj):
        system.fatal(f'{subj} is not a valid freesurfer subject directory')

    # initialize the output directories
    if os.path.isdir(tmpdir):
        shutil.rmtree(tmpdir)
    os.makedirs(prepdir, exist_ok=True)
    os.makedirs(tmpdir, exist_ok=True)

    # make sure FS has been sourced in the env (check for mris_register since we'll need it anyway)
    if shutil.which('mris_register') is None:
        system.fatal('Cannot find freesurfer commands in the system path, has freesurfer '
                     'been properly sourced?')

    if args.all or args.img_copy:
        # copy useful image data into output directory
        shutil.copy(f'{subj}/mri/orig.mgz', f'{prepdir}/t1w.mgz')
        shutil.copy(f'{subj}/mri/nu.mgz', f'{prepdir}/t1w-bias-corrected.mgz')
        shutil.copy(f'{subj}/mri/norm.mgz', f'{prepdir}/t1w-normalized.mgz')

    if args.all or args.img_seg:
        # run synthseg since it's a good way to get a solid brainmask and CSF labels
        system.run(f'mri_synthseg --cpu --robust --i {subj}/mri/orig.mgz --o {prepdir}/seg-wb.mgz')
        sf.load_volume(f'{prepdir}/seg-wb.mgz').astype(np.uint8).save(f'{prepdir}/seg-wb.mgz')

    if args.all or args.img_crop:

        # load whole brain segmentation
        synthseg = sf.load_volume(f'{prepdir}/seg-wb.mgz')

        # an 'orienting seg' is an extremely coarse segmentation of general midline regions,
        # brain matter, and CSF which can be used to train an 'orienting' cropping model,
        # i.e. a model that can crop the image as well as rapidly determine the anatomical
        # orientation of the image data without relying on any header matrix information
        tissue_mask = (synthseg > 0).astype('uint8')
        orienting_seg = sf.load_volume(system.resource('template/orienting-seg.mgz'))
        template_aff = sf.load_affine(f'{subj}/mri/transforms/talairach.lta').inv()
        orienting_seg = orienting_seg.transform(template_aff, method='nearest')
        tissue_mask[tissue_mask > 0] += orienting_seg.max()
        within_tissue = (orienting_seg > 0) & (tissue_mask > 0)
        tissue_mask[within_tissue] = orienting_seg[within_tissue]
        tissue_mask.save(f'{prepdir}/orienting-tissue-mask.mgz')

    if args.all or args.img_mask:

        # now we'll build a single segmentation that encodes a series of masks (all saved
        # within a single segmentation). this segmentation includes hemi-specific brain masks,
        # cerebellum masks, an extra-cerebral tissue mask, and a brainstem mask.
        system.run(f'mri_synthstrip -i {subj}/mri/orig.mgz -m {tmpdir}/tissue-mask.mgz --no-csf -b 1')
        tissue_mask = (sf.load_volume(f'{tmpdir}/tissue-mask.mgz') > 0).astype(np.uint8)
        for _ in range(8):
            tissue_mask += (tissue_mask > 0).dilate(1)
        tissue_mask = -(tissue_mask - tissue_mask.max())
        tissue_mask += 6
        aseg = sf.load_volume(f'{subj}/mri/aseg.mgz')
        nocc = sf.load_volume(f'{subj}/mri/aseg.auto_noCCseg.mgz')
        merge = lambda m, labels : m.new(np.isin(m, labels)).connected_component_mask(fill=True)
        # replace the aseg CC labels with WM labels from the no-CC segmentation
        cc = np.isin(aseg, [251, 252, 253, 254, 255])
        aseg[cc] = nocc[cc]
        # brainstem and cerebellum masks
        tissue_mask[merge(aseg, [7, 8])] = 3
        tissue_mask[merge(aseg, [46, 47])] = 4
        tissue_mask[np.isin(aseg, [15, 16])] = 5
        # merge labels to get hemi-specific brain masks
        hemi = [2, 3, 4, 5, 10, 11, 12, 13, 17, 18, 26, 28, 30, 31, 77]
        tissue_mask[merge(aseg, hemi)] = 1
        hemi = [41, 42, 43, 44, 49, 50, 51, 52, 53, 54, 58, 60, 62, 63, 77]
        tissue_mask[merge(aseg, hemi)] = 2
        tissue_mask.save(f'{prepdir}/masks.mgz')

    if args.all or args.synth_density:
        # computing some general tissue densities is useful for more realistic image synthesis
        # during training. the densities don't need to accurately represent any particular set of
        # tissue classes (they don't) as long we they can be used to generate somewhat realistic
        # images with variable intensity contrast. the probabilities chosen below seem to produce
        # the best-looking results, but they don't really have any particular quantitative value
        system.run(f'run_samseg --save-probabilities -i {prepdir}/{args.synth_density_source}.mgz -o {tmpdir}/samseg')
        probdir = f'{tmpdir}/samseg/probabilities'
        frame = 2
        frames = [
            sf.load_volume(f'{probdir}/GlobalCSF_clean.mgz') + sf.load_volume(f'{probdir}/GlobalCSF_messy.mgz'),
            sf.load_volume(f'{probdir}/Soft-1.mgz'),
            sf.load_volume(f'{probdir}/Soft-2.mgz')]
        density = sf.stack([f[..., frame] for f in frames])
        totals = np.sum(density, axis=-1)
        mask = totals > 0
        density[mask] /= totals[mask, None]
        density.save(f'{prepdir}/{args.synth_density_source}-synth-densities.mgz')

    if args.all or args.surf_resample:

        # we want to resample the subject surfaces of both hemispheres to match the mesh
        # topology of our predefined template surface. this is necessary for training topofit
        # models, which rely partially on target surfaces with one-to-one correspondence for
        # each vertex (this is mostly for training stability). for both hemispheres we will use
        # the left hemisphere of the template, since the right template surface is just a linear
        # transformation of the left anyway
        target_reg = sf.load_mesh(system.resource('template/sphere-reg.srf'))
        atlas = system.resource('template/folding-atlas.tif')
        template = sf.load_mesh(system.resource('template/cortex-int-lh.srf'))

        # cycle across hemispheres
        for hemi in ('lh', 'rh'):

            # copy the original surfaces
            shutil.copy(f'{subj}/surf/{hemi}.white', f'{prepdir}/cortex-int-{hemi}.srf')
            shutil.copy(f'{subj}/surf/{hemi}.pial', f'{prepdir}/cortex-ext-{hemi}.srf')

            # first step is to spherically register the white matter surfaces to the template
            # surface. if working with the right hemisphere, make sure to flip over the first
            # axis so that the anatomy aligns correctly
            source_sphere = sf.load_mesh(f'{subj}/surf/{hemi}.sphere')
            source_smoothwm = sf.load_mesh(f'{subj}/surf/{hemi}.smoothwm')
            if hemi == 'rh':
                source_sphere.vertices   *= (-1, 1, 1)
                source_smoothwm.vertices *= (-1, 1, 1)
            source_sphere.save(f'{tmpdir}/{hemi}.sphere')
            source_smoothwm.save(f'{tmpdir}/{hemi}.smoothwm')
            shutil.copyfile(f'{subj}/surf/{hemi}.sulc', f'{tmpdir}/{hemi}.sulc')
            system.run(f'mris_register -curv {tmpdir}/{hemi}.sphere {atlas} {prepdir}/src-sphere-reg-{hemi}.srf')

            # once we have the spherical registration, we can resample the subject surfaces to the
            # mesh space of the template using a spherical barycentric resampling
            source_wms = sf.load_mesh(f'{subj}/surf/{hemi}.white')
            source_reg = sf.load_mesh(f'{prepdir}/src-sphere-reg-{hemi}.srf')
            vertices = sf.sphere.SphericalResamplingBarycentric(source_reg, target_reg).sample(source_wms.vertices)
            resampled = sf.Mesh(vertices, target_reg.faces, geometry=source_wms.geom)
            resampled.save(f'{prepdir}/cortex-int-resampled-to-template-{hemi}.srf')

            # since we have a one-to-one correspondence between the subject's white matter surface
            # and template surface, we can do a simple least-squares regression to compute an
            # linear alignment between the template and subject cortex. we can use this
            # for training a cortical template-alignment model for both hemispheres
            resampled = sf.load_mesh(f'{prepdir}/cortex-int-resampled-to-template-{hemi}.srf')
            X = np.concatenate([template.vertices, np.ones((template.nvertices, 1))], axis=-1)
            Y = np.concatenate([resampled.vertices, np.ones((resampled.nvertices, 1))], axis=-1)
            B = (np.linalg.inv((X.T @ X) + np.eye(X.shape[1])) @ X.T) @ Y
            affine = sf.Affine(B.T, space='surf', source=template.geom, target=resampled.geom).convert(space='world')
            affine.save(f'{prepdir}/cortex-template-alignment-{hemi}.lta')

    if args.all or args.surf_seg:

        #  here we transfer cortical parcellation maps to the resampled surface space

        target_reg = sf.load_mesh(system.resource('template/sphere-reg.srf'))

        parcellations = [
            ['', 'dk'],
            ['.a2009s', 'dsx'],
            ['.DKTatlas', 'dkt']]

        for hemi in ('lh', 'rh'):

            source_wms = sf.load_mesh(f'{subj}/surf/{hemi}.white')
            source_reg = sf.load_mesh(f'{prepdir}/src-sphere-reg-{hemi}.srf')
            interp = sf.sphere.SphericalResamplingNearest(source_reg, target_reg)
            
            for a, b in parcellations:
                source_labels = sf.load_overlay(f'{subj}/label/{hemi}.aparc{a}.annot')
                interp.sample(source_labels).save(f'{prepdir}/parc-{b}-{hemi}.annot')

            v = sf.io.fsio.load_surface_label(f'{subj}/label/{hemi}.cortex.label')
            mask = np.zeros(source_wms.nvertices, dtype=np.uint8)
            mask[v] = 1
            interp.sample(mask).save(f'{prepdir}/cortex-mask-{hemi}.mgz')

    # delete temporary directory
    shutil.rmtree(tmpdir)


def load_brain_mask(
    subj,
    synth_exvivo_probability=0.0,
    synth_exvivo_hemi_probability=0.0,
    synth_exvivo_hemi=None):
    """
    Load and generate a brain mask for a preprocessed subject. The resulting mask will be
    an arbitrary distance from the brain tissue.

    Parameters
    ----------
    subj : str
        The preprocessed subject directory.
    synth_exvivo_probability : float
        The probability of synthesizing an ex-vivo-like brain mask in which the cerebellum
        and brainstem are randomly removed.
    synth_exvivo_hemi_probability : float
        The probability of including only a single hemisphere in the ex-vivo-like brain mask.
        This is a sub-probability of `synth_exvivo_probability`, so the total probability of
        synthesizing a single-hemisphere ex-vivo-like brain mask is the product of these two.
    synth_exvivo_hemi : {'lh', 'rh', None}
        The hemisphere to include in the ex-vivo-like brain mask if `synth_exvivo_hemi_probability`
        is greater than zero. If `None`, the hemisphere will be randomly selected.

    Returns
    -------
    mask : sf.Volume
        The generated binary brain mask (of type bool).
    """
    masks = sf.load_volume(f'{subj}/masks.mgz')

    if np.random.rand() < synth_exvivo_probability:

        # if we end up sampling a hemi-specific ex-vivo mask, figure
        # out which hemisphere we're going to use
        hidx = None
        if np.random.rand() < synth_exvivo_hemi_probability:
            if synth_exvivo_hemi is None:
                hidx = np.random.randint(2)
            elif synth_exvivo_hemi[0].lower() == 'l':
                hidx = 0
            elif synth_exvivo_hemi[0].lower() == 'r':
                hidx = 1
            else:
                raise ValueError(f'invalid hemisphere {hemi}')

        # compute mask labels for both hemispheres
        cerebrum = [1, 2]
        cerebellum = [3, 4]

        # if we're only using one hemisphere, remove the other labels
        if hidx is not None:
            cerebrum = [cerebrum[hidx]]
            cerebellum = [cerebellum[hidx]]

        # definitely include the cerebrum
        matches = cerebrum

        # optionally include the cerebellum
        if np.random.rand() < 0.5:
            matches.extend(cerebellum)

        # optionally include the brainstem
        if np.random.rand() < 0.5:
            matches.append(5)

        # optionally include the outer brain mask shell
        if np.random.rand() < 0.5:
            matches.append(6)

        return masks.new(np.isin(masks, matches))

    else:
        # otherwise, return the original mask with an arbitrary distance
        return masks < np.random.randint(8, 16)
