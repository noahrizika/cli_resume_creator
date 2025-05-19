"""
helpers.py
"""

import json

def parse_json_file(file_path):
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
    return data_dict

def write_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # indent for pretty printing
