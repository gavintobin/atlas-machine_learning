#!/usr/bin/env python3
'''task1'''
import requests


def availableShips(passenger_count):
    '''fvail ship number'''
    base_url = "https://swapi.dev/api/starships/"
    ships = []

    while base_url:
        response = requests.get(base_url)
        data = response.json()

        for ship in data.get('results', []):
            if ship.get('passengers') and int(ship['passengers']) >= passengerCount:
                ships.append(ship['name'])

        base_url = data.get('next')

    return ships
