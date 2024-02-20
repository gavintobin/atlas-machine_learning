#!/usr/bin/env python3
'''task2'''
import requests


def sentientPlanets():
    '''list of names with sentient beings'''
    base_url = "https://swapi.dev/api/starships/"
    planets = []

    while base_url:
        response = requests.get(base_url)
        data = response.json()

        for species in data['results']:
            if 'classification' in species and 'designation' in species:
                if 'sentient' in species['classification'].lower() or 'sentient' in species['designation'].lower():
                    homeworld_url = species.get('homeworld')
                    if homeworld_url:
                        homeworld_data = requests.get(homeworld_url).json()
                        planets.append(homeworld_data.get('name', ''))

        base_url = data['next']

    return planets
