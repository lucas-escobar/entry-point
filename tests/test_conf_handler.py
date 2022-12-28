import pytest
import configparser as conf
import pathlib
import re


def test_get_config_data_path():
    """Verify that the path returned by get_config matches the path
    found in config.ini. Assumes correct formatting of .ini file.
    """
    c = config.get_()
    p = pathlib.Path('../config/config.ini')
    with p.open() as f:
        for line in f:
            m = re.match('data_path', line)
            d = re.search(r"/*", line) if m else None
    assert c['Paths']['data_path'] == d
