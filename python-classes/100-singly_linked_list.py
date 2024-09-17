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


class SinglyLinkedList:
    '''A singly linked list class'''
    def __init__(self):
        '''Initialization of the linked list'''
        self.__head = None

    def sorted_insert(self, value):
        '''Insert a new Node into the correct sorted position'''
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        '''String representation of the linked list'''
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
