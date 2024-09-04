#!/usr/bin/python3

def remove_char_at(string, n):
    """remove character at index n

    Args:
        string (string): string to remove character from
        n (int): index to remove character from

    Returns:
         : string
    """
    if n < 0 or n >= len(string):
        return string
    else:
        return string[:n] + string[n+1:]
