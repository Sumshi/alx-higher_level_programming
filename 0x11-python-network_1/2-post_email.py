#!/usr/bin/python3


""" script that takes in a URL and an email, sends a POST request to the url"""
import urllib.request  # for making http requests
import urllib.parse  # for url encoding
import sys  # for command line arguments

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    email = sys.argv[2]
    data = {'email': email}
    # encodes the data dictionary
    data_encoded = urllib.parse.urlencode(data).encode('ascii')
    # creating a post request using Request class
    with urllib.request.urlopen(url, data=data_encoded) as response:
        # read the response and retrieves body as bytes
        body = response.read().decode('utf-8')
        print(body)
