from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class StatisticsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def main_menu(self):
        self._go_to_menu_screen()

    def list_all_units(self):
        pass

    def initialize(self):
        self._frame = Frame(master=self._root)
        return_to_menu_button = Button(master=self._frame, text='Nothing here', command=self._go_to_menu_screen)
        return_to_menu_button.pack()
