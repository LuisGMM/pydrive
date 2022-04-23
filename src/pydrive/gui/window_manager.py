
import tkinter as tk

from os import listdir, sep
from os.path import abspath, isdir, join

from tkinter import ttk

class WindowManager(ttk.Frame):

    def __init__(self, parent: ttk.Frame, path: str = None, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    
    main_window = tk.Tk()
    app = WindowManager(main_window)
    app.mainloop()
