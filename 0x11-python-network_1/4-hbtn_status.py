#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    response = response.text
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
