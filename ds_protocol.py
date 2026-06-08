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

def direct_message(
        token,
        message,
        recipient,
        timestamp):

    return json.dumps({
        "token": token,
        "directmessage": {
            "entry": message,
            "recipient": recipient,
            "timestamp": timestamp
        }
    })

