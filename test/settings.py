import os
from dotenv import load_dotenv

load_dotenv(".env")

APP_PATH = os.getenv('APP_PATH')
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')
TITLE = os.getenv('TITLE')
