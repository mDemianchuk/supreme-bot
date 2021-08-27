import json
from json.decoder import JSONDecodeError
from utils.logging_util import log_error


def read_json_file(filename: str):
    try:
        with open(filename) as file:
            return json.load(file)
    except OSError:
        log_error(f"Unable to read file {filename}.")
    except JSONDecodeError:
        log_error(f"Unable to decode JSON from {filename}.")
    finally:
        exit()
