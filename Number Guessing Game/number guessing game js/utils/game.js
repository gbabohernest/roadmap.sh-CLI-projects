/*
* This module contains functions that control the game logic.
 */


const { DIFFICULTIES} = require('./gameConstant');
const { getUserInput } = require('./inputs');
const { getUserName } = require('./getUserName');
const { playGame } = require('./playGame');

/*
*  A function that control the game logic
**/

const startGame = async () => {
    console.log('\nPlease select the difficulty level:');

    for (const [key, level] of Object.entries(DIFFICULTIES)) {
        console.log(`${key}: ${level['name']} \(${level['chances']} chances\)`);
    }
    console.log();

    let difficulty;
    let chances;

    while (!difficulty) {
        const levelInput = await getUserInput('Enter your choice: ');

        // validate user input;
        if (DIFFICULTIES[levelInput]) {
            difficulty = DIFFICULTIES[levelInput]['name'];
            chances = DIFFICULTIES[levelInput]['chances'];
        } else {
            console.error('Invalid choice! Please select a valid level [1, 2, or 3]\n');
            //TODO try to prompt user if they want to quit or not.
        }
    }

    let playerName;
    do {
        playerName = await getUserName();
    } while (!playerName)


    const maxChances = chances;
    const secretNumber = Math.floor(Math.random() * 100) + 1;

    console.log(`\nGreat! You have selected the ${difficulty} difficulty level.\nYou have ${maxChances} chances.`);
    console.log("Let's start the game!\n");

    //get the user's input;
    playGame(secretNumber, maxChances, difficulty, maxChances, playerName);

}


module.exports = { startGame };

