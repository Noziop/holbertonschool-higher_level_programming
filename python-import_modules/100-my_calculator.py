#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

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
            sys.exit(1)
        result = div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
