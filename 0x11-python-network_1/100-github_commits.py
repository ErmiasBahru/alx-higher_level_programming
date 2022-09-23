#!/usr/bin/python3
"""
Python script that list 10 commits (from the most recent to oldest) of the repository
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    res = requests.get(url)
    commits = res.json()
    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except IndexError:
        pass
