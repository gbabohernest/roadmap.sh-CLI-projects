const { SCORES_PER_LEVEL} = require('./gameConstant');

/**
 * Calculate user score.
 * @param level : String  The game leve of difficulty.
 * @param maxChances : Number The max number of chances per level.
 * @param usedAttempts : Number  Number of attempts used.
 *
 * @return Number - User total score for a level.
 */
const calculateUserScore = (level, maxChances, usedAttempts) => {
    const unusedAttempts = Math.max(0, maxChances - usedAttempts);
    const bonus = unusedAttempts * SCORES_PER_LEVEL[level]['bonus'];

    return SCORES_PER_LEVEL[level]['score'] + bonus;
}


module.exports = { calculateUserScore }