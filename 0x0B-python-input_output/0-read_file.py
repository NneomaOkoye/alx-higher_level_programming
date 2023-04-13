#!/usr/bin/python3
"""Defines a Read File Function."""

def read_file(filename=""):
    """Prints a text file UTF8 content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
