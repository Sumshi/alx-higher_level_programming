#!/usr/bin/python3
import requests
import json

response = requests.get('https://www.tutorialspoint.com/http/http_methods.htm')
print(response.json())