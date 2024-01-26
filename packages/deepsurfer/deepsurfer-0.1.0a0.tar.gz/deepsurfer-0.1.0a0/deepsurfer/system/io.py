import os
import glob
import yaml

from . import resource
from .utility import fatal
from .utility import read_list


def parse_io_docket(
    parser,
    listed_columns,
    single_input_args=None,
    formatted=False):
    """
    This is meant to be a relatively generic way to parse sub-command line arguments
    in such a way that allows for specifying single-instance inputs (e.g. an
    input and output file are provided directly on the command line) or multiple
    instances (e.g. a set of subjects or list of input and output files).

    As an example, consider a SubcommandParser configured with these arguments:

    ```
    parser = SubcommandParser(description=description)
    parser.add_argument('-i', '--image', metavar='file', help='Input image (for single-image processing).')
    parser.add_argument('-o', '--out', metavar='file', help='Output image (for single-image processing).')
    parser.add_argument('--list', metavar='file', help='Input list for multi-image processing.')
    parser.add_argument('--subjs', nargs='+', metavar='subj', help='Subjects to process. Requires that IO type is provided.')
    parser.add_argument('--io', metavar='format', help='IO format type.')
    ```

    The enables the user to specify the IO protocol as an explicit set of input and output files
    by doing something like:

    ```
    ds command -i input.nii.gz -o output.nii.gz
    ```

    Or, alternatively, the user can specify a list of input and output files:

    ```
    ds command --list files.txt
    ```

    where each line in files.txt is a space-separated list of input and corresponding
    output file names.

    This file could alternatively consist of a list of subject paths for a subject-specific
    processing protocol, like for freesurfer-style outputs. In this case, the user needs
    to specify the --io IO type (e.g. FS for freesurfer-style outputs). The user can also
    specify a set of subjects to process. For example:

    ```
    ds command --subjs s01 s02 s03 --io fs
    ```

    This will process the subjects s01, s02, and s03, assuming that the IO type is configured.
    IO types can be defined by editing yaml files in the `deepsurfer/resource/io` package directory.

    The easiest way to configure the above example subcommand is by using this parse_io_docket
    function, which returns a "docket", i.e. a list of dictionaries, where each dictionary contains
    information about a single instance to process. Ex:

    ```
    docket = parse_io_docket(
        parser=parser,
        listed_columns=['image_input', 'image_processed'],
        single_input=['image', 'out'])

    for item in docket:
        image = sf.load_volume(item['image_input'])
        process(image).save('image_processed')

    ```

    The `listed_columns` parameter is meant to specify which keys correspond to each column
    in a potential input list file. The optional `single_input` parameter maps parser arguments
    to these column keys to enable single-instance inputs. If any subject-style processing is
    enabled for the subcommand (--subjs and --io are available flags), then the keys defined in
    `listed_columns` must correspond to keys defined in the IO type yaml file. Take a look at the
    `fs.yaml` file and `deepsurfer/modules/strip.py` as an example for how this works.


    Parameters
    ----------
    parser : SubcommandParser
        Command line parser.
    listed_columns : list of str
        Ordered list of column names for the input list file.
    single_input_args : list of str, optional
        List of parser arguments that correspond to the listed_columns. This enables
        single-instance processing.

    Returns
    -------
    list of dict
        List of dictionaries, where each dictionary contains information about a single
        instance to process.
    """

    # get all arguments supplied to the parser object
    vargs = vars(parser.parse_args())

    # check if subjects, iotype, and/or input list are specified
    subjs = vargs.get('subjs')
    iotype = vargs.get('io')
    listed_input_file = vargs.get('list')

    # initialize the output docket
    docket = []

    if single_input_args is not None:
        # here we handle the case where the command line parameters specify
        # only single-subject or single-instance processing

        # convert to list if it isn't one
        if not isinstance(single_input_args, (tuple, list)):
            single_input_args = [single_input_args]

        # the aguments must match the number of columns in the input list file
        if len(single_input_args) != len(listed_columns):
            raise ValueError('the length of listed_columns must match single_input_args')

        # here we check if the user has provided any of the single input arguments.
        # note that this should not throw a key error, assuming things are configured
        # correctly. if a key error is thrown here, it means the developer has listed
        # single input arguments that were never configured in the parser object
        single_inputs = [vargs[a] for a in single_input_args]

        # check if any of the single input arguments were actually provided
        given = [s is not None for s in single_inputs]

        if all(given):
            # if all of the single input arguments were provided, then we assume
            # that the user wants to process a single subject or instance
            spec = {k: v for k, v in zip(listed_columns, single_inputs)}
            docket.append(spec)
            return docket
        else:
            # if not all of the single input arguments were provided, then we check
            # to make sure this isn't a command line usage error
            optional_given = []
            if any(given) or any(optional_given):
                missing = [f'--{single_input_args[i]}' for i in range(len(given)) if not given[i]]
                fatal(f'Missing arguments: {", ".join(missing)}')

    # at this point we know that we are not (explicitly) processing a single instance, so we
    # assume that we are processing a list of inputs specified via the --list flag or --subjs flag
    if isinstance(subjs, str):
        subjs = [subjs]
    elif subjs is not None and len(subjs) == 0:
        subjs = None

    if listed_input_file is not None:

        if subjs is not None:
            fatal('Cannot specify both subjects AND an input file list. Must chose one or the other.')

        # read the input list file
        inputlist, ncolumns = read_list(listed_input_file)

        # sanity check on the file contents
        if len(inputlist) == 0:
            fatal(f'Input list file \'{listed_input_file}\' is empty')

        if iotype is None or not formatted:
            # if no IO format was specified, then we assume that the input list file
            # has columns correspond one-to-one with the listed_columns parameter
            if ncolumns != len(listed_columns):
                column_config = '\n'.join([f'column {i + 1}: {col.replace("_", " ")}' for i, col in enumerate(listed_columns)])
                fatal(f'Input list file \'{listed_input_file}\' has unexpected number of '
                      f'columns ({ncolumns}). Since no IO format was specified, the '
                      f'file should be a {len(listed_columns)}-column list, where '
                      f'the columns represent the following:\n\n{column_config}\n\n'
                       'If you want to only provide an input list of subjects (output '
                       'directories) following a particular IO format, use the --io flag.')
            for s in inputlist:
                docket.append({k: v for k, v in zip(listed_columns, s)})
            return docket
        else:
            # otherwise, we assume that the input list file is a list of subjects
            if ncolumns != 1:
                fatal(f'Input list file \'{listed_input_file}\' has unexpected number of '
                      f'columns ({ncolumns}). Since an IO format was specified ({iotype}), '
                      f'the file should be a 1-column list of subject directories.')
            subjs = [i[0] for i in inputlist]

    # at this point, iotype is a required argument
    if iotype is None:
        fatal('Must specify IO format type with --io flag when specifying input subjects.')
    io_spec = io_type_to_spec(iotype)

    # check somewhere to make sure io type has all the necessary stuff
    for k in listed_columns:
        if k not in io_spec:
            fatal(f'IO type \'{iotype}\' is missing required key \'{k}\'')

    # add special parameter to use the FS style SUBJECTS_DIR env variable when determining input paths
    if io_spec.get('use_subjects_directory'):
        sdir = os.environ.get('SUBJECTS_DIR')
        if sdir is not None:
            prefix = sdir[:-1] if sdir.endswith('/') else sdir
            subjs = [f'{prefix}/{s}' for s in subjs]
            print(f'Detected env variable SUBJECTS_DIR for IO type \'{iotype}\'')
            print(f'Using subject directory prefix {prefix}')

    # generate the docket for subjects specified with the --subjs flag
    if subjs is not None and len(subjs) > 0:
        for subj in subjs:
            spec = {k: v.format(outdir=subj) for k, v in io_spec.items() if isinstance(v, str)}
            docket.append(spec)

    return docket


def io_type_to_spec(iotype):
    """
    Given an IO type string, load the corresponding IO spec dictionary.

    Parameters
    ----------
    iotype : str
        The IO type string.

    Returns
    -------
    spec : dict
        The IO spec dictionary.
    """
    io_format_file = iotype if iotype.endswith('.yaml') else resource(f'iotypes/{iotype}.yaml', check=False)
    if not os.path.isfile(io_format_file):
        valid_format_files = glob.glob(resource(f'iotypes/*.yaml', check=False))
        valid = ', '.join([os.path.basename(v.replace('.yaml', '')) for v in valid_format_files])
        fatal(f'Cannot find IO format \'{iotype}\'. Valid built-in formats are: {valid}.')
    with open(io_format_file, 'r') as file:
        spec = yaml.safe_load(file)
    return spec
