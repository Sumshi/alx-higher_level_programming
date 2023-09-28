#!/bin/bash
# takes in a url and sends it a reguest
# sends a get reguest to the url
curl -s "$1" | wc -c