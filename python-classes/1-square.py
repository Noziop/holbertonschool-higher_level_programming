#!/usr/bin/python3
'''Module for Square class'''


class Square:
    '''A simple Square class'''
    def __init__(self, size):
        '''Initialization of instance attributes'''
        self.__size = size 

    def width(self):
        '''Getter method for size'''
        return self.__size
    
    def width(self, value):
        '''Setter method for size'''
        self.__size = value

    def height(self):
        '''Getter method for size'''
        return self.__size
    
    def height(self, value):
        '''Setter method for size'''
        self.__size = value
