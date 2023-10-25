#!/usr/bin/python3
"""Module that contains a class to serve as base for other classes"""


import csv
import json
import os
import turtle


class Base:
    """Represents base of all the classes created """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
