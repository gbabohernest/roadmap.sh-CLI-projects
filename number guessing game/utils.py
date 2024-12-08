"""
Utils Function for the number guessing game
"""
import random
from game_constants import GAME_LEVELS, CHANCES


def play_game(level: int):
    """
    Executes the game main loop
    :param level: The level of difficulty the game will be played :
    :return:  None
    """

    computer_guess = random.randint(1, 100)
    difficulty = GAME_LEVELS[level]
    attempts_left = CHANCES[difficulty]
    attempts_used = 0

    # print(f"Computer guess: {computer_guess}")  # remove later, use for debugging

    while attempts_left > 0:
        # get user guess
        user_guess = get_user_guess()
        attempts_used += 1
        attempts_left -= 1

        if user_guess == computer_guess:
            print(f"Congratulations! You guessed the correct number in {attempts_used} attempts.\n")
            break

        if user_guess < computer_guess:
            print(f"Incorrect! The number is greater than {user_guess}. \n")

        else:
            print(f"Incorrect! The number is less than {user_guess}. \n")

        print(f"Remaining attempts: {attempts_left}. \n")

    if attempts_left == 0:
        print(f"Oops you've run out of guesses! The correct number was {computer_guess}. \n")


def get_user_guess():
    """
    Prompts the user to enter a valid guess.
    """
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, Please enter a valid number")


def select_difficulty() -> int:
    """
    Prompts user to select a valid difficulty level.
    :return: The difficulty(level)
    """

    while True:
        try:
            level = int(input('Enter your choice: '))

            if level in GAME_LEVELS:
                return level

            print("Invalid choice! Please select a valid level [1, 2, or 3]")

        except ValueError:
            print("Invalid input, Please enter a number")


def select_difficulty_and_start():
    """
    Allows the user to select a difficulty and start the game.
    """

    level = select_difficulty()
    print(f"\nGreat! You have selected the {GAME_LEVELS[level]} difficulty level.\nLet's start the game!\n")
    play_game(level)
