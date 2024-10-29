#!/usr/bin/python3
'''Module for Rectangle class'''


class Dog:
    def __init__(self, species='none', name='none', age=0):
        self.species = species
        self.name = name
        self.age = age

    @property
    def species(self):
        return self.__species
    
    @species.setter
    def species(self, value):
        if not isinstance(value, str):
            raise TypeError("species must be a string")
        self.__species = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value < 0:
            raise ValueError("age must be >= 0")
        self.__age = value


    def bark(self):
        print("Woof!")
    
    def sit(self):
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")
    