from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class MenuScreen:
    def __init__(self, root, stay_on_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = Frame(master=self._root)
        menu_label = Label(text='Main Menu')
        menu_label.grid(row=1, column=0)
