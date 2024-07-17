#!/usr/bin/python3
"""This script distributes an archive to my web servers"""
from fabric.api import run, put, env
import os


env.key_filename = '~/.ssh/school'
env.hosts = ['54.152.97.27', '52.91.127.178']
env.user = 'ubuntu'


def do_pack():
    """This function generates a .tgz archive from web_static contents"""
    # Create /versions directory, if it doesn't exist
    local("mkdir -p versions/")

    # Generate archive name and create archive
    archive_name = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
    archive = local(f"tar -czvf versions/{archive_name} web_static")

    if archive.succeeded:
        return f"versions/{archive_name}"
    else:
        return None


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
        run("mkdir -p {}".format(file_dir))

        run(
                "sudo tar -xvf {} -C {}".format(
                    archived_file,
                    file_dir
                    )
                )

        # Remove the archived file
        run("sudo rm {}".format(archived_file))

        run("mv {}web_static/* {}".format(file_dir, file_dir))

        run("rm -rf {}web_static".format(file_dir))

        run("rm -rf {}".format("/data/web_static/current"))

        # Create symbolic link
        run("ln -s {} /data/web_static/current".format(file_dir))

        print("New version deployed!")

        return True
    except Exception as e:
        return False


def deploy():
    """This function creates and distributes an archive to your web servers"""
    archive_path = do_pack()

    deployed = do_deploy(archive_path)

    return deployed
