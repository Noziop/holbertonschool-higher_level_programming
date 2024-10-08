#!/usr/bin/python3
'''module for student class'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initializes student instance'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''returns dictionary representation of student instance'''
        return self.__dict__
