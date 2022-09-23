#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a
parameter
"""

import requests
from sys import argv

if __name__ == "__main__":
    q_value = "" if len(argv) == 1 else argv[1]
    values = {
        'q': q_value
    }
    url = "http://0.0.0.0:5000/search_user"
    resp = requests.post(url, data=values)
    try:
        json = resp.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
