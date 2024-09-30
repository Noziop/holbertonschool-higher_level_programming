#!/usr/bin/python3
'''module for add_item function'''


import sys
import os.path


def add_item(filename, *args):
    '''adds all arguments to a Python list, and then save them to a file'''
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_json_file = __import__('6-load_from_json_file').load_from_json_file

    if os.path.exists(filename):
        my_list = load_json_file(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":

    filename = "add_item.json"

    add_item(filename, *sys.argv[1:])
