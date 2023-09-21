#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            condition = row.index(column) == len(row) - 1
            print("{:d}".format(column), end="" if condition else " ")
        print()
