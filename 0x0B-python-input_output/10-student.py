#!/usr/bin/python3
"""Module defining the class Student based on 9-student.py"""


class Student:
    
    def __init__(self, first_name, last_name, age):
       
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
