import json
from utils.logging_util import log_error


def read_json_file(filename: str):
    try:
        with open(filename) as file:
            return json.load(file)
    except:
        log_error("Error while loading the settings file.")
