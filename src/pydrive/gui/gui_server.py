
import tkinter as tk

from tkinter import filedialog

import socket


class CreateServerFrame(tk.Frame):

    def __init__(self, parent: tk.Tk) -> None:

        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.parent.title("Create server")
        self.parent.resizable(False, False)

        server_name_label = tk.Label(self.parent, text="Server Name:", width=20)
        server_name_label.grid(column=0, row=0)

        self.server_name_entry = tk.Entry()
        self.server_name_entry.grid(column=1, row=0)

        