from ds_messenger import DirectMessage, DirectMessenger


def test_direct_message_defaults():
    dm = DirectMessage()

    assert dm.recipient is None
    assert dm.sender is None
    assert dm.message is None
    assert dm.timestamp is None


def test_direct_messenger_init():
    messenger = DirectMessenger("127.0.0.1", "nikhil", "password")

    assert messenger.dsuserver == "127.0.0.1"
    assert messenger.username == "nikhil"
    assert messenger.password == "password"
    assert messenger.token is None