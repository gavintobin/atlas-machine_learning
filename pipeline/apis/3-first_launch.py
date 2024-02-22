#!/usr/bin/env python3
'''taskj 3'''
if __name__ == "__main__":
    import requests

    LAUNCHES = 'https://api.spacexdata.com/v5/launches/'
    ROCKETS = 'https://api.spacexdata.com/v4/rockets/'
    PADS = 'https://api.spacexdata.com/v4/launchpads/'

    upcomming_response = requests.get(LAUNCHES + 'upcoming')
    upcomming_launches = upcomming_response.json()

    launch_names = [launch['name'] for launch in upcomming_launches]
    launch_dates = [launch['date_local'] for launch in upcomming_launches]
    launch_rockets = [launch['rocket'] for launch in upcomming_launches]
    launch_pads = [launch['launchpad'] for launch in upcomming_launches]

    min_pos = launch_dates.index(min(launch_dates))

    rocket_response = requests.get(ROCKETS + launch_rockets[min_pos])
    rocket_data = rocket_response.json()
    rocket = rocket_data['name']

    pad_response = requests.get(PADS + launch_pads[min_pos])
    pad_data = pad_response.json()
    pad = pad_data['name']
    locality = pad_data['locality']

    name = launch_names[min_pos]
    date = launch_dates[min_pos]

    print("{} ({}) {} - {} ({})".format(name, date, rocket, pad, locality))
