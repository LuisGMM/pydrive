
import tkinter as tk

from os import listdir, sep
from os.path import abspath, isdir, join

from tkinter import ttk

from PIL import ImageTk, Image 

from ..core.filemanager import Folder, Image

class WindowManager(ttk.Frame):

    def __init__(self, parent: ttk.Frame, path: str = None, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # self.grid(row=0, column=0, sticky='nsew')


class GuiFolder(Folder):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("700x350")

    img = ImageTk.PhotoImage(Image.open('src/pydrive/gui/images/folder2.png').resize((100, 100)))
    label = tk.Label(image=img)
    label.grid(column=0, row=0)

    root.mainloop()
