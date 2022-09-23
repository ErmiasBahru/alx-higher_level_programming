#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=HTTPBasicAuth(user, token))
    json = resp.json()
    print(json.get('id'))
