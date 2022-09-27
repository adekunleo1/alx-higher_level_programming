#!/usr/bin/python3
""" To Fetch https:alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as url_o:
        read_url = url_o.read()
        print("Body response:")
        print("\t- type:", type(read_url))
        print("\t- content:", read_url)
        print("\t- utf8 content:", read_url.decode("utf-8"))
