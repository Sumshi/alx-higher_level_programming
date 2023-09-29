#!/usr/bin/python3


""" script that takes in a URL and an email, sends a POST request to the url"""
import requests  # for making http requests
import sys  # for command line arguments

if __name__ == "__main__":
    url = sys.argv[1]  # url from command line
    email = sys.argv[2]
    data = {'email': email}
    # creating a post request using Request class
    response = requests.post(url, data=data)
    print(response.text)
