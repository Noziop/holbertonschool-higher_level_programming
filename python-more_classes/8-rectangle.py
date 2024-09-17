#!/usr/bin/python3
'''Module for Rectangle class'''


class Rectangle:
    '''Class that defines a rectangle'''
    number_of_instances = 0  # Class attribute to keep track of instances
    print_symbol = "#"  # Class attribute to print the rectangle

    def __init__(self, width=0, height=0):
        '''Initialization of instance attributes'''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''Return the area of the rectangle'''
        return self.width * self.height

    def perimeter(self):
        '''Return the perimeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        '''Returns a string representation of the rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(str(self.print_symbol) *
                         self.width for _ in range(self.height))

    def __repr__(self):
        '''Returns a string representation of the rectangle'''
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        '''Prints a message when an instance of Rectangle is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the biggest rectangle based on the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def square(cls, size=0):
        '''Returns a new Rectangle instance with width == height == size'''
        return cls(size, size)
