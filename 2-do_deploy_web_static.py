#!/usr/bin/python3
"""This script distributes an archive to my web servers"""
from fabric.api import *
import os


env.key_filename = '~/.ssh/school'
env.hosts = ['54.152.97.27', '52.91.127.178']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Distributes an archive to my web servers"""
    try:
        # Check archive_path exist
        if not os.path.exists(archive_path):
            return False
        archived_file = archive_path[9:]

        # Without the extension.
        file_without_ext = archived_file[:-4]

        # Full path without the extension of the file
        file_dir = "/data/web_static/releases/{}/".format(
                file_without_ext)

        # Retrive the file name
        archived_file = "/tmp/" + archive_path[9:]

        # Upload to /tmp/ directory of the server
        put(archive_path, "/tmp/")

        # Create the directory & Uncompress the file
        run("sudo mkdir -p {}".format(file_dir))

        run(
                "sudo tar -xvf {} -C {}".format(
                    archived_file,
                    file_dir
                    )
                )

        # Remove the archived file
        run("sudo rm {}".format(archived_file))

        run("sudo mv {}web_static/* {}".format(file_dir, file_dir))

        run("sudo rm -rf {}web_static".format(file_dir))

        run("sudo rm -rf {}".format("/data/web_static/current"))

        # Create symbolic link
        run("sudo ln -s {} /data/web_static/current".format(file_dir))

        print("New version deployed!")

    except Exception as e:
        return False

    return True
