
from __future__ import annotations

from datetime import datetime
from typing import List, Tuple

from user import User


class Directory():

    def __init__(self, parent: Directory , children: List[Directory], contains: List[File]) -> None:

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

        try:
            with open(self.from_path, 'rb') as f:
                return f.read()

        except IOError as e:
            print(e)
