#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == '+':
        result = add(a, b)
        print(f"{a} + {b} = {result}")
    elif operator == '-':
        result = sub(a, b)
        print(f"{a} - {b} = {result}")
    elif operator == '*':
        result = mul(a, b)
        print(f"{a} * {b} = {result}")
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            exit(1)
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
