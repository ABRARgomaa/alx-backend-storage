#!/usr/bin/env python3
'''
topic
'''


def schools_by_topic(mongo_collection, topic):
    '''
    topic method
    '''
    tfilter = {
        'topics': {
            '$elementMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(tfilter)]
