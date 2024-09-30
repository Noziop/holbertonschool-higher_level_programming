#!/usr/bin/python3
'''module for basic serialization'''


import json

def serialize_and_save_to_file(data, filename):
    '''function to serialize and save data to a file'''
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    '''function to load and deserialize data from a file'''
    with open(filename, 'r') as file:
        return json.load(file)