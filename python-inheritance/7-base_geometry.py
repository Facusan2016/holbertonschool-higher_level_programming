#!/usr/bin/python3
"""
    Module that declares the BaseGeometry class

"""

class BaseGeometry():
    """BaseGeometry class that has methods and attributes."""
    def area(self):
        """Method that raises an error if area is not defined."""
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """
            Method that validates value checking if it's an
            integer and if it's greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
