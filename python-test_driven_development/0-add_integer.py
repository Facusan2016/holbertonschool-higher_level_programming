#!/usr/bin/python3
"""
    This module defines an add function
    and it's tested on /tests folder.

"""


def add_integer(a, b=98):
    """
    Adds a and b just if they're int or floats,
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
