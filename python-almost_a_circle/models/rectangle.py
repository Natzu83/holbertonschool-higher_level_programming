#!/usr/bin/python3
"""Contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y
