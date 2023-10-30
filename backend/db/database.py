import os
from pymongo import MongoClient
from bson import ObjectId

DB_URI = os.environ.get('DB_URI')

client = MongoClient(DB_URI)