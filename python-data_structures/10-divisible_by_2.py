#!/usr/bin/python3
# a function that finds all multiples of 2 in a list.


def divisible_by_2(my_list=[]):
    x = my_list
    for x in range(len(my_list)):
        if x/2 == 0:
            return True
            print("x is divisible by 2")
        else:
            return False
            print("x is not divisible by 2")