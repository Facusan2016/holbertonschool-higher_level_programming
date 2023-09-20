#!/usr/bin/python3
def no_c(my_string):
    lst = []
    for c in my_string:
        if c != 'c' and c != 'C':
            lst.append(c)
    return ''.join(lst)
