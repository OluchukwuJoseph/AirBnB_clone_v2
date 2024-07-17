#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import local, cd


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
