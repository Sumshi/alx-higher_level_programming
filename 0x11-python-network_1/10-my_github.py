#!/usr/bin/python3


"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests  # for making http requests
import sys  # for command line arguments
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # username and password from command line
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    # authentication
    auth = HTTPBasicAuth(username, password)
    # sending a get request to github API
    response = requests.get(url, auth=auth)
    # print users github id
    print(response.json().get("id"))
