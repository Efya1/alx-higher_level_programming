#!/usr/bin/python3
""" Fetch information about object attributes and methods
"""


def lookup(obj):
    """ Fetch a list of an object's attributes and methods
    """
    return dir(obj)
