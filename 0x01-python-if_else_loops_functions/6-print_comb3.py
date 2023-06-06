#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):  # ensures second digit is always greater
        if x == 8 and y == 9:
            print('89')  # last number
        else:
            print('{}{}, '.format(x, y), end='')
