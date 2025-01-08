"""
This module contains a function that fetches movie function and display it in the terminal
"""


import json
from urllib.request import  urlopen, Request
from urllib.error import HTTPError, URLError
from xml.etree.ElementTree import indent


def fetch_movie_details(movie_type: str, access_token: str):
    """
    Fetches movie information using the TMDB API and display in the terminal.
    :param movie_type:
    :param access_token:
    :return:
    """

    url = f'https://api.themoviedb.org/3/movie/{movie_type}?language=en-US&page=1'
    headers = {
        'User-Agent': 'TMDB-CLI Tools',
        'accept': 'application/json',
        'Authorization': f"Bearer {access_token}"
    }

    try:
        request = Request(url, headers=headers)
        with urlopen(request) as response:
            response_byte = response.read()
            response_data = json.loads(response_byte.decode('utf-8'))
            print(json.dumps(response_data, indent=4))

            # iterate over the data and get the relevant info


    except HTTPError as e:
        if e.code == 401:
            print("Invalid API Key, must be granted a valid key.")

        else:
            print(f"Error, something went wrong. {e}")

    except URLError as e:
        print(f"Connection error. {e.reason}")


    except Exception as e:
        print(f"Unexpected error: {e}")




