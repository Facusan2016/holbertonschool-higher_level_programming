#!/usr/bin/python3
"""
    This module contains the declaration of the base class
"""


class Base:
    """Declaration of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method."""
        if id is None:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
