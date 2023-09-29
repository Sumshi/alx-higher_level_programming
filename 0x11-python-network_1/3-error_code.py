#!/usr/bin/python3


"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import urllib.request  # for making http requests
import urllib.error  # for url encoding
import sys  # for command line arguments

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # handling HTTP error exception
        print("Error code:", e.code)
