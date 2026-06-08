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

    def select_contact(self, event):
        selection = self.contact_list.curselection()

        if selection:
            index = selection[0]
            self.current_contact = self.contacts[index]

            self.message_display.delete("1.0", tk.END)
            self.load_messages_for_contact()

    def send_message(self):
        if not self.current_contact:
            messagebox.showerror("Error", "Select a user first.")
            return

        text = self.entry_box.get("1.0", tk.END).strip()

        if not text:
            return

        success = self.messenger.send(text, self.current_contact)

        if success:
            self.message_display.insert(tk.END, f"Me: {text}\n")
            self.entry_box.delete("1.0", tk.END)
        else:
            messagebox.showerror("Error", "Message failed to send.")

    def load_messages_for_contact(self):
        all_messages = self.messenger.retrieve_all()

        for msg in all_messages:
            if msg.sender == self.current_contact:
                self.message_display.insert(
                    tk.END,
                    f"{msg.sender}: {msg.message}\n"
                )
            elif msg.recipient == self.current_contact:
                self.message_display.insert(
                    tk.END,
                    f"Me: {msg.message}\n"
                )