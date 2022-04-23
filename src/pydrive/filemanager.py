
from __future__ import annotations

from datetime import datetime
from typing import List, Tuple, Union

from user import User

class Path():

    def __init__(self, parent: Path , children: List[Path], contains: Union[File, Folder]) -> None:

        self.parent = parent
        self.children = children
        self.contains = contains


class File():
    
    def __init__(self, from_path: str, name: str, modified: List[Tuple[datetime, User]]) -> None:
        
        self.from_path = from_path
        self.name = name
        self.modified = modified

        self.file = self.get_file()

    def get_file(self) -> bytes:
        return open(self.from_path, 'rb').read()
        
        


class Folder():
    pass
