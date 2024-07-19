#!/usr/bin/env python3
'''
list db in py
'''


def list_all(mongo_collection):
    '''
    list method
    '''
    return [doc for doc in mongo_collection.find()]
