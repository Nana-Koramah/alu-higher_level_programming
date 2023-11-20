#!/usr/bin/python3
"""Defines a square with a private instance attritube:size and no type verification"""


class Square():
    """Represent a square"""

    def __init__(self, size):
        """initialize a new square"""

        self.__size = size
        
