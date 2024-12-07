#!/usr/bin/python3

"""
Number Guessing Game - A Roadmap.sh Backend skill development project
"""

from utils import select_difficulty_and_start


def main():
    """
    Main function to start the game
    """

    game_rules = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
    
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)    
"""

    print(game_rules)

    while True:
        select_difficulty_and_start()
        play_again = input("\nDo you want to play again? Yes / No: ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing Goodbye")
            break


if __name__ == "__main__":
    main()
