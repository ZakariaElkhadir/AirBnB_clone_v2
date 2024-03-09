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

        local('tar -cvzf {} web_static'.format(archive_name))

        return archive_name
    except Exception as e:
        return None
