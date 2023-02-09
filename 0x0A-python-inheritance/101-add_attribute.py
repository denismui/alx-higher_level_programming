#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_attribute(obj, name, value):
    """Method checking if attributes can be set and sets where possible"""
    if hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
