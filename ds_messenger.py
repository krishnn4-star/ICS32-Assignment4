import socket
import time
import ds_protocol

PORT = 3001

class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.sender = None
        self.message = None
        self.timestamp = None

class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.token = None