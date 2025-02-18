const {getUserInput} = require('./inputs');

/**
 *  A function that handles user guess.
 *  @param secretNumber :(Number) - A random number for user to guess.
 *  @param chancesLeft :(Number) - Amount of chances left to guess the number.
 */
const playGame = async (secretNumber, chancesLeft) => {
    //TODO work on the number of chances left , mostly espically if user missed or wrong type bad guess

    let usedAttempts = 0;
    while (chancesLeft > 0) {
        const userGuess = await getUserInput('Enter your guess: ');
        const guess = parseInt(userGuess, 10);

        if (isNaN(guess) && guess <= 0) {
            console.error('Invalid input, Please enter a valid number greater than 0.');
            continue;
            //TODO prompt user if they want to quit or continue.
        }

        /*
        if (guess < 1 || guess > 100) {
            console.error('Invalid, Please enter a number greater than 0');
            continue;
            //TODO prompt user if they want to quit or continue.
        }
        */
        usedAttempts++;
        chancesLeft--;
        if (guess === secretNumber) {
            console.log(`Congratulations! You guessed the correct number in ${usedAttempts} attempts.`)

        } else if (guess < secretNumber) {
            console.log(`Incorrect! The number is greater than ${guess}.\n`);

        } else {
            console.log(`Incorrect! The number is less than ${guess}.\n`)
        }

        console.log(`Chances left: ${chancesLeft}`);
    }

    // Didn't guess the number correctly, game over
    console.log(`Game over, you ran out of guesses. The correct number was ${secretNumber}`);
}