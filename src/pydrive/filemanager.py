
from typing import List, Union

from __future__ import annotations


class Path():
    
    def __init__(self, parent: Path , children: List[Path], contains: Union[File, Folder] ) -> None:
        
        self.parent = parent
        self.children = children
        self.contains = contains


class File():
    raise NotImplementedError()


class Folder():
    raise NotImplementedError()
