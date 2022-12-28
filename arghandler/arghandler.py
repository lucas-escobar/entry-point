import argparse
import pathlib
import arghandler.arg_functions as arg_functions


def get_argparser():
    """Returns a configured instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        prog='entry-point',
        description="""
        Command line program that creates, organizes, and manages daily journal
        entries.
        """,
    )
    parser.add_argument(
        '-w', '--write',
        action=Write,
        help="""
        Create and open a new entry file with the current date. If an entry for 
        the current date exists, the file is opened.
        """,
    )
    # TODO: implement absolute functionality
    parser.add_argument(
        '-r', '--read',
        action=Read,
        nargs='*',
        default=[3], # FIXME: default not working
        help="""
        Read entries in specified date range. Range can be relative to current
        date (read past 3 entries: [3]) or absolute (read entries from 
        2022-01-01 to 2023-01-01: ['2022-01-01', '2023-01-01'])
        """,
    )
    # TODO: -d should change data_path in config.ini
    parser.add_argument(
        '-d', '--directory',
        nargs=1,
        type=pathlib.Path,
        default=f'{__file__}/entries',
        help="""Specify directory in which to store journal entries""",
    )
    return parser


class Write(argparse.Action):
    def __init__(self, nargs=0, **kwargs):
        if nargs != 0:
            raise ValueError("No args permitted for --write actions")
        super().__init__(nargs=nargs, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        arg_functions.handle_write()


class Read(argparse.Action):
    def __init__(self, nargs='*', **kwargs):
        super().__init__(nargs=nargs, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        if len(values) > 2:
            raise ValueError("Args for --read should not exceed 2")
        arg_functions.handle_read(values)



