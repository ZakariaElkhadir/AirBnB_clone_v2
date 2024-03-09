#!/usr/bin/python3
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
        env.hosts = ['<IP web-01>', '<IP web-02>']
        env.user = '<your_username>'
        env.key_filename = '<path_to_your_ssh_key>'

        archive_name = os.path.basename(archive_path)
        folder_name = os.path.splitext(archive_name)[0]

        for host in env.hosts:
            with Connection(host, user=env.user, connect_kwargs={"key_filename": env.key_filename}) as conn:
                conn.put(archive_path, "/tmp/")
                conn.run("mkdir -p /data/web_static/releases/{}".format(folder_name))
                conn.run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(archive_name, folder_name))
                conn.run("rm /tmp/{}".format(archive_name))
                conn.run("rm -rf /data/web_static/current")
                conn.run("ln -s /data/web_static/releases/{} /data/web_static/current".format(folder_name))

        return True
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        return False

if __name__ == "__main__":
    archive_path = do_pack()
    if archive_path:
        if do_deploy(archive_path):
            print("Deployment successful.")
        else:
            print("Deployment failed.")
    else:
        print("Archive creation failed.")
