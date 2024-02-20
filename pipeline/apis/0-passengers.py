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

        for data in data.get('results', []):
            passengers = data.get('passengers', '0')  # Default to '0' if 'passengers' is missing
            if passengers.isdigit() and int(passengers) >= passenger_count:
                ships.append(data)

        base_url = data.get('next')

    return ships

