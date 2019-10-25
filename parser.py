#-*- coding: utf-8 -*-

from tikapp import TikaApp
import json
import constants

def init_tika():
    # Get tika path
    tika_file = constants.TIKA_DIR + constants.TIKA_FILENAME
    # Get tika instance
    tika = TikaApp(file_jar=tika_file)
    return tika

def get_contents(file_list):
    # Get tika instance
    tika = init_tika()
    # init contents result list
    contents_list = []
    # Get contents for each file
    for file in file_list:
        contents_str = tika.extract_all_content(file)
        contents = json.loads(contents_str)
        contents_list.append(contents[0])
    
    return contents_list