
import tkinter as tk

# from os import listdir, sep
# from os.path import abspath, isdir, join

from tkinter import ttk

from PIL import ImageTk, Image

from ..core.filemanager import Folder, File


class GuiItem(ttk.Frame):

    def __init__(self, parent: ttk.Frame, row: int, column: int, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.grid(column=column, row=row)

        self.gui_image = tk.Label(self)
        self.gui_image.grid(column=0, row=0)

        self.gui_name = tk.Label(self)
        self.gui_name.grid(column=0, row=1)


class GuiFolder(GuiItem, Folder):

    def __init__(self, parent: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(parent, row, column, *args, **kwargs)
        Folder.__init__(path)

        self.gui_image.configure(image=self.image)
        self.gui_name.configure(text=self.name)


class GuiFile(File):

    def __init__(self, parent: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(parent, row, column, *args, **kwargs)
        File.__init__(path)

        self.gui_image.configure(image=self.image)
        self.gui_name.configure(text=self.name)


class WindowManager(ttk.Frame):

    def __init__(self, parent: ttk.Frame, path: str = None, *args, **kwargs) -> None:

        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.elem = GuiFolder(self, 0, 0, '/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui')
        self.elem2 = GuiFile(self, 0, 0, '/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui/__init__.py')

        # self.grid(row=0, column=0, sticky='nsew')


def main():
    
    root = tk.Tk()
    root.geometry("700x350")

    frame = WindowManager(root)

    root.mainloop()



if __name__ == '__main__':

    main()