#!/usr/bin/env python

from credential import API_ACCESS_TOKEN
from fetch_movie_details import fetch_movie_details


def main():
    print("Welcome to the TMDB CLI Tool\nEnter the type of movies data you want: eg(playing, popular, top, upcoming)")

    types_of_movies = {
        'playing': 'now_playing',
        'popular': 'something-popular',
        'top': 'something-top',
        'upcoming': 'something-upcoming'
    }

    try:
        movie_type = input("--type: ").strip()
        if movie_type not in types_of_movies:
            print("Wrong type, Please enter a valid type")
            return

        # call the fetch movie details function with the movie type
        fetch_movie_details(types_of_movies[movie_type], API_ACCESS_TOKEN)

    except ValueError:
        pass


if __name__ == "__main__":
    main()
