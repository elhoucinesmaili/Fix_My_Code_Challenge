#!/usr/bin/python3
"""
FizzBuzz
    A simple FizzBuzz implementation.
"""

import sys


def fizzbuzz(n):
    """
    Prints numbers from 1 to n, replacing:
    - Multiples of 3 with "Fizz".
    - Multiples of 5 with "Buzz".
    - Multiples of both 3 and 5 with "FizzBuzz".
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i, end=" ")
    print()  # Newline after the loop


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Invalid input: Please enter an integer.")
        sys.exit(1)

    fizzbuzz(number)
