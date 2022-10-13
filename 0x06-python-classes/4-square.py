#!/usr/bin/python3
"""class Square"""


class Square:
    """initializing private size attribute"""
    def __init__(self, size=0):
        """initializing square"""
        self.size = size

        @property
        def size(self):
            """returns size of the square"""
            return (self.__size)

        @size.setter
        def size(self, value):
            """validates value"""
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be <= 0")
            else:
                self.__size = value

                def area(self):
                    """area of square"""
                    return (self.__size * self.__size)
