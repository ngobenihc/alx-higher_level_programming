#!/usr/bin/python3

import json


def from_json_string(my_str):
    
    # print("type json.loads(my_str)--> {}".format(type(json.loads(my_str))))
    # print("type my_str--> {}".format(type(my_str)))
    return json.loads(my_str)
