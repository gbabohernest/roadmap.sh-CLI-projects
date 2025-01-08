def print_movies_details(movie_data: list, movie_category: str):
    """
    Print the relevant information about the movie.
    :param movie_data: A list containing movies data.
    :param movie_category: Movie category.
    """

    categories = {
        'now_playing': 'Now Playing',
        'popular': 'Popular',
        'top_rated': 'Top Rated',
        'upcoming': 'Upcoming'
    }

    category_fields = {
        'popular': ['title', 'release_date', 'popularity', 'vote_count', 'adult'],
        'now_playing': ['title', 'release_date', 'adult'],
        'top_rated': ['title', 'release_date', 'vote_average', 'adult'],
        'upcoming': ['title', 'release_date', 'adult']
    }

    field_headers = {
        'title': 'Movie Title',
        'release_date': 'Release Date',
        'popularity': 'Popularity',
        'vote_count': 'Vote Count',
        'adult': 'Adult Film',
        'vote_average': 'Rating'
    }

    fields = category_fields.get(movie_category, [])
    header_str = " ".join(f"{field_headers[field]:<30}" for field in fields)

    print(f"\nThe following are the best Five (5) '{categories[movie_category]}' movies right now!!!")
    print()
    print(header_str)
    print("=" * len(header_str))

    for movie in movie_data[:5]:
        print(" ".join(f"{str(movie.get(field, 'N/A')):<30}" for field in fields))
