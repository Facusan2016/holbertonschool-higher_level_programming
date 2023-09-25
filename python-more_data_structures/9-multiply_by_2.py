#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d_copy = dict(a_dictionary)
    d_copy.update((key, value * 2) for key, value in a_dictionary.items())
    return d_copy
