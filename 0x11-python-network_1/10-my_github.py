#!/usr/bin/python3
"""
    Python Script using the GitHub API to display a GitHub ID based on given credentials.
    Usage: ./10-my_github.py <Github Username> <Github Password> in this case a personal access token is required.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print('None')
