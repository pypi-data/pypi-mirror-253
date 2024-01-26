import os
import sys
import platform
import textwrap
import argparse

from .formatting import formatted
from .formatting import blue
from .formatting import bold
from .formatting import dim


class SubcommandParser(argparse.ArgumentParser):

    def __init__(self, *args, **kwargs):
        """
        A subclass of `argparse.ArgumentParser` customized for sub-commands.

        This parser is designed to start parsing arguments after the second command-line argument,
        as opposed to the first. It also includes some fancy custom formatting options provided
        by the `HelpFormatter` subclass defined below.

        Parameters
        ----------
        *args : any
            Positional arguments to be passed to the parent `ArgumentParser` constructor.
        **kwargs : any
            Keyword arguments to be passed to the parent `ArgumentParser` constructor.

        See Also
        --------
        argparse.ArgumentParser : The parent class of this subclass.
        """
        super().__init__(
            prog=' '.join(sys.argv[:2]),
            formatter_class=HelpFormatter,
            allow_abbrev=False,
            add_help=False, 
            *args,
            **kwargs)

        # rename the default title for flagged arguments
        self._optionals.title = 'options'

    def parse_args(self, args=None, namespace=None, allow_no_args=False):
        """
        Parse the command-line arguments.

        This method wraps the default `parse_args` method of the `argparse.ArgumentParser` class
        so that parsing starts after the second command line argument. It also appends a `--help`
        flag to the list of arguments.

        If `args` is None, the method takes the arguments from `sys.argv`. If `namespace` is None,
        the method creates a new namespace object to populate with the parsed arguments.

        Parameters
        ----------
        args : list, optional
            The list of arguments to parse. If not provided, the arguments are taken
            from `sys.argv`.
        namespace : argparse.Namespace, optional
            The namespace object to populate with the parsed arguments. If not provided,
            a new namespace object is created.
        allow_no_args : bool, optional
            Whether to allow no command-line arguments. Default is False, i.e., an error
            is raised if no arguments are provided.

        Returns
        -------
        argparse.Namespace
            The namespace object populated with the parsed arguments.
        """


        """
        Wrap the default parse_args() function so that parsing starts after the
        second command line argument. It also appends a --help flag to the list of
        arguments and exists with error when no commandl ine options are provided.
        """
        args = sys.argv[2:]
        
        # add help flag (at the end instead of the beginning) but only if it doesn't exist
        if 'help' not in [a.dest for a in self._actions]:
            self.add_argument('--help', action='help', help='Show this help message and exit.')
        
        # print usage and exit if no inputs are provided
        if not args and not allow_no_args:
            self.print_help()
            self.exit(2)

        return super().parse_args(args, namespace)

    def format_help(self):
        """
        Customize the default help formatter by organizing the help messages into
        distinct sections.

        Returns
        -------
        str
            The formatted help message.
        """
        formatter = self._get_formatter()

        # usage
        formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)

        # description
        if self.description is not None:
            formatter.add_text(formatted(self.description, width=formatter._width))

        # positionals, optionals, and user-defined groups
        groups = self._action_groups
        if len(groups) > 2:
            groups = groups[:1] + groups[2:] + groups[1:2]

        for action_group in groups:
            formatter.start_section(action_group.title.upper())
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        # epilog
        if self.epilog is not None:
            formatter.add_text(formatted(self.epilog, width=formatter._width))

        # return the formatted help message
        return formatter.format_help()


class HelpFormatter(argparse.HelpFormatter):

    def __init__(self, *args, **kwargs):
        """
        A subclass of `argparse.HelpFormatter` that provides customized help text
        formatting.

        This formatter is designed to improve upon the default settings for `argparse`
        help text, which can be difficult to read and parse. This subclass cleans up
        the help text output by increasing the indent and width, making section headers
        stand out, and other small tweaks.

        Parameters
        ----------
        *args : any
            Positional arguments to be passed to the parent `HelpFormatter` constructor.
        **kwargs : any
            Keyword arguments to be passed to the parent `HelpFormatter` constructor.

        See Also
        --------
        argparse.HelpFormatter : The parent class of this subclass.
        """
        super(HelpFormatter, self).__init__(width=80, indent_increment=4, *args, **kwargs)

    def _format_action(self, action):
        """
        Custom: account for change in indentation
        """
        parts = [self._current_indent * ' ' + self._format_action_invocation(action)]
        if action.help:
            self._indent()
            help_text = self._expand_help(action)
            for line in self._split_lines(help_text, self._width - self._current_indent):
                parts.append(self._current_indent * ' ' + line)
            self._dedent()
        return '\n'.join(parts) + '\n\n'

    def _format_action_invocation(self, action):
        """
        Custom: simplify the argument invocation syntax
        """
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return bold(metavar)
        else:
            msg = ', '.join([bold(opt) for opt in action.option_strings])
            if action.nargs != 0:
                default = self._get_default_metavar_for_optional(action)
                msg += '  ' +  blue(self._format_args(action, default).upper())
            return msg

    def _format_usage(self, usage, actions, groups, prefix=None):
        """
        Custom: simplify the usage string
        """

        prefix = bold('USAGE: ')

        # if usage is specified, use that
        if usage is not None:
            usage = usage % dict(prog=self._prog)

        # if no optionals or positionals are available, usage is just prog
        elif usage is None and not actions:
            usage = self._prog

        # if optionals and positionals are available, calculate usage
        elif usage is None:
            prog = self._prog

            # split flags from positionals
            positionals = [action for action in actions if not action.option_strings]
            flags = [action for action in actions if action.option_strings]

            # build full usage string
            format = self._format_actions_usage
            action_usage = format(positionals + flags, groups)
            usage = ' '.join([s for s in [prog, action_usage] if s])

            # wrap the usage parts if it's too long
            text_width = self._width - self._current_indent
            if action_usage and len(prefix) + len(usage) > text_width:
                usage = prog + ' '
                first_len = len(prefix) + len(usage) + self._current_indent
                lines = self._split_lines(action_usage, self._width - first_len)
                usage += lines[0]
                for line in lines[1:]:
                    usage += '\n' + first_len * ' ' + line

        return f'{prefix}{usage}\n\n'

    def _format_actions_usage(self, actions, groups):
        """
        Custom: simplify the usage string
        """
        parts = []
        for i, action in enumerate(actions):
            if not action.required:
                continue
            if not action.option_strings:
                parts.append(self._format_args(action, self._get_default_metavar_for_positional(action)))
            else:
                parts.append(action.option_strings[0])
                if action.nargs != 0:
                    default = self._get_default_metavar_for_optional(action)
                    parts.append(self._format_args(action, default))
        parts.append('[options] [--help]')
        return ' '.join(parts)

    def _get_default_metavar_for_optional(self, action):
        """
        Custom: use type for flagged argument metavar
        """
        return action.type.__name__ if action.type else action.dest

    def _fill_text(self, text, width, indent):
        """
        Custom: don't remove newlines when adding text
        """
        return '\n'.join([textwrap.fill(line, width, initial_indent=indent, subsequent_indent=indent) for line in text.strip().splitlines()])

    def _split_lines(self, text, width):
        """
        Custom: don't remove newlines when adding help text to arguments
        """
        lines = []
        for line in text.strip().splitlines():
            lines.extend(textwrap.fill(line, width).splitlines())
        return lines

    def _get_help_string(self, action):
        """
        Custom: add the default value to the option help message
        """
        help = action.help
        if help is None:
            help = ''
        if '%(default)' not in help:
            if action.default is not argparse.SUPPRESS and \
               action.default is not None and \
               not isinstance(action, argparse._StoreConstAction):
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    help += ' (default: %(default)s)'
        return help

    class _Section(argparse.HelpFormatter._Section):

        def format_help(self):
            """
            Custom: reformat each section's header
            """

            # format the indented section
            if self.parent is not None:
                self.formatter._indent()
            join = self.formatter._join_parts
            item_help = join([func(*args) for func, args in self.items])
            if self.parent is not None:
                self.formatter._dedent()

            # return nothing if the section was empty
            if not item_help:
                return ''

            # add the heading if the section was non-empty
            if self.heading is not argparse.SUPPRESS and self.heading is not None:
                indent = self.formatter._current_indent * ' '
                heading = indent + bold(self.heading) + '\n'
            else:
                heading = ''

            # join the section-initial newline, the heading and the help
            return join(['\n', heading, item_help, '\n'])
