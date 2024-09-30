#!/usr/bin/python3
'''module for student class'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initializes student instance'''
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}
