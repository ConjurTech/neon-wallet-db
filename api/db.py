from pymongo import MongoClient
import os
import redis
from rq import Queue

MONGO_URL = os.environ.get('MONGO_URL')
MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME')

client = MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB_NAME]

# db["meta"].insert_one({"name":"lastTrustedBlock", "value":1162327})
# db["meta"].insert_one({"name":"lastTrustedTransaction", "value":1162327})

# redis

redis_url = os.environ.get('REDIS_URL')

redis_db = redis.from_url(redis_url)

# redis_db.flushdb()

q = Queue(connection=redis_db)

transaction_db = db['transactions']
blockchain_db = db['blockchain']
meta_db = db['meta']
logs_db = db['logs']
address_db = db['addresses']
