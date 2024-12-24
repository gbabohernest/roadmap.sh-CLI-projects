# Number Guessing Game

This is a **CLI-based application** developed as part of the [roadmap.sh](https://roadmap.sh/projects/number-guessing-game) backend skills development project

Check out the [project url here](https://roadmap.sh/projects/number-guessing-game)


### Features

1. Difficulty Levels:
   - Easy: 10 chances to guess.
   - Medium: 5 chances to guess.
   - Hard: 3 chances to guess.

2. Custom Range:
   - User can specify the range of guessing numbers for the game.

3. Scoring System:
   - Points are awarded based on the difficulty level and the number of unused chances.
   
   - Difficulty-based scores:
     - Easy: 50 points
     - Medium: 75 points
     - Hard: 100 points
     
   - Bonus points are calculated as:
     - Easy: 5 points per unused chance.
     - Medium: 10 points per unused chance.
     - Hard: 20 points per unused chance.
   
4. Persistent High Scores:
   - High scores are saved in a **JSON** file.
   - The leaderboard displays the top scores in descending order.


### How to Run the Project

1. **Clone the repository**:
    ```bash
   git clone <repository-url>

2. Navigate to the project directory:
    ```bash
   cd <respository-directory>

3. Run the script:
   ```bash
    ./main.py #script is executable
   python main.py  # not executable


### How to Play

1. When prompted, choose to play or quit.
2. Select a difficulty level (Easy, Medium, Hard).
3. Specify a range of numbers (eg: 1 to 100).
4. Guess the number within the allowed chances.
5. Scores are calculated and saved based on your performance.
6. View the leaderboard at the end of the game.
