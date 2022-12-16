#!/usr/bin/python3
"""'
    Script that sends a POST request and displays the body of the response
    Using requests
"""
import requests
import sys


if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    url = sys.argv[1]
    post = requests.post(url, data=email)
    print(post.text)
