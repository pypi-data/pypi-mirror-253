# DeepSurfer
DeepSurfer is a deep-learning toolbox for analysis of human brain MRI

**AH:** Probably good to keep this as a private repo until we decide on how we want to use this library or if we want to rename it / move it somewhere else etc. I'm still making updates, mainly to the surface related stuff as I try to finish the TopoFit paper, but definitely feel free to make changes or extensions as you see fit. I'll try to update documentation as I go along.

## Overview

This package aims to 1. avoid the plague of code redundancy for building and training models and 2. make it easier to actually distribute these tools to users who don't care about the underlying implementation. It's all built on top of pytorch, which also makes things super easy to deploy.

**Usage:** From a user standpoint, utilities/models are accessible through the `ds` command, which should be added to the user's path whenever deepsurfer is installed through pip (in the future ideally). Similar to how git is organized, the `ds` command is a base command that can be followed by a subcommand to access a specific tool. For example, `ds train` will train a model, `ds skull-strip` will run the skull-stripping inference, etc. The `ds` command is a small executable at the top-level directory, so to get an idea of how it works, run:

```bash
./ds help
```

## Installation

It's not on PyPi or anything yet. The only non-standard dependencies are `torch >= 1.12`, `surfa >= 0.5.0`, `scipy`, and `pyyaml`, and the current python requirement is at least 3.7. No other steps should be necessary for running inference at this point, but if you want to actually train models, see the notes below.

**Training:** All of the models that I've implemented so far build on the [voxsynth](https://github.com/dalcalab/voxynth) library for image synthesis and augmentation. That's also not on pip (yet), but you can clone it from that link. It doesn't have any crazy dependencies, and it's only required for training.

**TopoFit:** If you want to train a TopoFit model, you'll have to build the nearest-neighbor CUDA extension to speed up the optimization. It should be relatively easy if you use conda, but there are a few specific steps that need to be run -- outlined in the docstring of [this function](https://github.com/freesurfer/deepsurfer/blob/1e1ad53a9adbc4c5e420c54c30eee4bd51bc0a89/deepsurfer/extension/extension.py#L27C17-L27C17).

## Documentation

I started info-dumping everything into a single page but realized it just makes more sense to organize a bit. I copied the template I used for the surfa website into the `docs/` subdirectory. It uses sphinx, which is a markdown-style documentation framework that renders to html. It's a pretty common doc method in the python world. Anyway, I set up a temporary auto-build [here](https://surfer.nmr.mgh.harvard.edu/fstest/dstmp) (you can't view it without an nmr account). So far I wrote an overview of how to use each tool, along with some development documentation, but for now the site is 50% just placeholder stuff as a potential outline for public facing documentation. We can always change or ditch it, but it also might be a good way to host relevant paper pages.
