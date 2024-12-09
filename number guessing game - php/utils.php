<?php

declare(strict_types=1);


require_once 'game_constants.php';


/**
 * Display the game introduction and rules.
 * @return void
 */
function displayWelcomeMessage(): void
{
    $message = <<<EOT
Welcome to the Number Guessing Game.
Press 1 to play or 0 to quit: 
EOT;
    echo "$message";
}


/**
 * Handles the user's choice to play or quit the game.
 *
 * @return bool Returns true if the user wants to play, otherwise false.
 */
function handlePlayChoice(): bool
{
    fscanf(STDIN, "%d", $choice);

    if ($choice === 1) return true;

    echo "\nGoodbye! Thanks for checking out the game!\n";
    return false;
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

Enter your choice: 
EOT;

    echo "$options";
}

/**
 * Gets the user's difficulty choice.
 * @return int  The chosen difficulty level (1 => Easy, 2=> Medium, or 3 => Hard)
 */
function getDifficultyChoice(): int
{
    fscanf(STDIN, "%d", $choice);

    if ($choice === 0) {
        echo "Goodbye! Thanks for checking out the game!\n";
        die();
    }

    if (!array_key_exists($choice, GAME_LEVELS)) {
        echo "Invalid selection. Please select a valid level (1, 2 or 3).\n";
        echo "Enter 0 if you want to quit\n";

        //Re-prompt the user
        displayDifficultyOptions();
        return getDifficultyChoice();
    }


//    return GAME_LEVELS[$choice];
    return $choice;
}

/**
 * Display the difficulty level user choose and the amount of chances to guess.
 * @param int $level The chosen difficulty level [1, 2, 3]
 * @return void
 */
function displayUserChoiceAndChances(int $level): void
{
    $difficultyLevel = GAME_LEVELS[$level];
    $chances = CHANCES[$difficultyLevel];


    $message = <<<EOT
\nGreat! You have selected the $difficultyLevel difficulty level.\n
I'm thinking of a number between 1 and 100.
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

        if ($userGuess === 0) {
            echo "Goodbye! Thanks for checking out the game!\n";
            die();
        }
        if (is_numeric($userGuess) && $result = intval($userGuess) == $userGuess) {
            return $userGuess;
        }

        echo "Invalid input. Please enter a valid integer OR Press 0 to quit." . PHP_EOL;
    }
}

/**
 * Runs the guessing game logic.
 *
 * @param int $levelOfGame The selected difficulty level.
 */
function runGuessingGame(int $levelOfGame): void
{
    $computerGuess = random_int(1, 100);
    $gameLevel = GAME_LEVELS[$levelOfGame];
    $maxAttempts = CHANCES[$gameLevel];
    $attemptsUsed = 0;

    echo("Computer guess: $computerGuess\n");  # remove later, use for debugging

    while ($attemptsUsed < $maxAttempts) {

        $userGuess = getUserGuess();


        $attemptsUsed += 1;

        if ($userGuess === $computerGuess) {
            echo "Congratulations! You guessed the correct number in $attemptsUsed attempts.\n";
            return;
        }

        if ($userGuess < $computerGuess) {
            echo "Incorrect! The number higher than $userGuess\n";
        } else {
            echo "Incorrect! The number is less than $userGuess\n";
        }

        echo "\nYou've used $attemptsUsed attempts out of $maxAttempts\n";
    }

    echo "Sorry, you've run out of attempts. The correct number was $computerGuess.\n";

}
