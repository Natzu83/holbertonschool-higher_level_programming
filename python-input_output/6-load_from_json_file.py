#!/usr/bin/python3
"""Create the object from a JSON file"""


import json


def load_from_json_file(filename):
    """Function creates an object from a “JSON file”"""
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
