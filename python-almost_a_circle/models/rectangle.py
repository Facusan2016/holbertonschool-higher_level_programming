#!/usr/bin/python3

"""
    This module contains the declaration of
    the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """Declaration of Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Str Method"""
        p_str = f"({self.id}) {self.x}/{self.y}"
        w_str = f"{self.width}/{self.height}"
        return f"[Rectangle] {p_str} - {w_str}"

    @property
    def width(self):
        """Getter method for __width that returns """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for __width that sets"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for __height that returns"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for __height that sets"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter method for __x that returns"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for __x that sets"""
        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method for __y that returns"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for __y that sets"""
        if type(value) is not int:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area"""
        return self.height * self.width

    def display(self):
        """Show a representation of Rectangle using #"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" "*self.x, end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the attributtes using args or kwargs."""
        if args and len(args) > 0:

            opt_args = ["id", "width", "height", "x", "y"]

            for count, arg in enumerate(args):
                setattr(self, opt_args[count], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To dictionary implementation"""
        representation = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

        return representation
