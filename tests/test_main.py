import pytest
import main
from time import strftime, localtime
import configparser as conf
from pathlib import Path


def test_create_file_location():
    """Check if upon creating a new entry file, it exists in the expected
    directory based on the config file
    """
