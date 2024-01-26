import sys
import re
import platform
import textwrap


# terminal color codes
colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'underline': '\033[4m',
    'dim': '\033[2m',
    'bold': '\033[1m',
    'end': '\033[0m',
}

# check if tty allows colors
istty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
colors_enabled = istty and platform.system() in ('Darwin', 'Linux')

# clear all color codes if they're not enabled
if not colors_enabled:
    colors = dict.fromkeys(colors, '')

# temporary function to dynamically create string-wrapping methods
def mkmethod(name, code):
    def wrapstring(string):
        return ''.join((str(code), string, colors['end']))
    return wrapstring

# create the color methods and remove the temporary variables
for color, code in colors.items():
    vars()[color] = mkmethod(color, code)
del color, code, mkmethod


def formatted(text, width=80, preface=None, indent=None):
    """
    Format command line text to remove extra spaces and limit
    within a specific width. Enables a few modifers as well:

    <BR>  Used to force a newline without initiating a new paragraph.
    <DIM> Used at the start of a line to dim it.

    Parameters
    ----------
    text : str
        Text to format.
    width : int
        Max column width for each line.
    preface : str
        Prefacing text that will not be indented.
    indent : int
        Indentation length.

    Returns
    -------
    str
        The formatted text.
    """
    sdt = ' ' * indent if indent is not None else ''
    idt = sdt[:-len(preface)] if preface is not None else sdt
    text = re.sub(' +', ' ', re.sub('(?<!\n)\n(?!\n)', '', text))
    
    # make sure to account for single-line breaks
    text = text.replace('<BR>', '\n')
    
    # text wrap each individual line
    lines = [textwrap.fill(s.strip(), width=width, initial_indent=idt, subsequent_indent=sdt) for s in text.splitlines()]
    
    # dim any lines that start with <DIM>
    dim_block = lambda x : dim(x.replace('<DIM>', '')) if '<DIM>' in x else x
    lines = [dim_block(line) for line in lines]
    
    # rejoin text block
    text = '\n'.join(lines)
    if preface is not None:
        text = preface + text
    return text
