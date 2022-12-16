#!/usr/bin/python3
"""
Script that sends a POST request and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    email = sys.argv[2]
    url = sys.argv[1]
    mail = urllib.parse.urlencode({"email": email})
    mail = mail.encode('ascii')
    post = urllib.request.Request(url, mail)
    with urllib.request.urlopen(post) as url_o:
        print(url_o.read().decode('utf-8'))
