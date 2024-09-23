#!/usr/bin/python3
'''This module contains a class named VerboseList'''


class VerboseList(list):
    '''This class extends the list class to print messages.'''
    def append(self, item):
        '''This method appends an item to the list.'''
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        '''This method extends the list with an iterable.'''
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        '''This method removes an item from the list.'''
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        '''This method pops an item from the list.'''
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)