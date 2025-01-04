# GitHub User Activity CLI

GitHub User Activity CLI is a Python-based command-line application that fetches and displays the recent activity of a specified GitHub user. This project demonstrates the use of APIs, handling JSON data, and building CLI applications using Python.

## Features

- Fetch recent GitHub user activity using the GitHub API.
- Display activities such as pushes, issues, and stars in the terminal.
- Handle errors gracefully, including invalid usernames or rate-limiting errors.
- Simple and lightweight implementation without external libraries.

## Prerequisites

- Python 3.7 or higher
- Internet connection
- GitHub username to fetch activity for

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory
    ```bash
   cd github-user-activity-cli
   ```

## Usage

Run the application with the following command.
   ```bash
    python index.py  <github-username>
   ```

# Output Example
    ```bash
    Recent activity for GitHub user 'ralphjsmit'.
    -- IssueComment in ralphjsmit/laravel-glide
    -- PullRequest in spatie/package-skeleton-laravel
    -- Pushed 1 commits to ralphjsmit/package-skeleton-laravel
    -- Pushed 1 commits to ralphjsmit/package-skeleton-laravel
    -- Create in ralphjsmit/package-skeleton-laravel
    -- Fork in spatie/package-skeleton-laravel
    -- IssueComment in laravel-idea/plugin
    --Opened issue '[Bug]: Translation variables not correctly cased' in laravel-idea/plugin
    -- IssueComment in ralphjsmit/laravel-seo
    -- PullRequestReviewComment in filamentphp/filamentphp.com

    ```
