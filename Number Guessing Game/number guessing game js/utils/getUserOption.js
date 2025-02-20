// import { getUserInput as _getUserInput } from './inputs.js';
const { getUserInput } = require('./inputs.js');

/**
 * Function that get user options to play, display leaderboard or quit the game.
 */

const getUserOption = async () => {
  let responseOky = false;

  while (!responseOky) {
    //const option = parseInt(await _getUserInput('choose an option (1-3): '));
    const option = parseInt(await getUserInput('choose an option (1-3): '));

    if (option && !isNaN(option)) {
      // check the option [number either 1 - 3 ]
      switch (option) {
        case 1:
          return option;
        case 2:
          return option;
        case 3:
          return option;

        default:
          console.error(`Invalid value, Please enter [1, 2, or 3]`);
      }
    } else {
      console.error('Invalid, Please enter a number [1, 2, or 3] ');
    }
  }
};

module.exports = { getUserOption };