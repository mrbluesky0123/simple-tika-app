#-*- coding: utf-8 -*-
import os
import constants

def get_file_list():
    file_list = os.listdir(constants.FILE_DIR)
    for i in range(0, len(file_list)):
        file_list[i] = constants.FILE_DIR + file_list[i]
    return file_list