#!/usr/bin/python3
""" Square module """

class Square:
    """ A square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Initialize the square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        # Ensure the square's area uses the `width` dimension only for a perfect square
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ The perimeter of the square """
        # Use `width` only for the perimeter of a perfect square
        return self.width * 4

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)  # Instantiate the class
    print(s)  # Print the string representation
    print(s.area_of_my_square())  # Print the area
    print(s.perimeter_of_my_square())  # Print the perimeter
