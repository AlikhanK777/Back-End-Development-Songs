import os
import json
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

service = os.environ.get("MONGODB_SERVICE")
if service:
    client = MongoClient(f"mongodb://{service}:27017")
else:
    import mongomock
    client = mongomock.MongoClient()
db = client.songs

songs_path = os.path.join(os.path.dirname(__file__), "data", "songs.json")
with open(songs_path) as f:
    songs_list = json.load(f)
if db.songs.count_documents({}) == 0:
    db.songs.insert_many(songs_list)

from backend import routes  # noqa
