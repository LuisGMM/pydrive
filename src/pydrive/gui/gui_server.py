
import tkinter as tk

from tkinter import filedialog

import socket

from core.server import Server


class CreateServerFrame(tk.Frame):

    def __init__(self, parent: tk.Tk) -> None:

        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.parent.title("Create server")
        self.parent.resizable(False, False)

        server_name_label: tk.Label = tk.Label(self.parent, text="Server Name:", width=20)
        server_name_label.grid(column=0, row=0)

        self.server_name_entry: tk.Entry = tk.Entry(self.parent)
        self.server_name_entry.grid(column=1, row=0)

        self.port_label: tk.Label = tk.Label(self.parent, text="Port:", width=20)
        self.port_label.grid(column=0, row=1)

        self.port_entry: tk.Entry = tk.Entry(self.parent)
        self.port_entry.grid(column=1, row=1)

        self.default_port_button: tk.Button = tk.Button(self.parent, text="Default", command=self._cmd_search_default_port)
        self.default_port_button.grid(column=2, row=1)

        self.ip_label: tk.Label = tk.Label(self.parent, text="Ip:", width=20)
        self.ip_label.grid(column=0, row=2)

        self.ip_entry: tk.Entry = tk.Entry(self.parent)
        self.ip_entry.grid(column=1, row=2)

        self.default_ip_button: tk.Button = tk.Button(self.parent, text="Default", command=self._cmd_search_default_ip)
        self.default_ip_button.grid(column=2, row=2)

        self.root_label: tk.Label = tk.Label(self.parent, text="Root directory:", width=20)
        self.root_label.grid(column=0, row=3)

        self.root_entry: tk.Entry = tk.Entry(self.parent)
        self.root_entry.grid(column=1, row=3)

        self.search_root_button: tk.Button = tk.Button(self.parent, text="Search", command=self._cmd_search_root)
        self.search_root_button.grid(column=2, row=3)

        self.create_button = tk.Button(self.parent, text="Create server", command= self._cmd_create_server)
        self.create_button.grid(column=1, row=5)

    def _cmd_search_default_port(self):
        self.port_entry.delete(0, tk.END)
        self.port_entry.insert(tk.END, 5050)

    def _cmd_search_default_ip(self):

        self.__ip = socket.gethostbyname(socket.gethostname())

        self.ip_entry.delete(0, tk.END)
        self.ip_entry.insert(tk.END, self.__ip)

    def _cmd_search_root(self):
        self.file = filedialog.askdirectory(initialdir="/")

        self.root_entry.delete(0, tk.END)
        self.root_entry.insert(tk.END, self.file)

    def _cmd_create_server(self):

        self.__title = self.server_name_entry.get()
        self.__root = self.root_entry.get()
        self.__addr = (self.ip_entry.get(), int(self.port_entry.get()))

        self.parent.title(self.__title)
        self.__server = Server(addr=self.__addr)
        self.__server.start()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("600x300")
    APP = CreateServerFrame(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
