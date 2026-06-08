import json
from collections import namedtuple

Response = namedtuple(
    "Response",
    ["type", "message", "token"]
)

def join(username, password):
    return json.dumps({
        "join": {
            "username": username,
            "password": password,
            "token": ""
        }
    })