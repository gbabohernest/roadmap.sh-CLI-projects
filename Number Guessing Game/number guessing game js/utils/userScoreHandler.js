/*
* This module contains functions that deals with users' score.
 */

const fs = require('node:fs');
const path = require('node:path');
const { HIGH_SCORE_FILE } = require('./gameConstant');

// console.log(HIGH_SCORE_FILE)
const highScoreFile = path.join(__dirname, "..", HIGH_SCORE_FILE);

/**
 *  Load game high score(s) from a Json file or create an empty file if file doesn't exist.
 *  @return Object - An object containing the file contents.
 */
const loadHighScore  = () => {
    //check if the file exits.
    if (!fs.existsSync(highScoreFile)) {
        fs.writeFileSync(highScoreFile, JSON.stringify({}, null, 2))
    }

    return JSON.parse(fs.readFileSync(highScoreFile, 'utf-8'))
}

