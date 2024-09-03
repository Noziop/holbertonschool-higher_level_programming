#!/usr/bin/python3

# function that prints the numbers from 1 to 100 separated by a space
# for multiples of three print Fizz instead of the number
# for multiples of five print Buzz instead of the number
# for numbers which are multiples of both three and five print FizzBuzz
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
    print()
