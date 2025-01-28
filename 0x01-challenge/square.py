#!/usr/bin/python3
""" Square module """


class Square:
    """Square class"""

    def __init__(self, width=0, height=0):
        """Initialize the square with width and height"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Calculate area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Calculate perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=8)  # Example values
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
