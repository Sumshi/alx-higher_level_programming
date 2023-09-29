#!/usr/bin/python3


""" script that fetches url"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    email = sys.argv[2]
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Your email is:", email)
