#!/usr/bin/python3
"""
Function that returns True if the object
    is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """Determines if object is instance of class"""
    return type(obj) is a_class
