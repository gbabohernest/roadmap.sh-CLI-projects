#!/usr/bin/python3

"""
Number Guessing Game - A Roadmap.sh Backend skill development project
"""

# from utils import select_difficulty_and_start
from utils import play_choice, select_difficulty_and_start


def main():
    """
    Main function to start the game
    """

    print("Welcome to the Number Guessing Game!!")

    if not play_choice("Press 1 to play, 0 to quit: "):  return

    while True:
        select_difficulty_and_start()
        play_again = play_choice("Do you want to play again? Press 1 to play, 0 to quit:  ")

        if not play_again:
            print("\nThanks for playing the game. Goodbye :)")
            break


if __name__ == "__main__":
    main()
