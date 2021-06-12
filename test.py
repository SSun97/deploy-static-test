#!/usr/bin/python3
"""This module generates a .tgz file from web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """This function packs up all files from web_static"""
    try:
        now = datetime.now()

        tar_archive_name = "web_static_" +\
                           now.strftime("%Y%m%d%H%M%S")\
                           + ".tgz"
        tar_archive_path = "versions/" + tar_archive_name

        local("mkdir -p versions")

        local("tar -czvf " + tar_archive_path + " web_static")

        return tar_archive_path

    except:
        return None
