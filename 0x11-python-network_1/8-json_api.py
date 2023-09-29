#!/usr/bin/python3


"""
script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import requests  # for making http requests
import sys  # for command line arguments

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    # check if argument is provided
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    response = requests.post(url, data=data)
    # parse the response
    try:
        parsed_response = response.json()
        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                  "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
