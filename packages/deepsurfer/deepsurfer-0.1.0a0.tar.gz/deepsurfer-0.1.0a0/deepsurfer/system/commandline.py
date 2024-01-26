import os
import re
import sys
import platform
import argparse
import textwrap
import importlib

from collections import namedtuple

from . import parse


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        How to add a subcommand
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any tool added below via 'addcmd' will be automatically configured as a valid
deepsurfer subcommand and will be listed in the base help text. Make sure that
each entry is organized into the appropriate category and is initialized with a
short subcommand name, function call, and brief help text.

function usage: addcmd(cmd, func, help)

    cmd:  The name of the subcommand.

    func: The internal function that each subcommand links to. A string is used
          to designate the function path so that all corresponding submodules can
          be loaded on the fly, which avoids slow imports during the initial
          command parsing.

          Sub-arguments can be automatically parsed with SubcommandParser, which
          is a subclass of argparse.ArgumentParser. Here's a function template
          using SubcommandParser:

          def processs_subcommand():
              parser = SubcommandParser(description='some cmd for doing stuff')
              parser.add_argument('input', help='input file')
              args = parser.parse_args()

    help: Short help text to print in the main deepsurfer help text. More details
          can be added to the subcommand-specific help text.

For a complete example of how this stuff in configured, take a look at the
skull-strip command defined below and the corresponding deepsurfer.strip.command()
function in modules/strip.py.
"""


# init the list of subcommands and define the functions that will add to this list
subcommands = []
subcmd = namedtuple('SubCommand', ('cmd', 'func', 'help'))
addcmd = lambda cmd, func, help: subcommands.append(subcmd(cmd, func, help))
addcat = lambda cat: subcommands.append(cat)


# -------------------------------------------------------------------
addcat('Volumetric Processing')
# -------------------------------------------------------------------

addcmd('skull-strip',
       func='modules.strip.command',
       help='Skull-strip non-brain matter (SynthStrip).')

addcmd('seg-sc-limbic',
       func='TODO: link this module',
       help='Segment subcortical limbic structures.')

addcmd('align-template',
       func='modules.aligntemplate.command',
       help='Roughly align cortical surface template to image.')

addcmd('brain-crop',
       func='modules.braincrop.command',
       help='Rapidly crop an image to a bounding-box around the brain.')

# -------------------------------------------------------------------
addcat('Cortical Surface Processing')
# -------------------------------------------------------------------

addcmd('fit-cortex',
       func='modules.topofit.command',
       help='Fit mesh surfaces to cortical tissue boundaries (TopoFit).')

addcmd('seg-cortex',
       func='TODO: link this module',
       help='Parcellate structures of the cortical surface.')

# -------------------------------------------------------------------
addcat('Development')
# -------------------------------------------------------------------

addcmd('train',
       func='training.command',
       help='Universal utility for training a model.')

addcmd('preprocess',
       func='preprocess.command',
       help='Preprocess a freesurfer subject for deepsurfer training.')

# -------------------------------------------------------------------
addcat('Miscellaneous')
# -------------------------------------------------------------------

addcmd('help',
       func='system.commandline.print_help_text',
       help='Print this help text and exit.')

# -------------------------------------------------------------------
# -------------------------------------------------------------------


def execute():
    """
    Parse the commandline inputs
    """

    # print help and error out if no subcommand is given
    if len(sys.argv) < 2:
        print_help_text()
        return 1

    # get the subcommand
    sc = sys.argv[1]

    # it's possible that a user might run --help, so we should check for this
    if sc.replace('-', '') == 'help':
        return print_help_text()

    # make sure that the given subcommand exists
    matched = next((s for s in subcommands if not isinstance(s, str) and s.cmd == sc), None)
    if matched is None:
        print(f"error: '{sc}' is not a known deepsurfer subcommand. Run "
               "'ds help' to output a list of available tools.")
        return 1

    # wrangle the complete module path to the subcommand function
    split = matched.func.split('.')
    submodules = '.'.join(split[:-1])
    module = 'deepsurfer.' + submodules

    # import the function from the specified module
    m = importlib.import_module(module)
    func = getattr(m, split[-1])

    # run the function and return its result
    retcode = func()
    if retcode is None:
        retcode = 0
    return retcode


def help_text_description():
    """
    Help text printed before the subcommand list.
    """
    text = '''
    Learning-based toolbox for brain MRI analysis.

    The collection of tools is described below. For more info on each of the
    available methods, append the --help flag to the corresponding subcommand,
    for example, 'ds skull-strip --help'.
    '''
    return text


def help_text_epilogue():
    """
    Help text printed after the subcommand list.
    """
    text = """
    Note that the methods implemented in this package are experimental and
    should not be used for formal analysis without substantial review
    of the outputs.

    For more information, visit the readme at github.com/freesurfer/deepsurfer.
    """
    return text


def print_help_text():
    """
    Print complete help text for the base deepsurfer command.
    """

    # print the command usage and introduction
    print(parse.bold('USAGE:'), 'ds <subcommand> [options]\n')
    print(parse.formatted(help_text_description()))
    
    # cycle through each subcommand and print its help text
    for s in subcommands:

        if isinstance(s, str):
            print(f'\n{parse.bold(s.upper())}')
        else:
            print(parse.formatted(s.help, preface=s.cmd, indent=20))

    # print the epilogue
    print()
    print(parse.formatted(help_text_epilogue()))
