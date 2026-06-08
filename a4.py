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

    def setup_gui(self):
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.contact_list = tk.Listbox(self.left_frame, width=25)
        self.contact_list.pack(fill=tk.Y, expand=True)
        self.contact_list.bind("<<ListboxSelect>>", self.select_contact)

        self.add_button = tk.Button(
            self.left_frame,
            text="Add User",
            command=self.add_user
        )
        self.add_button.pack(fill=tk.X)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.message_display = tk.Text(
            self.right_frame,
            height=20,
            width=60
        )
        self.message_display.pack(fill=tk.BOTH, expand=True)

        self.entry_box = tk.Text(
            self.right_frame,
            height=4,
            width=60
        )
        self.entry_box.pack(fill=tk.X)

        self.send_button = tk.Button(
            self.right_frame,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(fill=tk.X)

    def add_user(self):
        user = simpledialog.askstring("Add User", "Enter username:")

        if user and user not in self.contacts:
            self.contacts.append(user)
            self.contact_list.insert(tk.END, user)

    