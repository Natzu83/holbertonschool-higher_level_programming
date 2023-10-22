#!/usr/bin/python3
"""
Function to return the dictionary description with simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Return the dictionary description with a simple data structure
    for JSON serialization

    """
    return obj.__dict__
