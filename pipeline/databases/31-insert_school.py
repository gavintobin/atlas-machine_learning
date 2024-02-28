#!/usr/bin/env python3
'''task 32 maybe this is long enough'''


def insert_school(mongo_collection, **kwargs):
    '''new document maybe this is long enough'''
    return mongo_collection.insert_one(kwargs).inserted_id
