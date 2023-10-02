#!/usr/bin/python3
"""
    Module that contains the Rectangle class definition.
    with their respective attributes and methods.
"""


class Rectangle:
    """Class that defines a Rectangle."""
    def __init__(self, width=0, height=0):
        """
            Initializes the instance of the class
            setting width and height as private attributes.

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method for __width that returns """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for __width that sets"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for __height that returns"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for __height that sets"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
