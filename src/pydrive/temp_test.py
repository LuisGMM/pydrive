
from tkinter import ttk
import tkinter as tk

# from pydrive.core.filemanager import Folder, File

from core.filemanager import Folder, File


class GuiItem(ttk.Frame):

    def __init__(self, parent: ttk.Frame, row: int, column: int, *args, **kwargs) -> None:
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.gui_image = tk.Label(self)
        self.gui_image.grid(column=0, row=0)

        self.gui_name = tk.Label(self)
        self.gui_name.grid(column=0, row=1)


class GuiFolder(GuiItem, Folder):

    def __init__(self, parent: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(self, parent, row, column, *args, **kwargs)
        Folder.__init__(self, path)

        self.gui_image.configure(image=self.image)
        self.gui_name.configure(text=self.name)


root = tk.Tk()

item = GuiItem(root, 0, 0)
folder = GuiFolder(item, 0, 0, '/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui')

root.mainloop()
