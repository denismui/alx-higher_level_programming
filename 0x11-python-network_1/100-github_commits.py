#!/usr/bin/python3
"""
Python script that uses Github API to list 10 previous commits
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/repos/' + sys.argv[2] + '/' + sys.argv[1] + \
            '/commits'
    r = requests.get(url)
    try:
        for i in range(10):
            print("{}: {}".format(r.json()[i]['sha'],
                                    r.json()[i]['commit']['author']['name']))
    except Exception:
        pass
