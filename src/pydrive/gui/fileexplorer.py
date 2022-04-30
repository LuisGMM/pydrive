
import tkinter as tk

from pydrive.gui.gui_filemanager import WindowManager
from pydrive.gui.treedirectory import TreeDirectory


class FileExplorer(tk.Frame):

    def __init__(self, parent, path: str, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.path = path

        # self.parent.title = 'File Explorer'
        self.pack()

        self.treedirectory = TreeDirectory(self, self.path)
        # self.treedirectory.pack(fill=tk.Y, side=tk.LEFT, expand=tk.YES)
        self.treedirectory.grid(row=0, column=0, sticky="NSW")

