#!/usr/bin/python3
def uppercase(str):
    """change a string to uppercase

    Args:
        str (sting): string to change to uppercase
    """
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
