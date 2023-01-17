#!/usr/bin/python3
"""A script that:
    - takes in a URL,
    - sends a request to the URL and displays the value
    - of the X-Request-Id variable found in the header of the reponse"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as reponse:
        print(dict(response.headers).get("X-Request-Id"))
