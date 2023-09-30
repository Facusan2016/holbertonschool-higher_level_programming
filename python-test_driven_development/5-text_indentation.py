#!/usr/bin/python3
"""
    This module contains the text_indentation function
    that it's tested on tests/5-text_indentation.txt

"""


def text_indentation(text):
    r"""Function that replaces . ? and : for \n\n"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    n_text = text.replace(". ", ".\n\n")
    n_text = n_text.replace("? ", "?\n\n").replace(": ", ":\n\n")
    print(n_text)
