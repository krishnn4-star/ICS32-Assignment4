import json
import ds_protocol


def test_join_format():
    msg = ds_protocol.join("nikhil", "password")
    data = json.loads(msg)

    assert "join" in data
    assert data["join"]["username"] == "nikhil"
    assert data["join"]["password"] == "password"


def test_direct_message_format():
    msg = ds_protocol.direct_message("abc", "hello", "friend", "123")
    data = json.loads(msg)

    assert data["token"] == "abc"
    assert data["directmessage"]["entry"] == "hello"
    assert data["directmessage"]["recipient"] == "friend"


def test_retrieve_new_format():
    msg = ds_protocol.retrieve_new("abc")
    data = json.loads(msg)

    assert data["directmessage"] == "new"


def test_retrieve_all_format():
    msg = ds_protocol.retrieve_all("abc")
    data = json.loads(msg)

    assert data["directmessage"] == "all"