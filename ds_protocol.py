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

def retrieve_new(token):

    return json.dumps({
        "token": token,
        "directmessage": "new"
    })
def retrieve_all(token):

    return json.dumps({
        "token": token,
        "directmessage": "all"
    })

def extract_json(json_msg):

    data = json.loads(json_msg)

    response = data["response"]

    if "messages" in response:
        return response["messages"]

    return Response(
        response.get("type"),
        response.get("message"),
        response.get("token", "")
    )