#!/usr/bin/python3
"""
    Script using the GitHub API to display a GitHub ID based on given credentials.
    Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    payload = {'login': sys.argv[1]}
    response = requests.get(url, params=payload, auth=(
        sys.argv[1], sys.argv[2])).json()

    try:
        print(response['id'])
    except KeyError:
        print('None')
