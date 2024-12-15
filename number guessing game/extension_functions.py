"""
Game extension functions. These functions add extra functionalities to the game.
"""

from game_constants import SCORES_PER_DIFFICULTY, BONUS_MULTIPLIERS


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
