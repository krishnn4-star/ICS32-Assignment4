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

    def _connect_and_join(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.dsuserver, PORT))

        join_msg = ds_protocol.join(self.username, self.password)
        client.sendall(join_msg.encode())

        response = client.recv(4096).decode()
        parsed = ds_protocol.extract_json(response)

        if parsed.type == "ok":
            self.token = parsed.token
            return client

        client.close()
        return None

    def send(self, message: str, recipient: str) -> bool:
        try:
            client = self._connect_and_join()

            if client is None:
                return False

            timestamp = str(time.time())

            dm_msg = ds_protocol.direct_message(
                self.token,
                message,
                recipient,
                timestamp
            )

            client.sendall(dm_msg.encode())

            response = client.recv(4096).decode()
            parsed = ds_protocol.extract_json(response)

            client.close()

            return parsed.type == "ok"

        except Exception:
            return False

