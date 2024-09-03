#!/usr/bin/python3

# function that prints the last digit of a number
def print_last_digit(number):
    if number < 0:
        number = -number
    print("{:d}".format(number % 10), end="")
    return number % 10