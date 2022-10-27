# Uses Cornell's eBird API
# Docs: https://documenter.getpostman.com/view/664302/S1ENwy59?version=latest


import os
import requests


def get_region_name(response):
    """Extracts a human-readabe region name from a JSON response
    
    The JSON response should contain a key, "result," that is the name of the region (usually a county).

    Args:
        response: The JSON response

    Returns:
        A string that is the region name
    """
    region = response.json()
    return region["result"]

# Main
def get_region_detail(region_code):
    """Hits eBird's "Recent notable observations in a region" API for a hardcoded region.

    From eBird: "Get the list of recent, notable observations (up to 30 days ago) of birds seen in a country, region or location.

    Notable observations can be for locally or nationally rare species or are otherwise unusual, e.g. over-wintering birds in a species which is normally only a summer visitor."
    
    https://documenter.getpostman.com/view/664302/S1ENwy59#397b9b8c-4ab9-4136-baae-3ffa4e5b26e4

    Args:
        region_code: The major region, country, subnational1 or subnational2 code, or locId

    Returns:
        A string with the region name
    """

    LOCATION_ID = region_code

    
    EBIRD_API_KEY = os.getenv['API_KEY']
    url = 'https://api.ebird.org/v2/ref/region/info/' + LOCATION_ID + '?regionNameFormat=detailed'
    header = {'X-eBirdApiToken': EBIRD_API_KEY}

    r = requests.get(url, headers=header)
    region = get_region_name(r)

    return region