#!/usr/bin/python3
for i in range(100):
    if i == 99:  # last element
        print("{:02d}".format(i))
        break
# if i is not egual to 99
    print("{:02d}, ".format(i), end="")
