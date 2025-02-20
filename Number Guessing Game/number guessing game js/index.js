#!/usr/bin/env node

/*
* Game Entry point
* */

const { startGame } = require('./utils/game')
const { displayLeaderboard } = require('./utils/userScoreHandler');
const { getUserOption } = require('./utils/getUserOption');

async function main () {
      console.log('Welcome to the Number Guessing Game!!');
      console.log("Game menu");
      console.log("1. Play Game\n2. View Leaderboard\n3. Exit");

      let choice;

      do {
          choice = await getUserOption();
      } while(!choice);

      if (choice) {

          switch (choice) {
              case 1:
                  await startGame();
                  break;
              case 2:
                  displayLeaderboard();
                  break;
              case 3:
                  process.exit(0)
                  break;
          }
      }
}

main();



