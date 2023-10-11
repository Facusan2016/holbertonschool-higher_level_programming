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
        """Method that converts a Json to an String."""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) <= 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that saves a Json representation to a file"""
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string(None))
            else:
                res = []
                for obj in list_objs:
                    res.append(obj.to_dictionary())
                f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Loads a python object from json string."""
        if json_string is None or len(json_string) == 0:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls is not Base:
            new_instance = cls(1, 1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        f_name = cls.__name__ + ".json"
        try:
            obj_lst = []
            with open(f_name, "r") as f:
                for line in f:
                    dict_obj = cls.from_json_string(line)
                    for obj in dict_obj:
                        n_obj = cls.create(**obj)
                        obj_lst.append(n_obj)

            return obj_lst

        except FileNotFoundError:
            return ([])
