#!/usr/bin/python3


""" script that fetches url"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    email = sys.argv[2]
    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')
    # creating a post request
    request = urllib.request.Request(url, data)
    # handle the response
    with urllib.request.urlopen(request) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", email)
