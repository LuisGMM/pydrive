
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
        '''Returns a list with the directories in that `path`.
        Is there is no permission to acces `path` it returns an empty list.

        Args:
            path (str): Path directory to explore its contents. 

        Returns:
            list: Contains the names of the directories (folders and files) in that path.
        '''
        try:
            return listdir(path)
        
        except PermissionError as e:
            print(str(e))
            
            return []

    def get_icon(self, path: str)-> tk.PhotoImage:
        '''Get the corresponding image depending if `path` corresponds to a file or a folder.

        Args:
            path (str): Directory of the item we want an icon for.

        Returns:
            tk.PhotoImage: Icon image corresponding to `path`.
        '''
        return self.folder_image if isdir(path) else self.file_image

    def insert_item(self, name: str, path: str, parent_uid: str = "") -> str:

        uid = self.treeview.insert(parent_uid, tk.END, text=name, tags=("fstag",), image=self.get_icon(path))
        self.directories[uid] = path
        
        return uid
