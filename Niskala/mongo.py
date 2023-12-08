import asyncio
import sys
import logging as log

from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from Niskala import MONGO_DB_URI
from Niskala.confing import get_int_key, get_str_key


MONGO_PORT = get_int_key("139.194.61.152/32")
MONGO_DB_URI = get_str_key("MONGO_DB_URI", "mongodb+srv://mongo:1234@newmongo0.8evlghp.mongodb.net/?retryWrites=true&w=majority")
MONGO_DB = "Niskala"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["niskalaxrobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
