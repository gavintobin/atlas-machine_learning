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
            if ('classification' in species and
                species['classification'].lower() == 'sentient') or \
               ('designation' in species and
               species['designation'].lower() == 'sentient'):
                if 'homeworld' in species and species['homeworld']:
                    homeworld_url = species['homeworld']
                    homeworld_response = requests.get(homeworld_url)
                    homeworld_data = homeworld_response.json()
                    planets.append(homeworld_data['name'])

        url = data['next']

    return planets
