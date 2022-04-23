
import tkinter as tk


class WindowManager(tk.Frame):

    def __init__(self, parent: tk.Tk, path: str, *args, **kwargs) -> None:

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == '__main__':
    pass
