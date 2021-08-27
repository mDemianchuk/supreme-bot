import logging

# Configure logging
logging.basicConfig(
    format="%(levelname)s: %(asctime)s - %(message)s",
    datefmt="%I:%M:%S", level=logging.INFO
)


def log_message(message: str):
    logging.info(message)


def log_warning(message: str):
    logging.warning(message)


def log_error(message: str):
    logging.error(message)
