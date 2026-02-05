from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongodb://mongodb-gerstnir-dev.apps.rm2.thpm.p1.openshiftapps.com:27017/")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")

myclient = MongoClient(mongo_uri)
db = myclient[mongo_db]
Collection = db[mongo_collection]


def serialize_doc(doc):
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return doc


def serialize_docs(docs):
    return [serialize_doc(doc) for doc in docs]
