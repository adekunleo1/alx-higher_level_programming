#!/usr/bin/python3
"""
     Script that Fetches https:alx-intranet.hbtn.io/status using requests
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    read_url = requests.get(url)
    print("Body response:")
    print("\t- type:", type(read_url.text))
    print("\t- content:", read_url.text)
