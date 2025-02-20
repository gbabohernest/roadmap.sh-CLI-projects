const { getUserInput } = require('./inputs');

/**
 * A function that gets the username and return it.
 * @return String - username.
 */

const getUserName = async () => {
    let valOky = false;

    while (!valOky) {
        const username = await getUserInput('Enter your name to save your score: ');

        if (username.trim().length > 2) {
            valOky = true;
            return username;
        } else {
            console.error("Invalid input! Name must contain at least 3 characters.");
        }
    }
};

module.exports = { getUserName }

