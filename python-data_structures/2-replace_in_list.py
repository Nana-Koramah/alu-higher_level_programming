#!/usr/bin/python3
# This code is a function that replaces an element of a list at a specific postion.
def replace_in_list(my_list, idx, element):
    if not (idx < 0 or idx > (len(my_list) - 1)):
        my_list[idx] = element
    else:
        return my_list
