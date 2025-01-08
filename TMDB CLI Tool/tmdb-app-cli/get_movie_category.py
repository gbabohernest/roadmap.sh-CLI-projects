"""
Get movie category from the user.
"""


def get_movie_category() -> str:
    """
    Get the movie category from the user.
    :return str:The category of movie (popular, now-playing, top-rated, upcoming)
    """

    movie_categories = {
        'playing': 'now_playing',
        'popular': 'popular',
        'top': 'top_rated',
        'upcoming': 'upcoming'
    }

    try:
        movie_category = input("--type: ").strip()
        if movie_category not in movie_categories:
            print("Wrong type, Please enter a valid type")
            exit()

        return movie_categories[movie_category]

    except ValueError:
        pass
