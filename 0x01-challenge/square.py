#!/usr/bin/python3
""" Square module """


class Square():
    """ A square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ the init for the square class """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """ the perimeter of the square """
        return 2 * (self.width + self.height)

    def __str__(self):
        """ the str repr """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
