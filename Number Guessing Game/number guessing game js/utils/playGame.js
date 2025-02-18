const {getUserInput} = require('./inputs');

/**
 *  A function that handles user guess.
 *  @param secretNumber :(Number) - A random number for user to guess.
 *  @param chancesLeft :(Number) - Amount of chances left to guess the number.
 */
const playGame = async (secretNumber, chancesLeft) => {
    let usedAttempts = 0;
    console.log(`for debugging, computer guess is: ${secretNumber}`); // remove later.

    while (chancesLeft > 0) {
        const userGuess = await getUserInput('Enter your guess: ');
        const guess = parseInt(userGuess, 10);

        if (!isNaN(guess) && guess > 0) {
            usedAttempts++;
            chancesLeft--;

            if (guess === secretNumber) {
                console.log(`Congratulations! You guessed the correct number in ${usedAttempts} attempts.`)
                return;

            } else if (guess < secretNumber) {
                console.log(`Incorrect! The number is greater than ${guess}.`);

            } else {
                console.log(`Incorrect! The number is less than ${guess}.`)
            }

            console.log(`Chances left: ${chancesLeft}`);

            //TODO prompt user if they want to quit or continue.
        } else {
            // WRONG INPUT!
            console.error('Invalid input, Please enter a valid number greater than 0.');
        }
    }

    // Didn't guess the number correctly, game over
    console.log(`Game over, you ran out of guesses. The correct number was ${secretNumber}`);
    //TODO: Ask user if they want to continue playing.
}


module.exports = {playGame};