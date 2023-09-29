#!/usr/bin/python3
"""
    This module defines an add function
    and it's tested on /tests folder.

"""


def add_integer(a, b=98):
    """
    Adds a and b just if they're int or floats,
    """
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')

    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return a + b
