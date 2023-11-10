#!/usr/bin/python3
# a function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    matrix = []
    for row in matrix:
        for col in row:
            if col != row[-1]:
                print("{:d}".format(col), end="")
            else:
                print()
