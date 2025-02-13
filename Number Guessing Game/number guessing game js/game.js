// main game logic
const fs = require('node:fs');

/*
*  A function that control the game logic
* */
const startGame = () => {
    const msg = `
 Welcome to the Number Guessing Game!
 I'm thinking of a number between 1 and 100.
 You have 5 chances to guess the correct number.
    
 Please select a difficulty level:
 1. Easy(10 chances)
 2. Medium(5 chances)
 3. Hard(3 chances)
 `

    console.clear();
    console.log(msg);
}

module.exports = { startGame };