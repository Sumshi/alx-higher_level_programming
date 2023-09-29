#!/usr/bin/python3


"""  script that takes in a URL, sends a request to the URL """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    response = requests.get(url)
    header_value = response.headers.get('X-Request-Id')
    print(header_value)
