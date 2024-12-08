#!/usr/bin/env php
<?php


declare(strict_types=1);


$root = dirname(__DIR__) . DIRECTORY_SEPARATOR;

define('UTILS_FUNCTIONS', $root . 'number guessing game - php' . DIRECTORY_SEPARATOR);

require_once UTILS_FUNCTIONS . 'utils.php';


/**
 * Main function to control the game flow
 */

function main(): void
{
    displayWelcomeMessage();

    if (!handlePlayChoice()) return;

    do {
        displayDifficultyOptions();

        $difficultyLevel = getDifficultyChoice();

        displayUserChoiceAndChances($difficultyLevel);
        runGuessingGame($difficultyLevel);

        echo "\nDo you want to continue playing? 1 for Yes, 0 for No: ";
        $keepPlaying = handlePlayChoice();


    } while ($keepPlaying);

}

main();