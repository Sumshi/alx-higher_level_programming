#!/bin/bash
#  takes in a URL as an argument, sends a GET request to the URL,
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
