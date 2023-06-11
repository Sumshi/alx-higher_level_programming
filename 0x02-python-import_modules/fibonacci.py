#!/usr/bin/python3
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1  # a = 0, b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b  # a = b, b = a+b
    print()

import fibo
fib(100)
