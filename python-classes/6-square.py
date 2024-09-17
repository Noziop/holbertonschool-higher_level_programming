#!/usr/bin/python3
'''Module for Square class'''


class Square:
    '''A simple Square class'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of instance attributes'''
        self.size = size
        self.position = position

    def area(self):
        '''Calculates the area'''
        return self.__size ** 2

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

        @property
    def position(self):
        '''Getter method for position'''
        return self.__position

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        '''Setter method for position'''
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''Prints the square'''
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
