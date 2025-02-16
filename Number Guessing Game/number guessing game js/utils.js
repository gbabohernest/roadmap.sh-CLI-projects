// This module contains Game helper functions

const gameDifficulties = require('./gameConstant');

/**
 * @Return string - A string specifying the rules of providing a custom range of numbers to guess.
 */
const gameRules = () => {
    return `
    Please provides a range of numbers you would like to guess within.
    Example: Range can be between two numbers (1 to 10) or (2 - 50) etc
    
    Take Note on the Rules:
    1. The first number (Lower Bound) cannot be greater or equal to the Second number (Upper Bound).
       Example: (100 to 1) NOT ACCEPTABLE.
    
    2. Both Lower & Upper bounds must be numbers greater than 0.
    `
}

/**
 * Prompt the user for custom guessing range of numbers to guess. [1, 10]
 * @return [Number] - Array of numbers. [lower & upper] bounds.
 */
const getCustomRange = () => {
    console.log(gameRules());


    // while (true) {
        try {
            // get custom range values;
            process.stdout.write('Enter both values seperated by space.')

            process.stdin.on('readable', () => {
                const data = process.stdin.read();
                // let limit;
                const customRange = data.split(' ', limit = 2);
                if (customRange.length === 2) {

                    let {firstNum, secondNum} = customRange;

                    const lowerBound = Number(firstNum);
                    const upperBound = Number(secondNum);

                    if ((!isNaN(lowerBound)) && (!isNaN(upperBound))) {
                        // they are both numbers.

                        //check if they are greater than zero.
                        if (lowerBound > 0 && upperBound > 0) {

                            if (lowerBound < upperBound) {
                                // return [lowerBound, upperBound];
                                    console.log([lowerBound, upperBound])
                                    process.exit(0)
                            } else {
                                console.log('Lower bound must be less than upper bound.');
                            }

                        } else {
                            // values are zero or less.
                            console.log('Both lower and upper bounds must be greater than zero.')
                        }

                    } else {
                        // they are not numbers.
                        console.log('Both lower and lower bounds must be a number.')
                    }

                } else {
                    // values must be two values
                    console.error('Please Provide two values.');
                }

            })

        } catch (exception) {
            console.log('Please enter two valid integers seperated by space.')
        }

        // re-prompt
    // }
}

/**
 * Prompt user to choose the game level.
 * @return Number - An integer presenting the game level. [1, 2, 3]
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

        const difficultiesLevel = Number(process.stdin.read());

        if (!isNaN(difficultiesLevel)) {
            // A valid number
            if (difficultiesLevel in gameDifficulties) {
                return difficultiesLevel;
            } else {
                console.error('WRONG!!! Please select a valid game level [1, 2, 3]')
                // prompt user if they want to quit the game or continue playing.
            }
        } else {
            console.log('Invalid input, Please enter a number. [1, 2, 3]');
            // prompt user if they want to quit the game or continue playing.
        }

    })
}


// module.exports = chooseGameLevel;
// module.exports = getCustomRange;

module.exports = {
    chooseGameLevel,
    getCustomRange,
}

console.log(module.exports);