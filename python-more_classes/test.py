#!/usr/bin/python3


class Person:
    '''person's def'''
    def __init__(self, name='none', age='0') -> None:
        self.name = name
        self.age = age

    @property
    def name(self, value):
        if not isinstance(self, value):
            raise TypeError("bal bla bla string")
        return self.name
    
    