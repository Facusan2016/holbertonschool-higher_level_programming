#!/usr/bin/python3
def uppercase(str):
    for c in str:
        up_c = c
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            up_c = chr(ord(c) - 32)

        print("{}".format(up_c), end="")
    else:
        print()
