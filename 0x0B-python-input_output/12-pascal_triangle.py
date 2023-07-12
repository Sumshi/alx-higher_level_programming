#!/usr/bin/python3
"""This defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """This represents Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    else:
        triangle = [[1]]
        for i in range(1, n):
            row = [1] # first element
            previous_row = triangle[i - 1]
            for j in range(1, i): # second last element
                row.append(previous_row[j-1] + previous_row[j])
            row.append(1)
            triangle.append(row)

        return (triangle)
