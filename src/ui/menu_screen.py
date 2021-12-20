from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class MenuScreen:
    def __init__(self, root, stay_on_screen, go_to_login_screen, go_to_insert_units_screen, go_to_insert_leases_screen, go_to_insert_charges_screen, go_to_insert_rents_screen, go_to_statistics_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_login_screen = go_to_login_screen
        self._go_to_insert_units_screen = go_to_insert_units_screen
        self._go_to_insert_leases_screen = go_to_insert_leases_screen
        self._go_to_insert_charges_screen = go_to_insert_charges_screen
        self._go_to_insert_rents_screen = go_to_insert_rents_screen
        self._go_to_statistics_screen = go_to_statistics_screen
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def logout(self):
        landlord_service.logout()
        self._logged_in_user = None
        self._go_to_login_screen()

    def insert_units(self):
        self._go_to_insert_units_screen()

    def insert_leases(self):
        self._go_to_insert_leases_screen()

    def insert_charges(self):
        self._go_to_insert_charges_screen()

    def insert_rents(self):
        self._go_to_insert_rents_screen()

    def initialize(self):
        self._frame = Frame(master=self._root)
        user_label = Label(master=self._frame, text=f'Logged in as {self._logged_in_user}')
        logout_button = Button(master=self._frame, text='Logout', command=self.logout)
        insert_unit_button = Button(master=self._frame, text='Insert unit', command=self._go_to_insert_units_screen)
        insert_lease_button = Button(master=self._frame, text='Insert lease', command=self._go_to_insert_leases_screen)
        insert_charge_button = Button(master=self._frame, text='Insert charge', command=self._go_to_insert_charges_screen)
        insert_rent_button = Button(master=self._frame, text='Insert change in rent', command=self._go_to_insert_rents_screen)
        get_statistics_button = Button(master=self._frame, text='Get statistics', command=self._go_to_statistics_screen)
        user_label.grid(row=1, column=1)
        insert_unit_button.grid(row=2, column=1)
        insert_lease_button.grid(row=3, column=1)
        insert_charge_button.grid(row=4, column=1)
        insert_rent_button.grid(row=5, column=1)
        get_statistics_button.grid(row=6, column=1)
        logout_button.grid(row=7, column=1)
