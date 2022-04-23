
import tkinter as tk
from tkinter import ttk

from os import listdir, sep
from os.path import isdir, join, abspath


class TreeDirectory(ttk.Frame):

    def __init__(self, main_window: ttk.Frame) -> None:
        super().__init__(main_window)

