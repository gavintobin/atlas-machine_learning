#!/usr/bin/env python3
'''taskj 3'''
import requests

def get_first_launch_info():
    '''task 3'''
    api_url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(api_url)

    if response.status_code == 200:
        launches = response.json()
        if launches:
            # Sort launches based on date_unix
            launches.sort(key=lambda launch: launch['date_unix'])

            first_launch = launches[0]

            launch_name = first_launch.get('name', 'N/A')
            launch_date_local = first_launch.get('date_local', 'N/A')

            # Check if 'rocket' is a string or a dictionary
            rocket_info = first_launch.get('rocket', 'N/A')
            if isinstance(rocket_info, dict):
                rocket_name = rocket_info.get('name', 'N/A')
            else:
                rocket_name = rocket_info

            launchpad_name = first_launch.get('launchpad', {}).get('name', 'N/A')
            launchpad_locality = first_launch.get('launchpad', {}).get('location', {}).get('name', 'N/A')

            result = "{launch_name} ({launch_date_local}) {rocket_name} - {launchpad_name} ({launchpad_locality})"
            print(result.format(launch_name=launch_name, launch_date_local=launch_date_local,
                                rocket_name=rocket_name, launchpad_name=launchpad_name, launchpad_locality=launchpad_locality))
        else:
            print("No launches found.")
    else:
        print("Error: {}".format(response.status_code))

if __name__ == '__main__':
    '''main'''
    get_first_launch_info()
