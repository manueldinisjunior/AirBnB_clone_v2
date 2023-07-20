#!/usr/bin/python3
""" All web_static folder into a .tgz file """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Nethod invoqued with fabric arg. """
    date = datetime.now()
    str_date = date.strftime('%Y%m%d%H%M%S')
    str_date = 'versions/web_static_' + str_date + '.tgz'
    local("mkdir -p versions")
    local("tar -c -v -z -f {} web_static".format(str_date))
    return str_date
