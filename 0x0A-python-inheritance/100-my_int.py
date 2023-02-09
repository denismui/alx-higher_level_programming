#!/usr/bin/python3
"""MyInt class Module"""


class MyInt(int):
    """A MyInt class"""
    def __eq__(self, other):
        """Overrides and inverts == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides and inverts != operator"""
        return int(self) == int(other)
