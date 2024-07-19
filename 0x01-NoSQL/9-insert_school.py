#!/usr/bin/env python3
'''
inserted school
'''


def insert_school(mongo_collection, **kwargs):
    '''
    insert method
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
