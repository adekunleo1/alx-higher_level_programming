#!/usr/bin/python3
"""
    Python Script using the GitHub API to display a GitHub ID based on given credentials.
    Usage: ./10-my_github.py <Github Username> <Github Password> in this case a personal access token is required.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
