#!/usr/bin/python3

# program that prints numbers from 0 to 99
for num in range(100):
    print(f"{num:02}", end=", " if num < 99 else "\n")