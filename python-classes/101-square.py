#!/usr/bin/python3
'''Module for Square class'''


class Square:
    '''A simple Square class'''
    def __init__(self, size=0):
        '''Initialization of instance attributes'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculates the area'''
        return self.__size ** 2

    @property
    def size(self):
        '''Getter for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def __lt__(self, other):
        '''Less than'''
        return self.area() < other.area()
    def __le__(self, other):
        '''Less than or equal'''
        return self.area() <= other.area()
    def __eq__(self, other):
        '''Equal to'''
        return self.area() == other.area()
    def __ne__(self, other):
        '''Not equal to'''
        return self.area() != other.area()
    def __gt__(self, other):
        '''Greater than'''
        return self.area() > other.area()
    def __ge__(self, other):
        '''Greater than or equal'''
        return self.area() >= other.area()
    def __str__(self):
        '''String representation of the square'''
        return "#" * self.__size
    def __repr__(self):
        '''String representation of the square'''
        return "Square({})".format(self.__size)
