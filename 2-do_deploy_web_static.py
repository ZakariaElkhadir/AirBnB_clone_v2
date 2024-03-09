#!/usr/bin/python3
import os
from fabric.api import *
from datetime import datetime

def do_pack():
    """Generates a .tgz
    archive from the contents of
    the web_static folder"""
    local('mkdir -p versions')
    name = "web_static_{}"
