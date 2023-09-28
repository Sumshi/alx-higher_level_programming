#!/bin/bash
#Takes in a URL and send a request to it and returns number of bytes
curl -s "$1" | wc -c
