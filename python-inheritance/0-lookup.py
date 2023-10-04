#!/usr/bin/python3
"""
    Module that declare a funciton that returns the list of available
    attributes and methods of an object.
"""


def lookup(obj):
    """
        Class that returns the list of attributes and methods.
    """
    return dir(obj)
