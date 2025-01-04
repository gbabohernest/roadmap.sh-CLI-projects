#!/usr/bin/env python

import sys
from get_user_activity import fetch_github_user_activity


if __name__ == "__main__":
    if len(sys.argv )!= 2:
        print(f"Please enter your github username:")
        sys.exit()

    username = sys.argv[1]
    fetch_github_user_activity(username)