#!/usr/bin/python3


def number_of_lines(filename=""):
    
    with open(filename, encoding='utf-8') as myFile:
        return sum([1 for line in myFile])
