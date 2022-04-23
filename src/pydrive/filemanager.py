
from __future__ import annotations

import time
from typing import List, Tuple, Union


class Path():

    def __init__(self, parent: Path , children: List[Path], contains: Union[File, Folder]) -> None:

        self.parent = parent
        self.children = children
        self.contains = contains


class File():
    
    def __init__(self, from_path: str, name: str, modified: List[Tuple[Time, User]]) -> None:
        ...


class Folder():
    pass
