#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the
    object is an instance of the class that inherited from the
    specified class; otherwise False """
    return isinstance(obj, a_class)
