<?php

/**
 * This file contains core functionalities for data persistence within the game.
 */


function loadHighScores(): array
{
    $fileName = 'high_scores.json';

    if (!file_exists($fileName)) {
        file_put_contents($fileName, json_encode([]));
    }

    $data = file_get_contents($fileName);
    return json_decode($data, true) ?? [];
}


