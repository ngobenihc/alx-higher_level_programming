#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    
    with open(filename, 'w', encoding="utf-8") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()
