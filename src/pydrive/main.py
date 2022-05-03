
from concurrent.futures import ThreadPoolExecutor
# import tkinter as tk

from pydrive.gui import fileexplorer

# ROOT = tk.Tk()
# ROOT.geometry("600x300")
# APP = create_server.CreateServerFrame(parent=ROOT)
# APP.mainloop()
# ROOT.destroy()


def foo():
    for i in range(10000000):
        print(i**2)


with ThreadPoolExecutor() as pool:
    pool.submit(fileexplorer.main)
    pool.submit(foo)
