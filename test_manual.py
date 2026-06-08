from ds_messenger import DirectMessenger

m1 = DirectMessenger("127.0.0.1", "nikhil", "password")
m2 = DirectMessenger("127.0.0.1", "friend", "password")

print(m1.send("hello friend", "friend"))

messages = m2.retrieve_all()

for msg in messages:
    print(msg.sender, msg.recipient, msg.message, msg.timestamp)