#!/usr/bin/python3
"""
    Module definition for is_same_class function
    that checks what is mentioned down.

"""


def is_kind_of_class(obj, a_class):
    """
        Function that returns True if obj is
        an instance of the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
