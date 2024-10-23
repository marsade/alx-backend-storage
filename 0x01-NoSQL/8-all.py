#!/usr/bin/env python3
'''Lists all the documents in the MongoDB database'''


def list_all(mongo_collection):
    '''Lists all documents in the specified collection'''
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
