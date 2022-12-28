import inspect
from time import strftime, localtime
from pathlib import Path
import config
import logging as log
import util


def get_current_entry_file():
    """Returns pathlib.Path object containing path to today's journal entry"""
    p = config.get_data_path()
    curr_date_ymd = strftime("%Y-%m-%d", localtime())
    return Path(p, f'{curr_date_ymd}.md')


def get_entry_template():
    """Returns string to be printed at the beginning of each journal entry.
    Intended to be able to be parsed as YAML for metadata (front matter).
    """
    return inspect.cleandoc(strftime(
        """
        ---
        year_week_day: %Y-%W-%j
        time_created: %H:%M:%S
        ---
        # %a %b %-d
        """,
        localtime()
    ))


def create_entry():
    """Creates new journal entry titled with current date (YMD) and writes
    basic template at start of file.

    :return: None
    :raises FileExistsError: Entry for today already exists
    """
    p = get_current_entry_file()
    if p.exists():
        raise FileExistsError("Entry for current date already exists")
    p.write_text(get_entry_template())


def handle_write():
    """Create a new journal entry for the current date and open the file
    in the default system text editor
    """
    try:
        create_entry()
    except FileExistsError as err:
        log.error(err)
    finally:
        f = get_current_entry_file()
        util.open_with_editor(f)
