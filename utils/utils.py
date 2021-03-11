import json


def read_records_from_json(filename):
    """
    Takes a json filename and returns its list representation
    """
    with open(filename, 'r') as f:
        return json.load(f)
