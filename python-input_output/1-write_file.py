#!/usr/bin/python3
"""Module write to a file"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file (UTF8)
    and returns the number of characters written: """
    with open(filename, "w", encoding="utf-8") as file:
        n_chars = file.write(text)
    return n_chars
