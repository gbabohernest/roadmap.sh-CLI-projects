<?php

/**
 * This file contains core functionalities for data persistence within the game.
 */


require_once 'game_constants.php';

/**
 * Loads high scores from a JSON file.
 *
 * @param string $fileName The name of the JSON file containing high scores.
 * @return array An associative array of high scores, with player names as key and scores as value
 */
function loadHighScores(string $fileName): array
{

    if (!file_exists($fileName)) {
        file_put_contents($fileName, json_encode([]));
    }

    $data = file_get_contents($fileName);
    return json_decode($data, true) ?? [];
}


/**
 * Saves high score to a JSON file.
 *
 * @param array $scores An associative array of high scores to save.
 * @param string $fileName The name of the JSON file to save high scores in.
 * @return void
 */
function saveHighScores(array $scores, string $fileName): void
{
    file_put_contents($fileName, json_encode($scores, JSON_PRETTY_PRINT));

}