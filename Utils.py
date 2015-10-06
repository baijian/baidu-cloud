# -*- coding: utf-8 -*-
import os
import sys
import yaml
import Constants

abspath = os.path.dirname(os.path.abspath(sys.argv[0])) + '/'

DEFAULT_CONFIG_FILE = abspath + '/cloud.cfg'


def read_config():
    ret = {}
    if os.path.exists(DEFAULT_CONFIG_FILE):
        conf = yaml.load(file(DEFAULT_CONFIG_FILE))
        ret = dict(conf, **ret)
    return ret


def format_disk_size(size, unit='Byte'):
    if size < 1024:
        return '%.2f %s' % (size, unit)
    return format_disk_size(size/1024.0, Constants.disk_unit[Constants.disk_unit.index(unit) + 1])


if __name__ == '__main__':
    a = 2000
    b = 123453416
    print format_disk_size(a)
    print format_disk_size(b)
