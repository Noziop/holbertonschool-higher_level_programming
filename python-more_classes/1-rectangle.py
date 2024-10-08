#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''Class that defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''Initialization of instance attributes'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for width attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for height attribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
