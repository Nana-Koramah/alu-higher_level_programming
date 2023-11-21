#!/usr/bin/python3
"""Define a square"""


class Rectangle():
    """Represent a square"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        """initialize a new square"""

    @property
    def width(self):
        """retrieve the width of the square"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the square"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height of the square"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
