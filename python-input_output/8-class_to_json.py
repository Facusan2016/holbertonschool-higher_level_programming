#!/usr/bin/python3

"""
    Write a function that returns the dictionary
    description with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object:
"""

import json


def class_to_json(obj):
    """Function that converts class to json"""
    return json.dumps(dict(obj.__dict__))
