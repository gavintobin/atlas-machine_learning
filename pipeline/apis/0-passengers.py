#!/usr/bin/env python3
'''task1'''
import requests


def availableShips(passenger_count):
    '''fvail ship number'''
    API_ROOT = "https://swapi-api.alx-tools.com/api/"
    page = 1
    results, ships_list, passengers_list = [], [], []

    response = requests.get(API_ROOT + 'starships/?page={}'.format(page))
    ships_data = response.json()


    while ships_data['next']:
        response = requests.get(API_ROOT + 'starships/?page={}'.format(page))
        ships_data = response.json()
        ships_list.extend([ship['name'] for ship in ships_data['results']])
        passengers_list.extend([ship['passengers']
                                for ship in ships_data['results']])
        page += 1

    for i in range(0, len(passengers_list)):
        passengers_list[i] = passengers_list[i].replace(',', '')
        if passengers_list[i] == 'n/a':
            passengers_list[i] = -1
        if passengers_list[i] == 'unknown':
            passengers_list[i] = -1
        passengers_list[i] = int(passengers_list[i])

    ship_passenger_dict = dict(zip(ships_list, passengers_list))

    for ship, passengers in ship_passenger_dict.items():
        if int(passengers) >= passengerCount:
            results.append(ship)

    return results
