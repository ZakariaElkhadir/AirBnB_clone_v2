#!/usr/bin/python3
"""
Fabric script that distributes
 an archive to your web servers.
"""
import os
from fabric.api import *
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:
        local('mkdir -p versions')
        name = "web_static_{}".format(datetime.now().strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf versions/{}.tgz web_static/".format(name))
        return "versions/{}".format(name)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        if not os.path.exists(archive_path):
            return False
        fn_with_extension = os.path.basename(archive_path)
        fn_no_extension = os.path.splitext(fn_with_extension)
        deploy_path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f"rm -p {deploy_path}{fn_no_extension}/")
        run(f"mkdir -p {deploy_path}{fn_no_extension}/")
        run("tar -xzf /tmp/{} -C {}{}/".format(
            fn_with_extension, deploy_path, fn_no_extension))
        run(f"rm /tmp/{fn_with_extension}")
        run("mv {0}{1}/web_static/* {0}{1}/".format(deploy_path, fn_no_extension))
        run(f"rm -rf {deploy_path}{fn_no_extension}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {deploy_path}{fn_no_extension}/ /data/web_static/current")
        print("Deployment complete.")
        return True
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        return False