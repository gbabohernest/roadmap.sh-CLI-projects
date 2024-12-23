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


/**
 * Updates the high scores list with a new or improved score for a player.
 *
 * @param string $playerName The name of the player.
 * @param int $score The player's score to update.
 * @return void
 */
function updateHighScores(string $playerName, int $score): void
{
    $highScores = loadHighScores(HIGH_SCORES);

    // update score if player exits,  or add new entry.
    if (!isset($highScores[$playerName])) {
        $highScores[$playerName] = $score;
    }

    $highScores[$playerName] = max($highScores[$playerName], $score);
    saveHighScores($highScores, HIGH_SCORES);

}

/**
 * Displays the high scores' leaderboard.
 *
 * @return void
 */

function displayHighScores(): void
{
    $highScores = loadHighScores(HIGH_SCORES);

    if ($highScores !== []) {
        echo "\n---- Game LeaderBoard ----\n---- High Scores ----\n";

        foreach ($highScores as $name => $score) {
            echo "$name: $score points" . PHP_EOL;
        }
    }
}
