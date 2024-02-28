#!/usr/bin/env python3
'''task 30'''


def list_all(mongo_collection):
    '''list all'''
    return mongo_collection.find()
