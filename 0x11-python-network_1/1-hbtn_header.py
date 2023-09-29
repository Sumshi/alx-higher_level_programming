#!/usr/bin/python3


""" script that fetches url"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
