#!/usr/bin/python3

"""
    File containing a Square class that have multiple
    attributes and methods.
"""


class Square:
    """Class that describes a Square with properties."""

    def check_and_set_size(self, size):
        """Checks if the size is a correct argument and sets it"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def check_and_set_position(self, position):
        """Checks if position is a correct argument and sets it"""
        if isinstance(position, tuple) and len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                self.__position = position
            else:
                msg = "position must be a tuple of 2 positive integers"
                raise TypeError(msg)
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """
            Init method that initializes each object (instance) of the class
            with __size being a private attribute. It raises an error if the
            passed size is not ar integer or if it's less than 0.
        """
        self.check_and_set_size(size)
        self.check_and_set_position(position)

    @property
    def size(self):
        """Getter method that returns the private __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method that sets the private attribute __size"""
        self.check_and_set_size(value)

    @property
    def position(self):
        """Setter method that sets the private attribute __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Getter method that returns the private __position"""
        self.check_and_set_position(value)

    def area(self):
        """Returns the area of the Square multiplying size * size"""
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square using muliples '#' characters
            and add spaces using the position tuple
        """
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print(""*self.__position[1])
            for i in range(self.__size):
                print(" "*self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
