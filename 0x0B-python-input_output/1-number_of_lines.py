#!/usr/bin/python3
def number_of_lines(filename=""):
    """ Function that returns the number of lines of a text file """
    with open(filename, encoding='utf-8') as f:
        return(len(f.readlines()))
