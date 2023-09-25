#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for c in set(my_list):
        total += c
    return total
