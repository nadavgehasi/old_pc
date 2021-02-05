from pymongo import MongoClient
from hashlib import sha256


def read_state(processor_state):
    with MongoClient('localhost', 27017) as client:
        db = client.nipy_db
        state_collection = db.state_collection
        state = state_collection.find_one({"id": processor_state})
        if state is None:
            state = {"id": processor_state}
    return state


def write_state(processor_state, state):
    with MongoClient('localhost', 27017) as client:
        db = client.nipy_db
        state_collection = db.state_collection
        state_collection.update(state)
