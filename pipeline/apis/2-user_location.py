#!/usr/bin/env python3
'''task a3'''
import sys
import requests
import time


if __name__ == '__main__':
    ''''user loc'''
    res = requests.get(sys.argv[1])

    if res.status_code == 200:
        print(res.json()['location'])
    elif res.status_code == 404:
        print("Not found")
    if res.status_code == 403:
        time = (int(res.headers['X-RateLimit-Reset']) - int(time.time()))
        print("Reset in {} min".format(time//60))
