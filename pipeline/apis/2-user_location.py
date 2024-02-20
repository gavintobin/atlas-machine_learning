#!/usr/bin/env python3
'''task a3'''
import sys
import requests
import time


if __name__ == "__main__":
    import requests
    import sys
    import time

    if len(sys.argv) != 2:
        print("Usage: ./2-user_location https://api.github.com/users/<user>")

    API = sys.argv[1]

    response = requests.get(API)

    user_data = response.json()

    if response.status_code == 200:
        print(user_data['location'])

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset_time = response.headers['X-RateLimit-Reset']
        now = int(time.time())
        print("Reset in {} min".format((int(reset_time) - now) // 60))
