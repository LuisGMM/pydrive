
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

        self.port_label = tk.Label(self.parent, text="Port", width=20)
        self.port_label.grid(column=0, row=1)

        self.port_entry = tk.Entry()
        self.port_entry.grid(column=1, row=1)

        self.default_port_button = tk.Button(self.parent, text="Default", command=self._search_default_port)
        self.default_port_button.grid(column=2, row=1)

        self.ip_label = tk.Label(self.parent, text="Ip", width=20)
        self.ip_label.grid(column=0, row=2)

        self.ip_entry = tk.Entry()
        self.ip_entry.grid(column=1, row=2)

        

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("600x300")
    APP = CreateServerFrame(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
