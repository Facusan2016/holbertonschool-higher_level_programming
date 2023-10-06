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

    def to_json(self):
        return self.__dict__
