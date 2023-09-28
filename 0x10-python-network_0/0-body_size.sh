#!/bin/bash
# takes in a url and sends it a reguest
# sends a get reguest to the url
#curl -s "$1" | wc -c

URL=$1 # first command line argument
#get reguest to the url provided
response=$(curl -sI "$URL") # -s for silent mode, -I fetches only response headers and not body
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')
echo "$content_length"

