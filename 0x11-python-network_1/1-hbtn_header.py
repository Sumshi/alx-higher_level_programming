# #!/usr/bin/python3


""" script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

if __name__ == "__main__":
    sys.argv[1] = url  # url from command line
    with urllib.request.urlopen(url) as response:
        header_value = response.getheader('X-Request-Id')
        print(header_value)
