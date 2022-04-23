
import tkinter as tk
from tkinter import ttk

from os import listdir, sep
from os.path import isdir, join, abspath


class TreeDirectory(ttk.Frame):

    def __init__(self, main_window: ttk.Frame) -> None:
        super().__init__(main_window)

        self.treeview: ttk.Treeview = ttk.Treeview(self)
        self.treeview.grid(row=0, column=0, sticky="nsew")

        self.treeview.tag_bind("fstag", "<<TreeviewOpen>>", self.event_item_opened)

        for w in (self, main_window):
            w.rowconfigure(0, weight=1)
            w.columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")

        self.directories: dict[str, str] = {}

        self.file_image: tk.PhotoImage = tk.PhotoImage(file="/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui/file.png")
        self.folder_image: tk.PhotoImage = tk.PhotoImage(file="/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui/folder.png")

        self.load_tree(abspath(sep))

    def listdir(self, path: str) -> list:

        try:
            return listdir(path)
        
        except PermissionError as e:
            print(str(e))
            
            return []

    