import json
from bson import json_util
from flask import request
from . import app, db


def parse_json(data):
    return json.loads(json_util.dumps(data))


@app.route("/health")
def health():
    return {"status": "OK"}


@app.route("/count")
def count():
    return {"count": db.songs.count_documents({})}


@app.route("/song", methods=["GET"])
def songs():
    return {"songs": parse_json(list(db.songs.find({})))}, 200


@app.route("/song/<int:id>", methods=["GET"])
def get_song_by_id(id):
    song = db.songs.find_one({"id": id})
    if song is None:
        return {"message": "song with id not found"}, 404
    return parse_json(song), 200


@app.route("/song", methods=["POST"])
def create_song():
    new_song = request.json
    if db.songs.find_one({"id": new_song["id"]}):
        return {"Message": f"song with id {new_song['id']} already present"}, 302
    res = db.songs.insert_one(new_song)
    return {"inserted id": parse_json(res.inserted_id)}, 201


@app.route("/song/<int:id>", methods=["PUT"])
def update_song(id):
    new_data = request.json
    if db.songs.find_one({"id": id}) is None:
        return {"message": "song not found"}, 404
    res = db.songs.update_one({"id": id}, {"$set": new_data})
    if res.modified_count == 0:
        return {"message": "song found, but nothing updated"}, 200
    return parse_json(db.songs.find_one({"id": id})), 201


@app.route("/song/<int:id>", methods=["DELETE"])
def delete_song(id):
    res = db.songs.delete_one({"id": id})
    if res.deleted_count == 0:
        return {"message": "song not found"}, 404
    return "", 204
