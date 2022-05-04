
import tkinter as tk

from os import listdir
from os.path import isdir

from tkinter import ttk

from typing import Union
# from PIL import ImageTk, Image

from pydrive.core.filemanager import Folder, File
# from pydrive.gui.fileexplorer import FileExplorer


class GuiItem(ttk.Frame):
    '''Frame. Graphic version of Item class, it is meant to be parent of folders and files.

    Attributes:
        master (ttk.Frame): Parent of this frame.
        gui_image (tk.Label): Image of the item stored in a label.
        gui_name (tk.Label): Name of the item in a label.
    '''

    def __init__(self, master: ttk.Frame, row: int, column: int, *args, **kwargs) -> None:
        '''Instantiate object.

        Args:
            master (ttk.Frame): Parent of this frame.
            row (int): Row to place this frame.
            column (int): Column to place this frame.
        '''
        ttk.Frame.__init__(self, master, *args, **kwargs)
        self.grid(column=column, row=row)

        self.master = master

        self.gui_image = tk.Label(self)
        self.gui_image.grid(column=0, row=0)

        self.gui_name = tk.Label(self)
        self.gui_name.grid(column=0, row=1)


class GuiFolder(GuiItem, Folder):
    '''Frame. Graphic version of Folder.

    Attributes:
        master (ttk.Frame): Parent of this frame.
        gui_image (tk.Label): Image of the item stored in a label.
        gui_name (tk.Label): Name of the item in a label.
        path (str): The location of the item.
        name (str): The name of the item. It includes its extension.
        parent (str): Parent directory of the folder.
        image (tk.PhotoImage): Image of a folder.
    '''
    def __init__(self, master: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(self, master, row, column, *args, **kwargs)
        Folder.__init__(self, path)

        self.path = path

        self.gui_image.configure(image=self.image)
        self.gui_image.bind("<Button-1>", self.open_folder)

        self.gui_name.configure(text=self.name)
        self.gui_name.bind("<Button-1>", self.open_folder)

    def open_folder(self, event):
        self.master.master.path = self.path


class GuiFile(GuiItem, File):
    '''Frame. Graphic version of File.

    Attributes:
        master (ttk.Frame): Parent of this frame.
        gui_image (tk.Label): Image of the item stored in a label.
        gui_name (tk.Label): Name of the item in a label.
        path (str): The location of the item.
        name (str): The name of the item. It includes its extension.
        modified (List[Tuple[datetime, User]]): Contains who and when modified this file.
        image (tk.PhotoImage): Image of a folder.
    '''
    def __init__(self, master: ttk.Frame, row: int, column: int, path: str, *args, **kwargs):
        GuiItem.__init__(self, master, row, column, *args, **kwargs)
        File.__init__(self, path)

        self.gui_image.configure(image=self.image)
        self.gui_image.bind("<Button-1>", lambda event: print('hello'))

        self.gui_name.configure(text=self.name)
        self.gui_name.bind("<Button-1>", lambda event: print('hello'))


class WindowManager(ttk.Frame):

    def __init__(self, master, path: str = None, *args, **kwargs) -> None:
        ttk.Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self._path = path
        self.items = {}

        for column, name in enumerate(listdir(self.path)):

            abspath = self.path + f'/{name}'
            self.items[name] = GuiFolder(self, row=0, column=column, path=abspath) if isdir(abspath) else GuiFile(self, row=0, column=column, path=abspath)

        # self.grid(row=0, column=0, sticky='nsew')

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, path: str) -> None:
        self._path = path
        self.update_items()

    def update_items(self):

        for label in self.items.values():
            label.destroy()

        self.items = {}

        for column, name in enumerate(listdir(self.path)):

            abspath = self.path + f'/{name}'
            self.items[name] = GuiFolder(self, row=0, column=column, path=abspath) if isdir(abspath) else GuiFile(self, row=0, column=column, path=abspath)


def main():
    root = tk.Tk()
    # root.geometry("700x350")

    frame = WindowManager(root, r'C:/Users/luisg/Documents/GitHub/pydrive/src/pydrive/gui')
    frame.pack()

    root.mainloop()


if __name__ == '__main__':
    main()
