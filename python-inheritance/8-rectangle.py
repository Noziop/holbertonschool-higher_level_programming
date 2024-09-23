#!/usr/bin/python3
'''This module contains a class named Rectangle
    that inherits from BaseGeometry.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This class inherits from BaseGeometry.'''
    def __init__(self, width, height):
        '''This method initializes an instance of Rectangle.'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
