#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""

from fabric.api import *
import os
from datetime import datetime

from fabric.api import local
import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:

        local('mkdir -p versions')

        name = "web_static_{}".format(
            datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

        local("tar -cvzf versions/{}.tgz {}".format(name, "web_static/"))

        return "versions/{}".format(name)
    except Exception as e:

        print(f"An error occurred: {e}")
        return None
