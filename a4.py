import tkinter as tk
from tkinter import simpledialog, messagebox
from ds_messenger import DirectMessenger

class MessengerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ICS 32 Messenger")

        self.server = "127.0.0.1"
        self.username = simpledialog.askstring("Username", "Enter username:")
        self.password = simpledialog.askstring("Password", "Enter password:")

        self.messenger = DirectMessenger(
            self.server,
            self.username,
            self.password
        )

        self.contacts = []
        self.current_contact = None

        self.setup_gui()
        self.root.after(5000, self.check_new_messages)