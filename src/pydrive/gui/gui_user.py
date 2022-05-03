
import socket
import tkinter as tk

from threading import Thread

from pydrive.core.user import User


class GuiUser(tk.Frame):

    def __init__(self, parent: tk.Tk, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.parent.title("Create User")
        self.parent.resizable(False, False)

        self.user_name_label: tk.Label = tk.Label(self.parent, text="Username: ", width=20, anchor='e', padx=10)
        self.user_name_label.grid(column=0, row=0, sticky='nsew')

        self.user_name_entry: tk.Entry = tk.Entry(self.parent)
        self.user_name_entry.grid(column=1, row=0)

        self.port_label: tk.Label = tk.Label(self.parent, text="Port: ", width=20, anchor='e', padx=10)
        self.port_label.grid(column=0, row=1, sticky='nsew')

        self.port_entry: tk.Entry = tk.Entry(self.parent)
        self.port_entry.grid(column=1, row=1)

        self.default_port_button: tk.Button = tk.Button(self.parent, text="Default", command=self._cmd_search_default_port)
        self.default_port_button.grid(column=2, row=1)

        self.ip_label: tk.Label = tk.Label(self.parent, text="Ip:", width=20, anchor='e', padx=10)
        self.ip_label.grid(column=0, row=2, sticky='nsew')

        self.ip_entry: tk.Entry = tk.Entry(self.parent)
        self.ip_entry.grid(column=1, row=2)

        self.default_ip_button: tk.Button = tk.Button(self.parent, text="Default", command=self._cmd_search_default_ip)
        self.default_ip_button.grid(column=2, row=2)

        self.create_button = tk.Button(self.parent, text="Connect to server", command=self._cmd_connect_to_server)
        self.create_button.grid(column=1, row=5)

    def _cmd_search_default_port(self):
        self.port_entry.delete(0, tk.END)
        self.port_entry.insert(tk.END, 5050)

    def _cmd_search_default_ip(self):

        self.__ip = socket.gethostbyname(socket.gethostname())

        self.ip_entry.delete(0, tk.END)
        self.ip_entry.insert(tk.END, self.__ip)

    def _cmd_connect_to_server(self):

        self.__title = self.user_name_entry.get()
        self.__addr = (self.ip_entry.get(), int(self.port_entry.get()))

        self.parent.title(self.__title)
        self.__user = User(username=self.user_name_entry.get(), addr=self.__addr)

        self.user_thread = Thread(target=self.__user.start)
        self.user_thread.start()


def main():
    ROOT = tk.Tk()
    ROOT.geometry("600x300")
    APP = GuiUser(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()


if __name__ == "__main__":
    main()
