#!/usr/bin/env python3
'''
topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    topic method
    '''
    result = mongo_collection.find({'topic': topic})
    return list(result)
