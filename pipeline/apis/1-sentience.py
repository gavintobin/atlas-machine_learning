#!/usr/bin/env python3
'''task2'''
import requests


API_ROOT = "https://swapi-api.alx-tools.com/api/"


def sentientPlanets():
    '''planets'''
    page = 1
    species_planet_urls, planet_list = [], []
    response = requests.get(API_ROOT + 'species/?page={}'.format(page))
    species_data = response.json()

    while species_data['next']:
        response = requests.get(API_ROOT + 'species/?page={}'.format(page))
        species_data = response.json()
        for species in species_data['results']:
            if species['designation'] == 'sentient':
                species_planet_urls.extend([species['homeworld']])
            if species['classification'] == 'sentient':
                species_planet_urls.extend([species['homeworld']])
        page += 1

    for url in species_planet_urls:
        if url is not None:
            response = requests.get(url)
            planet_data = response.json()
            planet_list.append(planet_data['name'])

    return(planet_list)



