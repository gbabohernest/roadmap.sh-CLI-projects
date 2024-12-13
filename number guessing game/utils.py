"""
Utilities Functions for the number guessing game
"""
import textwrap
import random
from game_constants import GAME_LEVELS, CHANCES
from typing import List


def play_choice(message: str) -> bool:
    """
    Handles user's choice to play or quit the game
    :param message: The custom message to ask the user
    :return: bool - True if user wants to play false otherwise.
    """

    while True:
        try:
            continue_playing = int(input(message).strip())
            if continue_playing == 1:
                return True
            elif continue_playing == 0:
                print("Sad to see you leave:( Thanks for checking out the game.")
                return False
            else:
                print("Please enter a VALID Integer: 1 or 0.")
        except ValueError:
            print("Please enter a Valid Integer 1 or 0.")


def get_user_custom_range() -> List[int]:
    """
     Prompt user to provide a custom range of
     numbers to guess while playing the game.
    :return: List[int] A list of integers (lower & upper) bounds.
    """

    game_rules = """
   Kindly provide a range of numbers you would like to guess  within.
   Example: Range can be between two numbers (1 to 100) etc.
   
   Rules:
   1. The Lower bound(first number) cannot be greater than or equal
      to the Upper bound(second number) (e.g., 100 to 1 is NOT ACCEPTABLE).
   2. Both Lower & Upper bounds must be numbers greater than 0.
   """
    game_rules = textwrap.dedent(game_rules)

    print(game_rules)

    while True:
        try:
            user_input = input("Enter both lower & upper bounds separated by space: ").strip()
            lower_bound, upper_bound = map(int, user_input.split())

            if lower_bound > 0 and upper_bound > 0:
                if lower_bound < upper_bound:
                    return [lower_bound, upper_bound]
                else:
                    print("Lower bound must be less than upper bound\n")
            else:
                print("Both lower and upper bound must be greater than 0.\n")

        except ValueError:
            print('Please enter two valid integer values separated by space\n')

        if not play_choice('Press 0 to quit, 1 to try again!: '): exit()


def get_user_guess():
    """
    Prompts the user to enter a valid guess.
    """
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 0:
                return guess
            else:
                print("Invalid, Please enter a number greater than 0")

        except ValueError:
            print("Invalid input, Please enter a valid number")

        if not play_choice('Press 0 to quit or 1 try again:  '): exit()


def play_game(level: int, user_custom_range: List[int]):
    """
    Executes the game main loop
    :param user_custom_range: User custom range of guesses.
    :param level: The level of difficulty the game will be played :
    :return:  None
    """

    user_custom_guess = random.randint(user_custom_range[0], user_custom_range[1])
    difficulty = GAME_LEVELS[level]
    attempts_left = CHANCES[difficulty]
    attempts_used = 0

    print(f"Computer guess: {user_custom_guess}")  # remove later, use for debugging
    user_guess_val = 0
    while attempts_left > 0:
        # get user guess
        user_guess = get_user_guess()
        attempts_used += 1
        attempts_left -= 1
        user_guess_val = user_guess

        if user_guess == user_custom_guess:
            print(f"Congratulations! You guessed the correct number in {attempts_used} attempts.\n")
            break

        if user_guess < user_custom_guess:
            print(f"Incorrect! The number is greater than {user_guess}. \n")

        else:
            print(f"Incorrect! The number is less than {user_guess}. \n")

        print(f"Remaining attempts: {attempts_left}. \n")

    if attempts_left == 0 and user_guess_val != user_custom_guess:
        print(f"Oops you've ran out of guesses! The correct number was {user_custom_guess}.")


def select_difficulty() -> int:
    """
    Prompts user to select a valid difficulty level.
    :return: The difficulty(level)
    """

    difficulties = """
    Please select the difficulty level:
    1. Easy(10 chances)
    2. Medium(5 chances)
    3. Hard(3 chances)
    """

    difficulties = textwrap.dedent(difficulties)
    print(difficulties)

    while True:
        try:
            level = int(input('Enter your choice: '))

            if level in GAME_LEVELS:
                return level

            print("Invalid choice! Please select a valid level [1, 2, or 3]")

        except ValueError:
            print("Invalid input, Please enter a number")

        if not play_choice('Press 0 to quit or 1 try again:  '): exit()


def level_info(level: int, custom_range: List[int]) -> str:
    """
    Prints the Difficulty Level information chosen by the user.
    :param level: The Level chosen
    :param custom_range:  The custom range of number the user provided
    :return: A string informing the user of their chosen level, chances and guess range.
    """
    game_info = f"""
       Great! You have selected the {GAME_LEVELS[level]} difficulty level.
       I'm thinking of a number between {custom_range[0]} and {custom_range[1]}.
       You have {CHANCES[GAME_LEVELS[level]]} chances to guess the correct number.

       Let's start the game!
       """

    game_info = textwrap.dedent(game_info)
    return game_info


def select_difficulty_and_start():
    """
    Allows the user to select a difficulty and start the game.
    """
    custom_range = get_user_custom_range()
    level = select_difficulty()

    print(level_info(level, custom_range))
    play_game(level, custom_range)
