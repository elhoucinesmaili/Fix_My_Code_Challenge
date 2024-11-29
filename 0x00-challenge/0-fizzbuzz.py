#!/usr/bin/python3
"""
FizzBuzz: Prints numbers from 1 to n with substitutions for multiples.
"""
import sys


def fizzbuzz(n):
    """
    Print the FizzBuzz sequence from 1 to n.

    - Print "Fizz" for multiples of 3.
    - Print "Buzz" for multiples of 5.
    - Print "FizzBuzz" for multiples of both 3 and 5.
    - Print the number itself otherwise.
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # Multiples of both 3 and 5
            result.append("FizzBuzz")
        elif i % 3 == 0:  # Multiples of 3
            result.append("Fizz")
        elif i % 5 == 0:  # Multiples of 5
            result.append("Buzz")
        else:
            result.append(str(i))
    
    # Print the result as a single space-separated string
    print(" ".join(result))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing or extra arguments")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 15")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 1:
            print("Please provide a positive integer greater than 0")
            sys.exit(1)
        fizzbuzz(number)
    except ValueError:
        print("Invalid input: Please provide a valid integer")
        sys.exit(1)
