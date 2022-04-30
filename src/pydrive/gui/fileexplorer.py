
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

