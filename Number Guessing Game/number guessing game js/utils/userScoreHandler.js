/*
* This module contains functions that deals with users' score.
 */

const fs = require('node:fs');
const path = require('node:path');
const {HIGH_SCORE_FILE} = require('./gameConstant');

// console.log(HIGH_SCORE_FILE)
const highScoreFile = path.join(__dirname, "..", HIGH_SCORE_FILE);

/**
 *  Load game high score(s) from a Json file or create an empty file if file doesn't exist.
 *  @param fileName : String - High score file name.
 *  @return Object - An object containing the file contents.
 */
const loadHighScore = (fileName) => {
    //check if the file exits.
    if (!fs.existsSync(fileName)) {
        fs.writeFileSync(fileName, JSON.stringify({}, null, 2))
    }

    return JSON.parse(fs.readFileSync(fileName, 'utf-8'))
}

/**
 * Save high scores back to the JSON file.
 * @param scores : Object  - An object containing the scores.
 * @param fileName : String -  Name of the file
 */
const saveHighScores = (scores, fileName) => {
    fs.writeFileSync(fileName, JSON.stringify(scores, null, 2));
}


/**
 * Update high scores if the player achieve a new best score
 * @param playerName : string - Name of the player.
 * @param score : Number - Player's score.
 */
const updateHighScore = (playerName, score) => {
    const allHighScores = loadHighScore(highScoreFile);

    if (!allHighScores[playerName] || score > allHighScores[playerName]) {
        allHighScores[playerName] = score;
        saveHighScores(allHighScores, highScoreFile);
        console.log(`New high score for ${playerName} : ${score} `)
    }
}