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

    def list_all_units(self): # Not working
        list_of_units = landlord_service.get_units_owned()
        cols = ['1','2','3','4','5','6','7','8','9']
        tree = Treeview(self._root, columns=cols, show='headings')
        tree.heading('1', text='unit identifier')
        tree.heading('2', text='username')
        tree.heading('3', text='address')
        tree.heading('4', text='location')
        tree.heading('5', text='square meters')
        tree.heading('6', text='asking price')
        tree.heading('7', text='purchase price')
        tree.heading('8', text='aquisision time')
        tree.heading('9', text='owned')
        for i in range(0,len(list_of_units)):
            unit_to_insert = list_of_units[i]
            tree.insert(parent= "",index=i, values = unit_to_insert)
        tree.pack()

    def initialize(self):
        self._frame = Frame(master=self._root)

        list_all_units_button = Button(
            master=self._frame,
            text='List all units',
            command=self.list_all_units
        )

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self.main_menu)

        list_all_units_button.grid(pady=6, row=1, column=0)
        return_to_menu_button.grid(pady=6, row=2, column=0)
