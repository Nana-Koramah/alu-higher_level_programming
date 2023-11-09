#!/usr/bin/python3
# This is a function that prints all integers of a list in reverse.
def print_reversed_list_integer(my_list=[]):
     for i in range(my_list)-1, -1, -1):
         print("{:d}".format(my_list[i]))
