# Uses Cornell's eBird API
# Docs: https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest

import os
from flask import abort
import requests


def get_list_of_common_names(response):
    """Parses a list of common names for birds from a JSON response
    
    The JSON response should contain a key, "comName," that contains the common name of the bird.

    Args:
        response: The JSON response

    Returns:
        A list containing the common names of all birds in the JSON response

    Raises:
        KeyError: If the JSON response does not have the "comName" key
    """
    birds = response.json()

    birds_list = []
    for bird in birds:
        birds_list.append(bird["comName"])
    return birds_list

# Cast to a set to remove duplicates
def get_unique_common_names(birds_list):
    """Casts a list of bird names to a set to remove duplicate names
    
    Args:
        birds_list: A list containing common names of birds

    Returns:
        A set containing common names of birds
    """
    return(set(birds_list))

# Main
def get_recent_notable_birds(region):
    """Hits eBird's "Recent notable observations in a region" API for a passed-in region code.

    From eBird: "Get the list of recent, notable observations (up to 30 days ago) of birds seen in a country, region or location.

    Notable observations can be for locally or nationally rare species or are otherwise unusual, e.g. over-wintering birds in a species which is normally only a summer visitor."
    
    https://documenter.getpostman.com/view/664302/S1ENwy59#397b9b8c-4ab9-4136-baae-3ffa4e5b26e4

    Returns:
        A set containing names of birds
    """

    LOCATION_ID = region # future: verify region string _before_ calling API?

    EBIRD_API_KEY = os.getenv('API_KEY')

    url = 'https://api.ebird.org/v2/data/obs/' + LOCATION_ID + '/recent/notable'
    header = {'X-eBirdApiToken': EBIRD_API_KEY}

    try:
        r = requests.get(url, headers=header)
        r.raise_for_status() # If eBird API returns with 4xx or 5xx, bail out
    except requests.exceptions.HTTPError:
        abort(404)

    # If response is empty, the region code is likely incorrect
    if r.json() == []:
        abort(404)

    recent_notable_birds = get_unique_common_names(get_list_of_common_names(r))

    return recent_notable_birds