import json

def read_json(file_path):
    # Read JSON data from a file and return it as a Python object. r use as read mode to open the file and json.load() to parse the JSON data.
    with open(file_path, 'r') as file:
    # Convert the JSON data to a Python object (usually a dict or list) using json.load() and return it.
        data = json.load(file)
    return data

"""
“Open the file located at file_path.”
“Read the text inside it.”
“Interpret that text as JSON.”
“Give me the resulting Python object.”
"""
