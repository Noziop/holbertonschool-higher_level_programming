#!/usr/bin/python3
def islower(c):
    """Function to check if a character is lowercase
    args: c character to check
    return: True if c is lowercase, False otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
