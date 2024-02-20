#!/usr/bin/env python3
 '''task1'''
 import requests


 
def available_ships(passenger_count):
    base_url = "https://swapi.dev/api/starships/"
    ships = []

    while base_url:
        response = requests.get(base_url)
        data = response.json()

        for starship in data.get('results', []):
            if int(starship['passengers']) >= passenger_count:
                ships.append(starship)

        base_url = data.get('next')

    return ships
