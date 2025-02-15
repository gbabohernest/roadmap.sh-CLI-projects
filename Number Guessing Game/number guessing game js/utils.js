// This module contains Game helper functions

const gameDifficulties = require('./gameConstant');

/*
* Prompt user to choose the game level.
* @return: An integer presenting the game level. [1, 2, 3]
*/


const chooseGameLevel = () => {
    const gameLevel = `
       Please select the difficulty level:
       1. Easy (10 chances)
       2. Medium (5 chances)
       3. Hard (3 chances)
    `;
    console.log(gameLevel.trimStart());
    const prompt = 'Enter your choice: ';

    process.stdout.write(prompt);

    process.stdin.on('readable', () => {

        const input = Number(process.stdin.read());

        if (!isNaN(input)) {
            // A valid number
            if (input in gameDifficulties) {
                console.log(gameDifficulties[input])
                console.log('exist')
                // return the game level.
            } else {
                console.error('WRONG!!! Please s-elect a valid game level [1, 2, 3]')
                // prompt user if they want to quit the game or continue playing.
            }
        }
        console.log('Invalid input, Please enter a number. [1, 2, 3]');
        // prompt user if they want to quit the game or continue playing.
    })
}


module.exports = chooseGameLevel;