"""
This module contains a function that fetches movie function and display it in the terminal
"""

import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from typing import List


def fetch_movies_details(movie_type: str, access_token: str) -> List:
    """
    Fetches movies information using the TMDB API.
    :param movie_type: The kind of movie to fetch (popular, top-rated, upcoming and now-playing movie)
    :param access_token: TMDB API access token
    :return: A list of dict containing movies information.
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
            results = response_data['results']

            if not results:
                print("Opps! Sorry could not fetch movies data.")
                exit()

            return results

    except HTTPError as e:
        if e.code == 401:
            print("Invalid API Key, must be granted a valid key.")

        else:
            print(f"Error, something went wrong. {e}")

    except URLError as e:
        print(f"Connection error. {e.reason}")


    except Exception as e:
        print(f"Unexpected error: {e}")
