#!/usr/bin/env python3
'''task 32'''


def insert_school(mongo_collection, **kwargs):
    '''new document'''
     return mongo_collection.insert_one(kwargs).inserted_id
