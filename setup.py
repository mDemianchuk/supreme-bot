import os
from dotenv import load_dotenv

load_dotenv()
ITEM_NAME = os.getenv("ITEM_NAME")
ITEM_SIZE = os.getenv("ITEM_SIZE")
ITEM_COLORWAY_POSITION = os.getenv("ITEM_COLORWAY_POSITION")
NAME = os.getenv("NAME")
EMAIL = os.getenv("EMAIL")
PHONE = os.getenv("PHONE")
ADDRESS = os.getenv("ADDRESS")
UNIT = os.getenv("UNIT")
ZIP = os.getenv("ZIP")
STATE = os.getenv("STATE")
CC_NUMBER = os.getenv("CC_NUMBER")
EXP_M = os.getenv("EXP_M")
EXP_Y = os.getenv("EXP_Y")
CVV = os.getenv("CVV")
