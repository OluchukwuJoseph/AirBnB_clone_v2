#!/usr/bin/python3
"""This script deletes out-of-date archives, using the function do_clean"""
from fabric.api import run, local, env, cd
import os

env.hosts = ['54.152.97.27', '52.91.127.178']
env.user = 'ubuntu'
env.key_filename = "~/.ssh/school"


def do_clean(number=0):
    if number == 0:
        number = 1
    else:
        number = int(number)

    local_archives = sorted(os.listdir("versions"))
    deleted = 0
    while (deleted < (len(local_archives) - number)):
        local(f"rm ./versions/{local_archives[deleted]}")
        deleted += 1

    with cd('/data/web_static/releases/'):
        archives = run('ls')
        archives = [item for item in sorted(archives.stdout.split(' '))
                    if item.startswith('web_static_')]

        deleted = 0
        while (deleted < (len(archives) - number)):
            run(f"rm -rf ./{archives[deleted]}")
            deleted += 1
