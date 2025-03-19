import * as process from "node:process";

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

const displayUserActivity = (events, username) => {
  if (events.length === 0 && username) {
    console.log(`No recent activity found for user ${username}`);
    return;
  }
  const arrayObject = events.slice(10);
  let action;
  arrayObject.forEach((event) => {
    switch (event.type) {
      case "PushEvent":
        const numOfCommit = event.payload.commits.length;
        const repoName = event.repo.name;
        action = `Pushed ${numOfCommit} to ${repoName}`;
        break;

      case "IssuesEvent":
        action = `${event.payload.action.charAt(0).toUpperCase() + event.payload.action.slice(1)} an issue in ${event.repo.name}`;
        break;

      case "WatchEvent":
        action = `Starred ${event.repo.name}`;
        break;

      default:
        action = `${event.type.replace("Event", "")} in ${event.repo.name}`;
    }
  });
  console.log(`-- ${action}`);
};

const username = process.argv[2];

if (!username) {
  console.error("Username is required, Pls enter username:");
  process.exit(1);
}

const userData = await fetchGithubUserActivity(username);
displayUserActivity(userData, username);
