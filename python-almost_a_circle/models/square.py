#!/usr/bin/python3

"""
    This module contains the declaration of
    the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """Class Square declaration"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init method of Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str method of Square class."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Size property getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size property setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        """Update the attributtes using args or kwargs."""

        if args and len(args) > 0:

            opt_args = ["id", "size", "x", "y"]

            for count, arg in enumerate(args):
                setattr(self, opt_args[count], arg)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Square to dictionary implementation"""
        representation = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }

        return representation
