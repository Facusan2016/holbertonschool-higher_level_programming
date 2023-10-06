#!/usr/bin/python3
"""
    Write a function that returns an Object
    from a JSON representation.
"""


import json


def from_json_string(my_str):
    """Function that converts an str to object."""
    return json.loads(my_str)
