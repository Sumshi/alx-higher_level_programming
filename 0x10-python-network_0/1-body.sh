#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response

URL=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$response" -eq 200 ]; then
    curl -s "$URL"
fi

