#-*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch import helpers
from datetime import datetime

import constants

def init_elastic_search():
    # Get elastic search instance
    elastic_search = Elasticsearch(constants.ELASTICSEARCH_HOST)
    return elastic_search

def upload_contents(contents_list):
    # Get elastic search instance
    es = init_elastic_search()
    # Upload contents
    for contents in  contents_list:
        res = es.index(index=contents['resourceName'].lower(), doc_type='manual', body=contents)
        print(contents['resourceName'] + ' uploaded')