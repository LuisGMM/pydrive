
import tkinter as tk

from pydrive.gui.gui_filemanager import WindowManager
from pydrive.gui.treedirectory import TreeDirectory


class FileExplorer(tk.Frame):

    def __init__(self, parent, path: str, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self._path = path
        self.max_path = path

        # self.parent.title = 'File Explorer'
        self.pack()

        self.pathbar = tk.Label(self, text=self.path)
        self.pathbar.grid(row=0, column=0, columnspan=2, sticky='NEWS')

        self.treedirectory = TreeDirectory(self, self.path)
        # self.treedirectory.pack(fill=tk.Y, side=tk.LEFT, expand=tk.YES)
        self.treedirectory.grid(row=1, column=0, sticky="NSW")

        self.windowmanager = WindowManager(self, self.path)
        # self.windowmanager.pack(fill=tk.BOTH, side=tk.RIGHT, expand=tk.YES)
        self.windowmanager.grid(row=1, column=1, sticky="NSW")


def main():
    root = tk.Tk()
    # root.geometry("700x350")

    root.title = 'File Explorer'
    root.iconbitmap(r'C:\Users\luisg\Documents\GitHub\pydrive\src\pydrive\gui\images\file2.png')

    frame = FileExplorer(root, r'C:/Users/luisg/Documents/GitHub/pydrive/src/pydrive/gui')
    frame.pack(fill=tk.BOTH, expand=tk.YES)

    root.mainloop()


if __name__ == '__main__':
    main()
