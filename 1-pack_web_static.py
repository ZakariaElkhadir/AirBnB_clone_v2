#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""

from fabric.api import local
import os
from datetime import datetime


def do_pack():
    # Define the archive name with the current timestamp
    archive_name = 'web_static_{}.tgz'.format(
        datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    # Execute the tar command
    local('tar -cvzf {} web_static'.format(archive_name))
    # Return the archive path if the archive was created
    if os.path.exists(archive_name):
        return archive_name
    else:
        return None
