import os
from motor.motor_asyncio import AsyncIOMotorClient
from bson.binary import UUID_SUBTYPE
from bson.codec_options import CodecOptions

DB_URI = os.environ.get('DB_URI')

client = AsyncIOMotorClient(DB_URI)
db = client.get_database(
    os.environ.get('MONGO_INITDB_DATABASE'),
    CodecOptions(uuid_representation=UUID_SUBTYPE)
)