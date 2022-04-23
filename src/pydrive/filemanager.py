
from __future__ import annotations

from typing import List, Union


class Path():

    def __init__(self, parent: Path, children: List[Path], contains: Union[File, Folder]) -> None:

        self.parent = parent
        self.children = children
        self.contains = contains


class File():
    pass


class Folder():
    pass
