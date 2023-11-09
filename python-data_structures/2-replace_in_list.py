#!/usr/bin/python3
# This code is a function that replaces an element of a list at a position


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
            my_list[idx] = element
    return (my_list)
