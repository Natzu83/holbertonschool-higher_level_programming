#!/usr/bin/python3
"""
MyList that inherits from list:

Public instance method: def print_sorted(self):
    that prints the list, but sorted
"""


class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list without changing original"""
        print(sorted(self))
