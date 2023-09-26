#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    i = 0
    while i < list_length:
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            i += 1
            n_list.append(res)

    return n_list
