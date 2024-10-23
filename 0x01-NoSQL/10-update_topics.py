#!/usr/bin/env python3
'''Changes documents'''

import pymongo
def update_topics(mongo_collection, name, topics):
    '''Updates all documents in a collection

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update
        name (str): The name of the document to update
        topics (list): The new topics for the document

    Returns:
        int: Updated documents'''
    return mongo_collection.update_many({'name': name, '$set': {'topics': topics}})
