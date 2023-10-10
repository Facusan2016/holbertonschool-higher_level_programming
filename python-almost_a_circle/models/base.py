#!/usr/bin/python3
"""
    This module contains the declaration of the base class
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string(None))
            else:
                res = []
                for obj in list_objs:
                    res.append(obj.__dict__)
                f.write(cls.to_json_string(res))
