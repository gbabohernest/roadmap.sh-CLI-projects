import * as process from "node:process";

console.log(process.argv);

/**
 * fetches GitHub user activity using the GitHub API
 * @param username : string  - GitHub username
 * @returns {Promise<void>}
 */
const fetchGithubUserActivity = async (username) => {
  const apiEndpoint = `https://api.github.com/users/${username}/events`;

  try {
    const response = await fetch(apiEndpoint, {
      headers: { "User-Agent": "Node GitHub User Activity" },
    });

    if (!response.ok) {
      if (response.status === 404) {
        throw new Error("User NOT Found, Check user name and try again!!");
      } else {
        throw new Error(`Error fetching the resource: ${response.status}`);
      }
    }
    return await response.json();
  } catch (error) {
    console.error(error.message);
  }
};

await fetchGithubUserActivity(process.argv[2]);
