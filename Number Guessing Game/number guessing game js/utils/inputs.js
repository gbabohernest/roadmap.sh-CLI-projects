/*
* This module contains a function that handles user input
 */


const getUserInput = (prompt) => {
    return new Promise((resolve) => {
        process.stdout.write(prompt);
        process.stdin.resume();
        process.stdin.setEncoding('utf-8');

        process.stdin.once('readable', () => {
            const data = process.stdin.read();
            resolve(data.trim());
        })
    })
}

module.exports = { getUserInput };