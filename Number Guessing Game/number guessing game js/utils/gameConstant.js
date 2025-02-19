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

const SCORES_PER_LEVEL = {
    Easy: {
        score: 50,
        bonus: 5,
    },

    Medium: {
        score: 75,
        bonus: 10,
    },

    Hard: {
        score: 100,
        bonus: 20,
    }
}

const HIGH_SCORE_FILE = 'highScores.json';

module.exports = { DIFFICULTIES, HIGH_SCORE_FILE, SCORES_PER_LEVEL };