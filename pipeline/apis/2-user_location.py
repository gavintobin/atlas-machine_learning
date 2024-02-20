#!/usr/bin/env python3
import sys
import requests
import time

def get_user_location(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        user_data = response.json()
        location = user_data.get('location')
        if location:
            print(f"The location of the user is: {location}")
        else:
            print("Location not available for this user.")
    elif response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_time = int(response.headers['X-Ratelimit-Reset'])
        current_time = int(time.time())
        minutes_until_reset = max(0, reset_time - current_time) // 60
        print(f"Reset in {minutes_until_reset} min")
    else:
        print(f"Unexpected status code: {response.status_code}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <github_user_api_url>")
        sys.exit(1)

    user_api_url = sys.argv[1]
    get_user_location(user_api_url)
