
from __future__ import annotations
from abc import ABC

from datetime import datetime
from typing import List, Tuple

from os import listdir
from os.path import isdir

import tkinter as tk
from PIL import ImageTk, Image

from pydrive.core.user import User


class Item(ABC):
    '''Parent class to represent a Folder or a File.

    Attributes:
        path (str): The location of the item.
        name (str): The name of the item. It includes its extension.
    '''
    def __init__(self, path: str) -> None:
        '''Instantiate object.

        Args:
            path (str): The location of the item.
        '''
        self.path = path.replace('\\', '/')
        self.name = self.path.split('/')[-1]

    def get_image(self) -> tk.PhotoImage:
        '''Get the corresponding image depending if `path` corresponds to a file or a folder.

        Args:
            path (str): Directory of the item we want an icon for.

        Returns:
            tk.PhotoImage: Icon image corresponding to `path`.
        '''
        if isdir(self.path):
            return ImageTk.PhotoImage(Image.open('src/pydrive/gui/images/folder2.png').resize((100, 100)))
        else:
            return ImageTk.PhotoImage(Image.open('src/pydrive/gui/images/file2.png').resize((100, 100)))


class Folder(Item):

    def __init__(self, path: str) -> None:

        super().__init__(path)
        self.parent = self.path.split('/')[-2]
        self.image = self.get_image()

    @property
    def dirs(self) -> list:
        '''Returns a list with the items in the directory.
        If there is no permission to access the directory, it returns an empty list.

        Args:
            path (str): Path directory to explore its contents.

        Returns:
            list: Contains the names of the directories (folders and files) in that path.
        '''
        try:
            return listdir(self.path)

        except PermissionError as e:
            print(str(e))

            return []


class File(Item):

    def __init__(self, path: str, modified: List[Tuple[datetime, User]] = None) -> None:
        super().__init__(path)
        self.modified = modified
        self.image = self.get_image()

    @property
    def file(self) -> bytes:

        try:
            with open(self.from_path, 'rb') as f:
                return f.read()

        except IOError as e:
            print(e)
