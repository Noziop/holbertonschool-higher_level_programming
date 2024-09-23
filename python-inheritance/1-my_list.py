#!/usr/bin/python3
'''This module creates a class named MyList that inherits from list.'''


class MyList(list):
    '''This class inherits from list.'''
    def print_sorted(self):
        '''Prints the list sorted.'''
        print(sorted(self))
