import os

from dotenv import load_dotenv


load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
LINK_PATTERN: str = os.getenv("LINK_PATTERN") # type: ignore

if LINK_PATTERN is None:
    raise ValueError("LINK_PATTERN cannot be None")
