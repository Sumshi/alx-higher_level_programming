#!/usr/bin/python3


"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests  # for making http requests
import sys  # for command line arguments

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
