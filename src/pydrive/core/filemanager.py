
from __future__ import annotations

from datetime import datetime
from typing import List, Tuple

from os import listdir, sep
from os.path import abspath, isdir, join

import tkinter as tk


from user import User

class Item():
    
    def __init__(self, path: str):    
        
        self.path = path.replace('\\', '/')
        self.name = self.path.split('/')[-1]
    
    def get_image(self, path: str) -> tk.PhotoImage:
        '''Get the corresponding image depending if `path` corresponds to a file or a folder.

        Args:
            path (str): Directory of the item we want an icon for.

        Returns:
            tk.PhotoImage: Icon image corresponding to `path`.
        '''
        if isdir(path):
            return tk.PhotoImage(file='src/pydrive/gui/images/folder.png')
        else:
            return tk.PhotoImage(file='src/pydrive/gui/images/file.png')


class Directory(Item):

    def __init__(self, path: str) -> None:

        super().__init__(path)
        self.parent = self.path.split('/')[-2]
    
    @property
    def children(self, path: str) -> list:
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


class File(Item):

    def __init__(self, path: str, from_path: str = None, name: str = None, modified: List[Tuple[datetime, User]] = None) -> None:
        super().__init__(path)
        self.from_path = from_path
        self.name = name
        self.modified = modified

        self.file = self.get_file()

    def get_file(self) -> bytes:

        try:
            with open(self.from_path, 'rb') as f:
                return f.read()

        except IOError as e:
            print(e)
