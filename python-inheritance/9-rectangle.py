#!/usr/bin/python3
'''This module contains a class named Rectangle
    that inherits from BaseGeometry.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    '''This class inherits from BaseGeometry.'''
    def __init__(self, width, height):
        '''This method initializes an instance of Rectangle.'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        '''This method validates the value.'''
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')

    def area(self):
        '''This method returns the area of the rectangle.'''
        return self.__width * self.__height

    def __str__(self):
        '''This method returns a string representation of the rectangle.'''
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
