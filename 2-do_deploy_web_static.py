#!/usr/bin/python3
"""This script distributes an archive to my web servers"""
from fabric.api import run, put, env
import os


env.use_ssh_config = True
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
    """This function distributes an archive to my web servers"""
    # Check if archive file exists
    if not os.path.exists(archive_path):
        return False

    # Upload archive file on server and uncompress it
    try:
        put(f'{archive_path}', '/tmp/')
        archive_name = archive_path.split('/')[-1]
        archive_name = archive_name.split('.')[0]

        run(f"mkdir -p /data/web_static/releases/{archive_name}/")
        run(f"tar -xzf /tmp/{archive_name}.tgz -C\
            /data/web_static/releases/{archive_name}/")

        # Delete archive from server and create a symbolic link to new release
        run(f"rm /tmp/{archive_name}.tgz")

        run(f"mv /data/web_static/releases/{archive_name}/web_static/*\
            /data/web_static/releases/{archive_name}")

        run(f"rm -rf /data/web_static/releases/{archive_name}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s /data/web_static/releases/{archive_name}/\
             /data/web_static/current")

        print('New version deployed!')
        return True
    except Exception as e:
        return False
