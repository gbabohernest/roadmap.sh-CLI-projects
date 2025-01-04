"""
This module contains a function that fetches GitHub user activity.
"""

import json
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError


def fetch_github_user_activity(username: str):
    """
    Fetches GitHub user activity using the GitHub API and displays it in the terminal.
    :param username: User for which we fetch the GitHub activity
    """

    endpoint = f'https://api.github.com/users/{username}/events'
    headers = {'User-Agent': 'GitHub-Activity-CLI'}

    try:
        request = Request(endpoint, headers=headers)
        with urlopen(request) as response:
            response_bytes = response.read()
            response_data = json.loads(response_bytes)
            # print(response_data)

            if not response_data:
                print(f"No recent activity found for user '{username}'.")
                return

            # Extract & display user's activity
            print(f"Recent activity for GitHub user '{username}'.")

            # display up to 10 activities
            for event in response_data[:10]:
                event_type = event.get('type', 'Unknown Event')
                repo_name = event['repo']['name'] if 'repo' in event else 'Unknown'

                if event_type == 'PushEvent':
                    commit_count = len(event.get('payload', {}).get('commits', []))
                    print(f"-- Pushed {commit_count} commits to {repo_name}")

                elif event_type == 'IssuesEvent':
                    action = event['payload'].get('action', 'performed an action on')
                    issue = event['payload'].get('issue', {}).get('title', 'an issue')
                    print(f"--{action.capaitalize()} issue '{issue}' in {repo_name}")

                elif event_type == 'WatchEvent':
                    print(f"-- Starred {repo_name}")

                else:
                    print(f"-- {event_type.replace('Event', '')} in {repo_name}")


    except HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")

        elif e.code == 403:
            print(f"Error: Rate limit exceeded. Try again later")

        else:
            print(f"HTTP error: {e.code}")

    except URLError as e:
        print(f"Connection error: {e.reason}")

    except Exception as e:
        print(f"Unexpected error: {e}")
