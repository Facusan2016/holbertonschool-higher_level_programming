#!/usr/bin/python3

"""
    File containing a Square class that have multiple
    attributes and methods.
"""


class Square:
    """Class that describes a Square with properties."""

    def check_if_valid_size(self, size):
        """Returns the area of the Square multiplying size * size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __init__(self, size=0):
        """
            Init method that initializes each object (instance) of the class
            with __size being a private attribute. It raises an error if the
            passed size is not ar integer or if it's less than 0.
        """
        self.check_if_valid_size(size)

    @property
    def size(self):
        """Getter method that returns the private __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method that sets the private attribute __size"""
        self.check_if_valid_size(value)

    def area(self):
        """Returns the area of the Square multiplying size * size"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square using muliples '#' characters"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
