
import tkinter as tk

from gui import create_server


ROOT = tk.Tk()
ROOT.geometry("600x300")
APP = create_server.CreateServerFrame(parent=ROOT)
APP.mainloop()
ROOT.destroy()
