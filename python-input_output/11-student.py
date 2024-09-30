#!/usr/bin/python3
'''module for student class'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initializes student instance'''
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            setattr(self, key, value)
