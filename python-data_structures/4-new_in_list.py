#!/usr/bin/python3
# This is a function that replaces an element in a list without changing original list.


def new_in_list(my_list, idx, element):
    if idx < 0:
        if idx > (len(my_list) - 1):
              return my_list.copy()
        else:
            new_list = my_list.copy()
            new_list[idx] = element
            return new_list
