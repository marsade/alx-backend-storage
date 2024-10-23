#!/usr/bin/env python3
'''Find a list based on conditions'''

import pymongo

def schools_by_topic(mongo_collection, topic):
    '''Finds the list of schools having a specified topic
    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to search in
        topic (str): The topic to search for
    Returns:
        list: List of schools with the specified topic'''
    return list(mongo_collection.find({'topics': topic}))
