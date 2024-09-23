#!/usr/bin/python3
'''This module contains a class named CountedIterator'''


class CountedIterator:
    '''This class counts the number of items returned by an iterator.'''
    def __init__(self, iterable):
        '''This method initializes the iterator and count.'''
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        '''This method returns the next item from the iterator.'''
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        '''This method returns the number of items returned by the iterator.'''
        return self.count
