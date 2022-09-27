#!/usr/bin/python3
"""
 Script that sends a request to the URL and displays the value of the
 X-Request-Id variable found in the header of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    url_o = requests.get(url)
    if "X-Request-Id" in url_o.headers:
        print(url_o.headers["X-Request-Id"])
    else:
        print(None)
