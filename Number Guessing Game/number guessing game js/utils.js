// This module contains Game helper functions

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
    `

    const prompt = 'Enter your choice: ';

    process.stdout.write(prompt);

    process.stdin.on('readable', () => {
        const input = process.stdin.read();
        if (input) {
            process.stdout.write(`thanks for providing your choice ${input}`);
        }
    })
}

module.exports = chooseGameLevel;