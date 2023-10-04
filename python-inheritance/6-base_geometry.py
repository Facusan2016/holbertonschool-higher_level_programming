#!/usr/bin/python3
"""
    Module that declares the BaseGeometry class

"""


class BaseGeometry():
    """BaseGeometry class that has methods and attributes."""
    def area(self):
        """Method that raises an error if area is not defined."""
        raise Exception('area() is not implemented')
