import * as process from "node:process";

console.log(process.argv);

/**
 * fetches GitHub user activity using the GitHub API
 * @param username : string  - GitHub username
 * @returns {Promise<void>}
 */
const fetchGithubUserActivity = async (username) => {
  const apiEndpoint = `https://api.github.com/users/${username}/events`;


  } catch (error) {
    console.error(error.message);
  }
};

await fetchGithubUserActivity(process.argv[2]);
