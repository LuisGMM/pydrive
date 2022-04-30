
import tkinter as tk

from pydrive.gui.gui_filemanager import WindowManager
from pydrive.gui.treedirectory import TreeDirectory


class FileExplorer(tk.Frame):

    def __init__(self, parent, path: str, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.path = path

        # self.parent.title = 'File Explorer'
        self.pack()

        self.treedirectory = TreeDirectory(self, self.path)
        # self.treedirectory.pack(fill=tk.Y, side=tk.LEFT, expand=tk.YES)
        self.treedirectory.grid(row=0, column=0, sticky="NSW")

        self.windowmanager = WindowManager(self, self.path)
        # self.windowmanager.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        self.windowmanager.grid(row=0, column=1, sticky="NSW")


def main():
    root = tk.Tk()
    # root.geometry("700x350")

    root.title = 'File Explorer'
    root.iconbitmap(r'C:\Users\luisg\Documents\GitHub\pydrive\src\pydrive\gui\images\folder.png')

    frame = FileExplorer(root, r'C:/Users/luisg/Documents/GitHub/pydrive/src/pydrive/gui')
    frame.pack(fill=tk.BOTH, expand=tk.YES)

    root.mainloop()
