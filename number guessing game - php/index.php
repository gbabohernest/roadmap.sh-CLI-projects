#!/usr/bin/env php
<?php


declare(strict_types=1);


$root = dirname(__DIR__) . DIRECTORY_SEPARATOR;

define('UTILS_FUNCTIONS', $root . 'number guessing game - php' . DIRECTORY_SEPARATOR);

require_once UTILS_FUNCTIONS . 'utils.php';
require_once 'scores_functions.php';


/**
 * Main function to control the game flow
 */

function main(): void
{
    displayWelcomeMessage();

    if (!handlePlayChoice("Press 1 to play or 0 to quit")) return;

    displayHighScores();

    do {
        $customRange = getCustomRange();
        displayDifficultyOptions();

        $difficultyLevel = getDifficultyChoice();

        displayUserChoiceAndChances($difficultyLevel, $customRange);
        runGuessingGame($difficultyLevel, $customRange);

        displayHighScores();

        $keepPlaying = handlePlayChoice("\nDo you want to continue playing? 1 for Yes, 0 for No: ");


    } while ($keepPlaying);

}

main();