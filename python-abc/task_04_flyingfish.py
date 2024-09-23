#!/usr/bin/python3
'''This module contains a class named Fish, a class named Bird, and a class named FlyingFish'''


class Fish:
    '''This class represents a Fish.'''
    def swim(self):
        '''This method makes the fish swim.'''
        print("The fish is swimming")

    def habitat(self):
        '''This method describes the fish's habitat.'''
        print("The fish lives in water")


class Bird:
    '''This class represents a Bird.'''
    def fly(self):
        '''This method makes the bird fly.'''
        print("The bird is flying")

    def habitat(self):
        '''This method describes the bird's habitat.'''
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''This class represents a FlyingFish.'''
    def fly(self):
        '''This method makes the flying fish fly.'''
        print("The flying fish is soaring!")

    def swim(self):
        '''This method makes the flying fish swim.'''
        print("The flying fish is swimming!")

    def habitat(self):
        '''This method describes the flying fish's habitat.'''
        print("The flying fish lives both in water and the sky!")
