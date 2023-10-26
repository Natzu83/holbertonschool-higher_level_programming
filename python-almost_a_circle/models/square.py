#!/usr/bin/python3
"""Contains a square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the string representation of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
