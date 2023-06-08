#!/usr/bin/python3
import sys

total = 0
args = sys.argv
if len(args) > 1:  # excludes program name
    for arg in sys.argv[1:]:
        total = total + int(arg)
print(total)
