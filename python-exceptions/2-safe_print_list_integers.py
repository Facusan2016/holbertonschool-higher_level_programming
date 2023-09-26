#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = it = 0
    while it < x:
        try:
            print("{:d}".format(my_list[it]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        it += 1
    print()
    return count
