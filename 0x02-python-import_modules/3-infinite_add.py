#!/usr/bin/python3
if __name__ == "__main__":
    import sys
total = 0
args = sys.argv
if len(args) > 1:  # excludes program name
    for arg in sys.argv[1:]:  # starts from second argument
        total = total + int(arg)
print(total)
