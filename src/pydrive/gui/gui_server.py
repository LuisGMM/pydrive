
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog

from constants import *


class Main_frame(tk.Frame):

    def __init__(self, parent: tk.Tk) -> None:

        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.parent.title("Subir examen a universidad")
        self.parent.resizable(False, False)

        universidad_field = tk.Label(self.parent, text="Universidad", width=20)
        universidad_field.grid(column=0, row=0)

        self.universidad_combobox = ttk.Combobox(
            self.parent, values=list(ASIGNATURAS.keys()), width=60)
        self.universidad_combobox.bind("<<ComboboxSelected>>", self._subjects)
        self.universidad_combobox.grid(column=1, row=0)

    def _subjects(self, *args) -> None:

        self.subjects_label = tk.Label(
            self.parent, text="Asignaturas", width=20)
        self.subjects_label.grid(column=0, row=1)

        self.__subjects = list(
            ASIGNATURAS[self.universidad_combobox.get()].keys())
        self.__subjects.sort()

        self.subjects_combobox = ttk.Combobox(
            self.parent, values=self.__subjects, width=60)
        self.subjects_combobox.bind("<<ComboboxSelected>>", self._askfile)
        self.subjects_combobox.grid(column=1, row=1)

    def _askfile(self, *args) -> None:

        self.file_label = tk.Label(self.parent, text="Examen", width=20)
        self.file_label.grid(column=0, row=2)

        self.__subjects = list(
            ASIGNATURAS[self.universidad_combobox.get()].keys())
        self.__subjects.sort()

        self.file_label = tk.Label(self.parent, text="", width=20)
        self.file_label.grid(column=1, row=2)

        self.subjects_button = tk.Button(
            self.parent, text="Examinar", command=self._search_file)
        self.subjects_button.grid(column=2, row=2)

        self.upload_button = tk.Button(self.parent, text="Subir", command=lambda: Exam(self.universidad_combobox.get(), self.subjects_combobox.get(
        ), self.file).create_exam(self.filename, True, self.minutes_entry.get(), self.points_per_question_entry.get()))
        self.upload_button.grid(column=1, row=5)

    def _search_file(self):

        self.file = filedialog.askopenfilename(initialdir="/")
        self.filename = self.file.split('/')[-1]

        self.file_label = tk.Label(self.parent, text=self.filename, width=60)
        self.file_label.grid(column=1, row=2)

        self.minutes_label = tk.Label(
            self.parent, text="Duración (minutos)", width=20)
        self.minutes_label.grid(column=0, row=3)

        self.minutes_entry = tk.Entry(self.parent, justify="left", width=20)
        self.minutes_entry.grid(column=1, row=3)

        self.points_per_question_label = tk.Label(
            self.parent, text="Puntos por pregunta:", width=20)
        self.points_per_question_label.grid(column=0, row=4)

        self.points_per_question_entry = tk.Entry(
            self.parent, justify="left", width=20)
        self.points_per_question_entry.grid(column=1, row=4)


if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("600x300")
    APP = Main_frame(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
