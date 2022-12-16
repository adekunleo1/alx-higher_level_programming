#!/usr/bin/python3
"""
    Script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    args = sys.argv[1] if len(sys.argv) >= 2 else ""

    post = requests.post(url, {"q": args})
    try:
        json_p = post.json()
        if not json_p:
            print("No result")
        else:
            print("[{}] {}".format(json_p["id"], json_p["name"]))
    except Exception as e:
        print("Not a valid JSON")
