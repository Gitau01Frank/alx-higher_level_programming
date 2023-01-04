#!/usr/bin/python3
"""Defines a class and inherited checking function"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
