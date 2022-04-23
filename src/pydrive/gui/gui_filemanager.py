
import tkinter as tk

from os import listdir, sep
from os.path import abspath, isdir, join

from tkinter import ttk

from PIL import ImageTk, Image
from pyparsing import col 

from ..core.filemanager import Folder, File

class WindowManager(ttk.Frame):

    def __init__(self, parent: ttk.Frame, path: str = None, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # self.grid(row=0, column=0, sticky='nsew')


class GuiItem(ttk.Frame):
    
    def __init__(self, parent: ttk.Frame, row: int, column: int, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.grid(column=column, row=row)


class GuiFolder(GuiItem, Folder):

    def __init__(self, parent: ttk.Frame, row: int, column: int, *args, **kwargs):
        GuiItem.__init__(parent, row, column, *args, **kwargs)

        self.gui_image = tk.Label(self, image=self.image)
        self.gui_image.grid(column=0, row=0)
        
        self.gui_name = tk.Label(self, text=self.name)
        self.gui_name.grid(column=0, row=1)
        


class GuiFile(File):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)




if __name__ == '__main__':

    root = tk.Tk()
    root.geometry("700x350")

    img = ImageTk.PhotoImage(Image.open('src/pydrive/gui/images/folder2.png').resize((100, 100)))
    label = tk.Label(image=img)
    label.grid(column=0, row=0)

    root.mainloop()
