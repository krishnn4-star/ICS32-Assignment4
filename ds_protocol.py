import json
from collections import namedtuple

Response = namedtuple(
    "Response",
    ["type", "message", "token"]
)
