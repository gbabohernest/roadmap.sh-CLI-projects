// main game logic
const { DIFFICULTIES } = require('./gameConstant');
const { getUserInput } = require('./inputs');

/*
*  A function that control the game logic
**/

const startGame = async () => {
    console.log('\nSelect a difficulty level:');

    for (const [key, level] of Object.entries(DIFFICULTIES)) {
        console.log(`${key}: ${level['name']}`);
    }

}
module.exports =  { startGame };

