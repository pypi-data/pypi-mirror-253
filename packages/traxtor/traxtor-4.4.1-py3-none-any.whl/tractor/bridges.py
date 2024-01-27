# Released under GPLv3+ License
# Danial Behzadi <dani.behzi@ubuntu.com>, 2020-2024.

"""
module to manages bridges
"""

import os
import re
import shutil

from . import db


def get_sample_bridges() -> str:
    """
    there should be some sample bridges in the package
    """
    return os.path.dirname(os.path.abspath(__file__)) + "/SampleBridges"


def copy_sample_bridges(bridges_file) -> None:
    """
    function to copy sample bridges for tractor
    """
    sample_bridges_file = get_sample_bridges()
    try:
        shutil.copyfile(sample_bridges_file, bridges_file)
    except Exception as exception:
        raise IOError from exception


def get_file() -> str:
    """
    get bridges file address
    """
    data_dir = db.data_directory()
    os.makedirs(data_dir, mode=0o700, exist_ok=True)
    bridges_file = data_dir + "/Bridges"
    if not os.path.isfile(bridges_file):
        copy_sample_bridges(bridges_file)
    return bridges_file


def relevant_lines(my_bridges: str, bridge_type: int) -> list:
    """
    return the relevant bridge lines from bridge list
    """
    match bridge_type:
        case 1:
            regex = r"(\[?[:.\w]+\]?:\d+ \w{40})$"
        case 2:
            regex = r"(obfs4 \[?[:.\w]+\]?:\d+ \w{40} cert=.+ iat-mode=\d)$"
        case _:
            raise ValueError("Unknown bridge type.")
    pattern = re.compile(regex, re.MULTILINE)
    matches = pattern.findall(my_bridges)
    return matches
