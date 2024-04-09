import os
import sys
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", None)
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", None)
MONGO_COLLECTION_NAME = os.getenv("MONGO_COLLECTION_NAME", None)

if not any([MONGO_URI, MONGO_DB_NAME, MONGO_COLLECTION_NAME]):
    sys.exit("Environment variables not defined")

client = MongoClient(MONGO_URI)

db = client[MONGO_DB_NAME]
collection_name = db[MONGO_COLLECTION_NAME]
