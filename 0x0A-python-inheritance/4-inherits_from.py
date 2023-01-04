#!/usr/bin/python3
"""Function that checks class inheritance"""


def inherits_from(obj, a_class):
    """Checks if an ojects is an inherited instance of a class."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
