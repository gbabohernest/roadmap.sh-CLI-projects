#!/usr/bin/env python


from get_movie_category import get_movie_category
from credential import API_ACCESS_TOKEN
from fetch_movie_details import fetch_movies_details
from print_movies_details import print_movies_details


def main():
    print("Welcome to the TMDB CLI Tool\nEnter the type of movies data you want: eg(playing, popular, top, upcoming)")

    movie_category = get_movie_category()
    movie_data = fetch_movies_details(movie_category, API_ACCESS_TOKEN)
    # print(json.dumps(movie_data, indent=4))
    print_movies_details(movie_data, movie_category)


if __name__ == "__main__":
    main()
