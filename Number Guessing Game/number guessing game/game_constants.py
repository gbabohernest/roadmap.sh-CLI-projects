"""
Constants for game levels and chances
"""

GAME_LEVELS = {
    1: 'Easy',
    2: 'Medium',
    3: 'Hard'
}

CHANCES = {
    'Easy': 10,
    'Medium': 5,
    'Hard': 3
}

SCORES_PER_DIFFICULTY = {
    'Easy': 50,
    'Medium': 75,
    'Hard': 100
}

BONUS_MULTIPLIERS = {
    'Easy': 5,
    'Medium': 10,
    'Hard': 20
}

HIGH_SCORES_FILE = "high_scores.json"