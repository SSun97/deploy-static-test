#!/usr/bin/python3
"""Fabric function"""

from fabric.api import local, env, put, run
from datetime import datetime
import os.path

env.hosts = ['3.90.35.112', '3.94.146.3']


def deploy():
    '''Method that creates and distributes an archive to servers'''
    newArc = do_pack()

    if newArc is None:
        return False

    return do_deploy(newArc)


def do_deploy(archive_path):
    """ Deploy an archive """

    if not os.path.exists(archive_path):
        return False
    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run("mkdir -p /data/web_static/releases/" +
            archiveNameWithoutExtension)
        run("tar -xzvf /tmp/" +
            archiveName +
            " -C " +
            "/data/web_static/releases/" +
            archiveNameWithoutExtension +
            " --strip-components=1")
        run("rm -f /tmp/" + archiveName)
        run("rm -f /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/" +
            archiveNameWithoutExtension + " /data/web_static/current")

        return True
    except BaseException:
        return False


def do_pack():
    """ pack up our web_static"""

    try:
        now = datetime.now()
        tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
        tarArchivePath = "versions/" + tarArchiveName

        local("mkdir -p versions")
        local("tar -czvf " + tarArchivePath + " web_static")

        return tarArchivePath
    except BaseException:
        return None
