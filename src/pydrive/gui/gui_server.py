
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

