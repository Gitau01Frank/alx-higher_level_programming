#!/usr/bin/python3
""" Defines class BaseGeometry"""


class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        """raise Exception error"""
        raise Exception("area() is not implemented yet")

    def integer_validation(self, name, value):
        """value validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
