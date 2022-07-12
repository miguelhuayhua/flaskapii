# ---MongoDB database connection
# MongoDB libraries
from pymongo import MongoClient
import os


def getDatabase():
    SECRET = os.getenv("MONGO_URI")
    client = MongoClient(SECRET)
    return client.get_database('movie-project')
