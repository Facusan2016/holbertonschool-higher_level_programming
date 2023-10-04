#!/usr/bin/python3

"""
    Module that defines the Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Init method to initialize the Square using the super class"""
        super().__init__(size, size)
