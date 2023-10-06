#!/usr/bin/python3

"""
    Module that define the Student class
"""


class Student:

    """
        Student class that has first_name
        last_name and age attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if type(attrs) is list:
            if all(isinstance(item, str) for item in attrs):
                cls_dict = dict(self.__dict__)
                filt_dict = {k: v for (k, v) in cls_dict.items() if k in attrs}
                return filt_dict

        return self.__dict__
