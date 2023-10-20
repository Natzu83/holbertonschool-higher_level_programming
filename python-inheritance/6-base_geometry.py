#!/usr/bin/python3
"""
Public instance method: def area(self): that raises an
    Exception with the message area() is not implemented
"""


class BaseGeometry:
    """Only raises exception"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")
