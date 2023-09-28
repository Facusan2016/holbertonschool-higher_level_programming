#!/usr/bin/python3

"""
    File containing a Square class that have multiple
    attributes and methods.
"""


class Square:
    """Class that describes a Square with properties."""

    def __init__(self, size):
        """
            Init method that initializes each object (instance) of the class
            with __size being a private attribute.
        """
        self.__size = size
