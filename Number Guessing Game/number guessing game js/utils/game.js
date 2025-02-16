// main game logic
const { DIFFICULTIES } = require('./gameConstant');
const { getUserInput } = require('')

/*
*  A function that control the game logic
* */
const startGame = () => {

    console.clear();
    console.log('Welcome to the Number Guessing Game\n');
    const difficulties = utilFuns.chooseGameLevel()
    console.log(difficulties);
    utilFuns.getCustomRange();

}

// module.exports =  startGame;

