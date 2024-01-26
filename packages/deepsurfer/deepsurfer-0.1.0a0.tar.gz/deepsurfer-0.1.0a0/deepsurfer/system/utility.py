import os
import sys
import csv
import numpy as np
import importlib
import pathlib
import subprocess as sp
import shutil

from .formatting import red
from .formatting import yellow


def fatal(message, retcode=1):
    """
    Print error message and exit.

    Parameters
    ----------
    text : str
        Message to print before exiting.
    retcode : int
        System exit code.
    """
    print(f'{red("Error:")} {message}')
    sys.exit(retcode)


def warning(message):
    """
    Print warning message to the terminal. Note that is different from a python-style
    system warning and meant to warn the end user instead of developers.

    Parameters
    ----------
    text : str
        Warning message to print.
    """
    print(f'{yellow("Warning:")} {message}')


def error(message):
    """
    Print error message to the terminal

    Parameters
    ----------
    text : str
        Warning message to print.
    """
    print(f'{red("Error:")} {message}')


def import_member(fullname):
    """
    Import member from its full module namespace.

    Parameters
    ----------
    fullname : str
        Complete namespace, for example 'scipy.ndimage.convolve'.

    Returns
    -------
    class
        Loaded member.
    """
    split = fullname.split('.')
    module_name = '.'.join(split[:-1])
    module = importlib.import_module(module_name)
    ref = getattr(module, split[-1])
    return ref


def resource(path, check=True):
    """
    Get full path of a file stored in the resource subdirectory
    of the deepsurfer package.

    Parameters
    ----------
    path : str
        Relative path to file under the `resource` subdir.
    check : bool
        Raise a fatal error if the file does not exist.

    Returns
    -------
    str
        Full path to the resource item.
    """
    basepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(basepath, 'resource', path)
    if check and not os.path.exists(path):
        fatal(f'Resource item {path} does not exist in the deepsurfer package.')
    return path


def read_list(filename):
    """
    Load a text file into a list. Will read each row into a list of columns
    if the rows contain multiple space-seperated items.

    Parameters
    ----------
    filename : str
        Path to text file.

    Returns
    -------
    (list, int)
        The text list and the number of columns in each row.
    """
    rows = []
    ncolumns = None
    with open(filename, 'r') as file:
        for lineno, line in enumerate(file):
            line = line.strip()
            if line:
                row = line.split()
                if ncolumns is None:
                    ncolumns = len(row)
                if len(row) != ncolumns:
                    fatal(f'When parsing list \'{filename}\', found differing number of '
                          f'columns across rows. Row on line {lineno + 1} has {len(row)} '
                          f'entries, while previous rows have {ncolumns}.')
                if len(row) == 1:
                    row = row[0]
                rows.append(row)
    return rows, ncolumns


def read_list_to_column_dict(filename):
    """
    Load a whitespace-seperated list file into a column-wise dictionary.
    The first row (header) is used as the key.

    Parameters
    ----------
    filename : str
        Path to whitespace-seperated list file. Items can be seperated by
        any number of spaces.

    Returns
    -------
    dict
    """
    with open(filename, 'r') as file:
        keys = next(file).strip().split()
        rows = [line.strip().split() for line in file if line.strip()]
    return {key: [row[i] for row in rows] for i, key in enumerate(keys)}


def read_csv_to_column_dict(filename):
    """
    Load a comma-seperated value file into a column-wise dictionary.
    The first row (header) is used as the key.

    Parameters
    ----------
    filename : str
        Path to CSV file.

    Returns
    -------
    dict
    """
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        keys = next(reader)
        rows = list(reader)
    return {key: [row[i] for row in rows] for i, key in enumerate(keys)}


def run(command,
        silent=False,
        background=False,
        exit_on_failure=True,
        executable='/bin/bash',
        log=None):
    """
    Runs a shell command and returns the exit code.

    Parameters
    ----------
    command : str
        Command to run.
    silent : bool
        Send output to devnull.
    background : bool
        Run command as a background process.
    exit_on_failure : bool
        Fatal failure if return code is not zero.
    executable : str
        Shell executable. Defaults to bash.
    log : str
        Send output to a log file.

    Returns
    -------
    int
        Command exit code.
    """

    # redirect the standard output appropriately
    if silent:
        std = {'stdout': sp.DEVNULL, 'stderr': sp.DEVNULL}
    elif not background:
        std = {'stdout': sp.PIPE, 'stderr': sp.STDOUT}
    else:
        std = {}  # do not redirect

    # run the command
    process = sp.Popen(command, **std, shell=True, executable=executable)
    if not background:
        # write the standard output stream
        if process.stdout:
            for line in process.stdout:
                decoded = line.decode('utf-8')
                if log is not None:
                    with open(log, 'a') as file:
                        file.write(decoded)
                sys.stdout.write(decoded)
        # wait for process to finish
        process.wait()

    retcode = process.returncode
    if exit_on_failure and retcode != 0:
        fatal(f'Could not run command: {command}')

    return retcode


def submit_slurm_job(
        command,
        basepath,
        account,
        partition,
        time='7-00:00:00',
        mem='8G',
        gpus=None,
    ):
    """
    Submit a unix command to a slurm cluster.

    Parameters
    ----------
    command : str
        Unix command to run in the shell.
    basepath : str
        Base path is the full path prefix to use when
        creating the slurm sbatch script and output logs.
    partition : str
        Slurm partition to submit to.
    time : str
        Job time limit.
    mem : str
        Job CPU memory limit.
    gpus : str
        Number of GPUs to request.
    """

    # first check if sbatch is even accessible
    if shutil.which('sbatch') is None:
        fatal('Cannot find \'sbatch\' command in shell, is slurm installed?')

    # configure slurm settings
    lines = [
        f'#!/bin/bash',
        f'#SBATCH --account={account}',
        f'#SBATCH --partition={partition}',
        f'#SBATCH --mem={mem}',
        f'#SBATCH --time={time}',
        f'#SBATCH --ntasks=1',
        f'#SBATCH --nodes=1',
        f'#SBATCH --output={basepath}.out',
        f'#SBATCH --error={basepath}.err',
    ]

    if gpus is not None:
        lines.append(f'#SBATCH --gpus={gpus}')

    # write the slurm script
    lines.append(command)    
    slurm_file = basepath + '.slurm'
    with open(slurm_file, 'w') as file:
        file.write(''.join([f'{x}\n' for x in lines]))

    # submit to the cluster
    if run(f'sbatch {slurm_file}') != 0:
        fatal('sbatch job submission failed!')


def add_suffix(filename, suffix):
    """
    Insert a suffix in a file path, just before the extension if possible.
    This function relies on an explicit set of commonly-used file
    extensions. If the extension of the input filename is not found in
    this set, the suffix is appended to the end of the path, which
    might cause problems.

    Parameters
    ----------
    filename : str or None
        File path to append a suffix to.
    suffix : str
        Suffix to append.

    Returns
    -------
    str
        Modified filename.
    """
    if suffix is None:
        return filename

    # some known extensions that would probably be
    # used in deepsurfer IO
    extensions = [
        '.nii.gz',
        '.nii',
        '.mgh.gz',
        '.mgz',
        '.m3z',
        '.mgh',
        '.srf',
        '.surf',
        '.lta',
        '.xfm',
        '.annot',
        '.ctab',
        '.label',
        '.gii.gz',
        '.gii',
        '.stats',
        '.txt',
        '.log',
        '.npy',
        '.npz',
        '.tar.gz',
        '.tar',
        '.zip'
        '.jpeg',
        '.jpg',
        '.png',
        '.pdf',
        '.svg',
        '.gif',
        '.tif',
        '.tiff',
    ]

    # insert the suffix
    for ext in extensions:
        if filename.endswith(ext):
            return f'{filename.replace(ext, "")}{suffix}{ext}'
    return f'{filename}{suffix}'
