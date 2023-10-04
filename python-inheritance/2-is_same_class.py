#!/usr/bin/python3
"""
    Module definition for is_same_class function
    that checks what is mentioned down.

"""


def is_same_class(obj, a_class):
    """
        Function that returns True if obj is exactly
        an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
