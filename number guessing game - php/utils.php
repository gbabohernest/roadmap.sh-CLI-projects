<?php

declare(strict_types=1);


require_once 'game_constants.php';


/**
 * Display the game introduction and rules.
 * @return void
 */
function displayWelcomeMessage(): void
{

    echo "Welcome to the Number Guessing Game.\n";
}


/**
 * Handles the user's choice to play or quit the game.
 * @param string $message The custom message to ask the user.
 * @return bool Returns true if the user wants to play, otherwise false.
 */
function handlePlayChoice(string $message): bool
{
    echo "$message: ";
    fscanf(STDIN, "%d", $choice);

    if ($choice === 1) return true;

    echo "\nGoodbye! Thanks for checking out the game!\n";
    return false;
}

/**
 * Prompt the user to define a custom range for the guessing game.
 *
 * @return array int[] An array containing the lower and upper bounds
 */

function getCustomRange(): array
{
    $rangeRule = <<<RULE
You'll decide the number range you want to guess.
Example: Range can be between two numbers (1 to 100) etc.

Rules:
1. The Lower bound cannot be greater than or equal to the Upper bound (e.g., 100 to 1 is NOT ACCEPTABLE).
2. Both Lower & Upper bounds must be numbers greater than 0.\n
RULE;

    echo "\n$rangeRule" . PHP_EOL;

    // loop runs until valid input is provided
    while (true) {
        echo "Enter the lower bound: ";
        fscanf(STDIN, "%d", $lowerBound);

        echo "Enter the upper bound: ";
        fscanf(STDIN, "%d", $upperBound);


        if (
            is_numeric($lowerBound) && is_numeric($upperBound) &&
            $lowerBound > 0 && $upperBound > 0
        ) {
            if ($lowerBound < $upperBound) {
                return [$lowerBound, $upperBound];
            } else {
                echo "Invalid range. Lower bound must be less than upper bound.\n";
            }
        } else {
            echo "Both bounds must be positive integers greater than 0. Try again.\n";
        }

        // Ask if user wants to quit the game or try again
        $playAgain = handlePlayChoice("\nPress 0 to quit the game or 1 to try agan: ");
        if (!$playAgain) die();
    }

}

/**
 * Display the game difficulty options.
 */
function displayDifficultyOptions(): void
{
    $options = <<<EOT
\nPlease select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

EOT;

    echo "$options";
}

/**
 * Gets the user's difficulty choice.
 * @return int  The chosen difficulty level (1 => Easy, 2=> Medium, or 3 => Hard)
 */
function getDifficultyChoice(): int
{

    // loop runs until a valid difficulty option is provided.
    while (true) {

        echo "\nEnter your choice: ";
        fscanf(STDIN, "%d", $choice);

        if (array_key_exists($choice, GAME_LEVELS)) {
            return $choice;
        } else {
            echo "Invalid selection. Please select a valid level (1, 2 or 3).\n";
        }

        $playAgain = handlePlayChoice("\nPress 0 to quit the game or 1 to try again: ");
        if (!$playAgain) die();
    }
}


/**
 * Display the difficulty level user choose and the amount of chances to guess.
 * @param int $level The chosen difficulty level [1, 2, 3]
 * @return void
 */
function displayUserChoiceAndChances(int $level, array $userCustomRange): void
{
    $difficultyLevel = GAME_LEVELS[$level];
    $chances = CHANCES[$difficultyLevel];


    $message = <<<EOT
\nGreat! You have selected the $difficultyLevel difficulty level.\n
I'm thinking of a number between $userCustomRange[0] and $userCustomRange[1].
You have $chances chances to guess the correct number.

Let's start the game!!

EOT;

    echo "$message" . PHP_EOL;

}


/**
 * Get the user guess
 * @return int User guessed value
 */
function getUserGuess(): int
{

    while (true) {
        echo "Enter your guess: ";

        fscanf(STDIN, "%d", $userGuess);

        if (is_numeric($userGuess) && $userGuess > 0) {
            return $userGuess;
        }

        echo "Invalid input. Please enter a valid integer greater than 0." . PHP_EOL;

        $playGame = handlePlayChoice("\nPress 0 to quit the game or 1 to try again: ");
        if (!$playGame) die();
    }
}

/**
 * Runs the guessing game logic.
 *
 * @param int $levelOfGame The selected difficulty level.
 */
function runGuessingGame(int $levelOfGame, array $userCustomRange): void
{
    $customRange = random_int($userCustomRange[0], $userCustomRange[1]);
    $gameLevel = GAME_LEVELS[$levelOfGame];
    $maxAttempts = CHANCES[$gameLevel];
    $attemptsUsed = 0;


    echo("Computer guess: $customRange\n");  # remove later, use for debugging

    while ($attemptsUsed < $maxAttempts) {

        $userGuess = getUserGuess();


        $attemptsUsed += 1;

        if ($userGuess === $customRange) {
            echo "Congratulations! You guessed the correct number in $attemptsUsed attempts.\n";
            return;
        }

        if ($userGuess < $customRange) {
            echo "Incorrect! The number higher than $userGuess\n";
        } else {
            echo "Incorrect! The number is less than $userGuess\n";
        }

        echo "\nYou've used $attemptsUsed attempts out of $maxAttempts\n";
    }

    echo "Sorry, you've run out of attempts. The correct number was $customRange.\n";

}
