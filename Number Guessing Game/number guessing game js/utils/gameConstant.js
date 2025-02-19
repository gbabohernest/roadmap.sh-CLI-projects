//Game constant

const DIFFICULTIES = {
    1: {
        name: 'Easy',
        chances: 10,
    },

    2: {
        name: 'Medium',
        chances: 5,
    },

    3: {
        name: 'Hard',
        chances: 3
    },
}

const HIGH_SCORE_FILE = 'highScores.json';

module.exports = { DIFFICULTIES, HIGH_SCORE_FILE };