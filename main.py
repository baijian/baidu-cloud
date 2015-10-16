# -*- coding: utf-8 -*-
import os
import sys
import PCS
import Constants


def read_dir(dir_name):
    current_path = dir_name
    files = os.listdir(dir_name)
    for f in files:
        if os.path.isfile(current_path + '/' + f):
            remote_path = Constants.PCS_BASE_DIR + '/' + current_path + '/' + f
            PCS.upload_file_to_pcs(remote_path, current_path + '/' + f, True)
        else:
            read_dir(current_path + '/' + f)


if __name__ == '__main__':
    args = sys.argv
    directory_name = args[args.index("-d") + 1]
    current_dir = os.getcwd()
    if directory_name[0] == '/':
        dir_name = directory_name
    else:
        dir_name = current_dir + '/' + directory_name
    read_dir(dir_name)
