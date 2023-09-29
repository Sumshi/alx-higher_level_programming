#!/usr/bin/python3


"""  script that takes in a URL, sends a request to the URL """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    response = requests.get(url)
    data = response.text
    print(data)
