
from __future__ import annotations

from datetime import datetime
from typing import List, Tuple

from os import listdir, sep
from os.path import abspath, isdir, join


from user import User

class Item():
    
    def __init__(self, path: str):    
        
        self.path = path.replace('\\', '/')
        self.name = self.path.split('/')[-1]
        self.isdir = True if isdir(self.path) else False


class Directory(Item):

    def __init__(self, path: str, parent: Directory = None, children: List[Directory] = None, contains: List[File] = None) -> None:
        super().__init__(path)
        self.parent = parent
        self.children = children
        self.contains = contains


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
