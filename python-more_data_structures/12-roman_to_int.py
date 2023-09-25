#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or None:
        return 0
    total = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ls = len(roman_string)
    for i in range(ls):
        if i + 1 < ls and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            total -= roman[roman_string[i]]
        else:
            total += roman[roman_string[i]]
    return total
