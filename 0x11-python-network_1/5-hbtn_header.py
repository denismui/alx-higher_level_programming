#!/usr/bin/python3
"""
Python script that sends a request to a URL and
displays the value of a variable in the response header
"""
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
