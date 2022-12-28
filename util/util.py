import platform
import os
import subprocess
import pathlib
import config


def open_with_editor(file_path):
    """Uses default OS text editor to open text file.

    :return: None
    :raises CalledProcessError: File at specified path cannot be opened
    """
    if platform.system() == 'Darwin':
        subprocess.run(['open', file_path], check=True)
    elif platform.system() == 'Windows':
        os.startfile(file_path)
    else:  # Linux
        subprocess.run(['xdg-open', file_path], check=True)


def get_file_content(file_list):
    """Returns text content of specified files from input list"""
    contents = []
    for file in file_list:
        p = pathlib.Path(config.get_data_path(), f'{file}.md')
        if not os.path.exists(p):
            continue
        with p.open() as f:
            contents.append(f.read())
    return contents

