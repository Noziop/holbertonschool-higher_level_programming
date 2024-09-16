#!/usr/bin/python3
'''Module for singly linked list'''


class Node:
    '''A simple Node class'''
    def __init__(self, data, next_node=None):
        '''Initialization of instance attributes'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Getter for data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Setter for data'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''Getter for next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Setter for next_node'''
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
