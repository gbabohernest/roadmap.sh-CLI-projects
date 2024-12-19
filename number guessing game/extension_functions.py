"""
Game extension functions. These functions add extra functionalities to the game.
"""

import json
from os import path
from game_constants import SCORES_PER_DIFFICULTY, BONUS_MULTIPLIERS, HIGH_SCORES_FILE


def load_high_scores(file_name: str) -> dict:
    """
    Load game high score(s) from a Json file or create an emtpy file
    if file doesn't exist.

    :param file_name: Name of the file
    :return: A dict containing the high score(s)
    """

    if not path.exists(file_name):
        # create the file
        with open(file_name, 'w', encoding='utf-8') as file_stream_obj:
            json.dump({}, file_stream_obj)

    # file exist
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def calculate_user_score(difficulty: str, max_chances: int, attempts_used: int) -> int:
    """
    Calculates & return user's score based on difficulty level.
    Give bonus based on unused chances per difficulty.

    :param difficulty: The level of difficulty of the game.
    :param max_chances: Max chances per level
    :param attempts_used: Amount of attempts used out of max_chances.

    :return: User score
    """

    unused_chance = max([0, max_chances - attempts_used])
    bonus = unused_chance * BONUS_MULTIPLIERS[difficulty]

    return SCORES_PER_DIFFICULTY[difficulty] + bonus
