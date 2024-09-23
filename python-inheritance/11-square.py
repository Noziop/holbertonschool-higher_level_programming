#!/usr/bin/python3
'''This module contains a class named Square that inherits from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''This class inherits from Rectangle'''
    def __init__(self, size):
        '''This method initializes an instance of Square'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''This method returns the area of the square'''
        return self.__size ** 2

    def __str__(self):
        '''This method returns a string representation of the square.'''
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
