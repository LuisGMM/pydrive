
import tkinter as tk

from gui import gui_server


ROOT = tk.Tk()
ROOT.geometry("600x300")
APP = gui_server.CreateServerFrame(parent=ROOT)
APP.mainloop()
ROOT.destroy()