#!/usr/bin/python3

import json


def to_json_string(my_obj):
    
    # print("type json.dumps(my_obj)--> {}".format(type(json.dumps(my_obj))))
    # print("type my_obj--> {}".format(type(my_obj)))

    # serializing json
    return json.dumps(my_obj)
