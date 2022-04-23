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

        for w in (self, main_window):
            w.rowconfigure(0, weight=1)
            w.columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")

        self.directories: dict[str, str] = {}

        self.file_image: tk.PhotoImage = tk.PhotoImage(file="/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui/file.png")
        self.folder_image: tk.PhotoImage = tk.PhotoImage(file="/home/luisgmm/Documents/GitHub/pydrive/src/pydrive/gui/folder.png")

        self.load_tree(abspath(sep))

    def listdir(self, path: str) -> list:
        '''Returns a list with the directories in that `path`.
        Is there is no permission to acces `path` it returns an empty list.

        Args:
            path (str): Path directory to explore its contents.

        Returns:
            list: Contains the names of the directories (folders and files) in that path.
        '''
        try:
            return listdir(path)

        except PermissionError as e:
            print(str(e))

            return []

    def get_icon(self, path: str) -> tk.PhotoImage:
        '''Get the corresponding image depending if `path` corresponds to a file or a folder.

        Args:
            path (str): Directory of the item we want an icon for.

        Returns:
            tk.PhotoImage: Icon image corresponding to `path`.
        '''
        return self.folder_image if isdir(path) else self.file_image

    def insert_item(self, name: str, path: str, parent_uid: str = "") -> str:
        '''Inserts the item located at `path` inside its parent `parent_uid` in the treeview
        and store the item in `self.directories`.

        Args:
            name (str): Text identifying the item in the treeview.
            path (str): Location of the item.
            parent_uid (str, optional): Parent of the item in the treeview. Defaults to "".

        Returns:
            str: The unique identifier of the inserted item.
        '''
        uid = self.treeview.insert(parent_uid, tk.END, text=name, tags=("fstag",), image=self.get_icon(path))
        self.directories[uid] = path

        return uid

    def load_tree(self, path: str, parent_uid: str = "") -> None:
        '''Loads the content of the directory `path` in the treeview and in `self.directories`.

        Args:
            path (str): Location of the directory
            parent_uid (str, optional): Parent unique identifier. Defaults to "".
        '''
        for fsobj in self.listdir(path):

            fullpath: str = join(path, fsobj)
            child: str = self.insert_item(fsobj, fullpath, parent_uid)

            if isdir(fullpath):

                for sub_fsobj in self.listdir(fullpath):
                    self.insert_item(sub_fsobj, join(fullpath, sub_fsobj), child)

    def load_subitems(self, uid: str) -> None:
        '''Loads the contents of `uid` if it is a folder.

        Args:
            uid (str): Unique identifier of the item.
        '''
        for child_uid in self.treeview.get_children(uid):

            if isdir(self.directories[child_uid]):

                self.load_tree(self.directories[child_uid], parent_uid=child_uid)

    def event_item_opened(self, event) -> None:
        '''Event invoked when a an item is opened.
        It loads the contents of of that item the the treeview and updated `self.directories`.

        Note that it does not distinguishes between files and folders. If the event is triggered
        with a file, which obviously has not items inside, it will runs anyway but do nothing.

        Args:
            event (_type_): Tkinter event argument.
        '''
        uid: str = self.treeview.selection()[0]
        self.load_subitems(uid)


if __name__ == '__main__':

    main_window = tk.Tk()
    app = TreeDirectory(main_window)
    app.mainloop()