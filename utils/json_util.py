import json
from json.decoder import JSONDecodeError


def read_json_file(filename: str):
    try:
        with open(filename) as file:
            return json.load(file)
    except OSError:
        exit(f"ERROR: Unable to read file {filename}.")
    except JSONDecodeError:
        exit(f"ERROR: Unable to decode JSON from {filename}.")
