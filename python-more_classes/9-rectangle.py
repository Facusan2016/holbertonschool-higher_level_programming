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
        type(self).number_of_instances += 1

    number_of_instances = 0
    print_symbol = "#"

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

    def area(self):
        """Method that returns the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Method that returns the perimeter of the rectangle."""
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        """Returns a Rectangle representation using #"""
        new_str = ""
        if self.height == 0 or self.width == 0:
            return ""
        for _ in range(self.height):
            for _ in range(self.width):
                new_str += str(type(self).print_symbol)
            new_str += "\n"

        new_str = new_str[:-1]

        return new_str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
            Class method to create a new rectangle of size
        """
        return cls(size, size)
