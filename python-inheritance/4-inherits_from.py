#!/usr/bin/python3
"""
A function that returns True if
    the object is an instance of a class that
    inherited (directly or indirectly) from the
    specified class otherwise it is False.
"""


def inherits_from(obj, a_class):
    """Returns true if obj is instance of parent classes"""
    return isinstance(obj, a_class) and type(obj) is not a_class
