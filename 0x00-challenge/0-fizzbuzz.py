#!/usr/bin/python3
"""
FizzBuzz Challenge
"""
import sys


def fizzbuzz(n):
    """
    Prints numbers from 1 to n separated by a space, with substitutions:
    - "Fizz" for multiples of 3,
    - "Buzz" for multiples of 5,
    - "FizzBuzz" for multiples of both 3 and 5.
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        result.append(output if output else str(i))
    
    print(" ".join(result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing or invalid number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("The argument must be an integer.")
        sys.exit(1)
