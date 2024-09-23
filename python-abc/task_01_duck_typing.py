#!/usr/bin/python3
'''This module contains a class named Shape and its subclasses'''


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''This is an abstract base class for shapes.'''
    @abstractmethod
    def area(self):
        '''This method should be implemented by subclasses.'''
        pass

    @abstractmethod
    def perimeter(self):
        '''This method should be implemented by subclasses.'''
        pass


class Circle(Shape):
    '''This class represents a Circle.'''
    def __init__(self, radius):
        '''This method initializes a Circle.'''
        self.radius = radius

    def area(self):
        '''This method returns the area of the Circle.'''
        return math.pi * self.radius ** 2

    def perimeter(self):
        '''This method returns the perimeter of the Circle.'''
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    '''This class represents a Rectangle.'''
    def __init__(self, width, height):
        '''This method initializes a Rectangle.'''
        self.width = width
        self.height = height

    def area(self):
        '''This method returns the area of the Rectangle.'''
        return self.width * self.height

    def perimeter(self):
        '''This method returns the perimeter of the Rectangle.'''
        return 2 * (self.width + self.height)


def shape_info(shape):
    '''This function prints the area and perimeter of a shape.'''
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
