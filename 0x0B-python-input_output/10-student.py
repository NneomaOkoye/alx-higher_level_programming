#!/usr/bin/python3
"""Defines a class named student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new student.

        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

def to_json(self, attrs=None):
    """Retrieves a dictionary representation of the Student."""
    if (type(attrs)) == list and all(type(i) == str for i in attrs):
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
    else:
        return self.__dict__
