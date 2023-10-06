#!/usr/bin/python3
"""
    Pascal's Triangle function
    that returns a list of list of integers
    representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Pascal Triangle function"""

    if n <= 0:
        return []

    out_list = [[1]]

    for i in range(n - 1):
        n_list = [1]
        for j in range(i):
            value = out_list[i][j] + out_list[i][j + 1]
            n_list.append(value)
        n_list.append(1)
        out_list.append(n_list)

    return out_list
