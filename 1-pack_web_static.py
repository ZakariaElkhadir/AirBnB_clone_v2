#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder"""

from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """ Define the archive name with the current timestamp"""
    try:
        archive_name = 'web_static_{}.tgz'.format(
            datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        # Execute the tar command
        local('tar -cvzf {} web_static'.format(archive_name))
        # Return the archive path if the archive was created
        return archive_name
    except Exception as e:
        return None
