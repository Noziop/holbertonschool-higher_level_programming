#!/usr/bin/python3
'''Module for Square class'''


class Square:
    '''A simple Square class'''
    def __init__(self, size=0):
        '''Initialization of instance attributes'''
        self.size = size

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Calculates the area'''
        return self.__size ** 2

    def my_print(self):
        '''Prints the square'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
