#!/usr/bin/python3

"""
    File containing a Square class that have multiple
    attributes and methods.
"""


class Square:
    """Class that describes a Square with properties."""

    def __init__(self, size=0):
        """
            Init method that initializes each object (instance) of the class
            with __size being a private attribute. It raises an error if the
            passed size is not ar integer or if it's less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
