#!/usr/bin/env python3
'''Inserts a new document in a collection'''

def insert_school(mongo_collection, **kwargs):
    '''Insert one into the db'''
    return mongo_collection.insert_one(kwargs).inserted_id
