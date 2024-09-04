#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(args[0])
    b = int(args[2])
    if args[1] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif args[1] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif args[1] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif args[1] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
