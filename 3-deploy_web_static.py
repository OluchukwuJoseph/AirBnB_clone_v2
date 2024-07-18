#!/usr/bin/python3
"""This script distributes an archive to my web servers"""
from fabric.api import env, put, local, run
from os import path
from datetime import datetime


env.hosts = ['54.152.97.27', '52.91.127.178']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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
        if not (path.exists(archive_path)):
            return False

        # upload web_static archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'
            .format(timestamp))

        # uncompress archive and delete .tgz
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}/"
            .format(timestamp, timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static
        run("sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/"
            .format(timestamp, timestamp))

        run("sudo rm -rf /data/web_static/releases/web_static_{}/web_static"
            .format(timestamp))

        # delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run("sudo ln -s /data/web_static/releases/web_static_{}/\
            /data/web_static/current".format(timestamp))

    except Exception as e:
        return False

    # return True on success
    return True


def deploy():
    """This function creates and distributes an archive to your web servers"""
    archive_path = do_pack()

    deployed = do_deploy(archive_path)

    return deployed
