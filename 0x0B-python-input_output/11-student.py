#!/usr/bin/python3
""" Createing a class named student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializing a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
    """Retrieving a dictionary representation of the student.

    If attr is a list of strings, represents only those attributes
    included in the list.

    Args:
        attrs (list): (Optional) The attributes to represent.
    """
    if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
    return self.__dict__

def reload_from_json(self, json):
    """update all the attributtes of student"""

    Args:
        json (dict): The key/value pairs to replace attributes with.
    """
    for k, v in json.items():
    setattr(self, k, v)
