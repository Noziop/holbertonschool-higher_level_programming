#!/usr/bin/python3
'''This module contains a function that returns True if the object
 is an instance of, or if the object is an instance of a class that
 inherited from, the specified class; otherwise False.'''


def inherits_from(obj, a_class):
    '''This function returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.'''
    return isinstance(obj, a_class) and type(obj) is not a_class
