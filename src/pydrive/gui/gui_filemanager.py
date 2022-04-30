
import tkinter as tk

from os import listdir
from os.path import isdir

from tkinter import ttk

# from PIL import ImageTk, Image

from pydrive.core.filemanager import Folder, File


class GuiItem(ttk.Frame):

        ttk.Frame.__init__(self, parent, *args, **kwargs)
    def __init__(self, master: ttk.Frame, row: int, column: int, *args, **kwargs) -> None:
        self.grid(column=column, row=row)

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


class GuiFile(GuiItem, File):

    def __init__(self, parent: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(self, parent, row, column, *args, **kwargs)
        File.__init__(self, path)

        self.gui_image.configure(image=self.image)
        self.gui_name.configure(text=self.name)


class WindowManager(ttk.Frame):

    def __init__(self, parent: ttk.Frame, path: str = None, *args, **kwargs) -> None:
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.path = path
        self.items = {}

        for column, name in enumerate(listdir(self.path)):

            abspath = self.path + f'/{name}'
            self.items[name] = GuiFolder(self, row=0, column=column, path=abspath) if isdir(abspath) else GuiFile(self, row=0, column=column, path=abspath)

        # self.grid(row=0, column=0, sticky='nsew')


def main():
    root = tk.Tk()
    # root.geometry("700x350")

    frame = WindowManager(root, r'C:/Users/luisg/Documents/GitHub/pydrive/src/pydrive/gui')
    frame.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
