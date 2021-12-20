from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from typing import Collection
from services.service import landlord_service


class StatisticsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._selected_unit_id = IntVar(master=self._root, value=0)
        self._logged_in_user = landlord_service.get_logged_in_user()
        self._list_of_units = []
        self._tenant_name = StringVar(master=self._root, value="Nakkimies")
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def main_menu(self):
        self.destroy_list_of_units()
        self._go_to_menu_screen()

    def list_all_units(self):
        list_of_units = landlord_service.get_units_owned()
        cols = ['1','2','3','4','5','6','7']
        tree = Treeview(self._root, columns=cols, show='headings', selectmode='browse')
        for col in range(0,len(cols)):
            col_name = cols[col]
            tree.column(col_name, anchor=CENTER, width=110)
        tree.heading('1', text='unit identifier', anchor=CENTER)
        tree.heading('2', text='address', anchor=CENTER)
        tree.heading('3', text='location', anchor=CENTER)
        tree.heading('4', text='construction year', anchor=CENTER)
        tree.heading('5', text='square meters', anchor=CENTER)
        tree.heading('6', text='floor', anchor=CENTER)
        tree.heading('7', text='purchase price', anchor=CENTER)
        for i in range(0,len(list_of_units)):
            unit_to_insert = list_of_units[i]
            tree.insert(parent= "",index=i, values = unit_to_insert)
        self._list_of_units = tree

    def show_list_of_units(self):
        self.list_all_units()
        self._list_of_units.pack()

    def destroy_list_of_units(self):
        self._list_of_units.destroy()

    def get_selected_unit_id(self):
        selected_unit = self._list_of_units.focus()
        unit_id  = self._list_of_units.item(selected_unit).get('values')[0]
        self._selected_unit_id.set(value=int(unit_id))

    def get_latest_tenant(self):
        selected_unit_id = int(self._selected_unit_id.get())
        tenant = landlord_service.get_latest_active_lease_tenant(selected_unit_id)
        self._tenant_name.set(value=str(tenant))

    def get_all_statistics(self):
        self.get_selected_unit_id() # Asettaa id:n oikein
        self.get_latest_tenant() # Asettaa tenantin nimen

    def initialize(self):
        self._frame = Frame(master=self._root)

        list_all_units_button = Button(
            master=self._frame,
            text='List all units',
            command=self.show_list_of_units
        )

        hide_all_units_button = Button(
            master=self._frame,
            text='Hide unit list',
            command=self.destroy_list_of_units
        )

        get_unit_statistics_button = Button(
            master=self._frame,
            text='Show statistics for selected unit',
            command=self.get_all_statistics
        )

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self.main_menu)
        
        tenant_label = Label(
            master=self._frame,
            textvariable=self._tenant_name)

        list_all_units_button.grid(pady=6, row=1, column=0)
        hide_all_units_button.grid(pady=6, row=1, column=1)
        get_unit_statistics_button.grid(pady=6, row=2, column=1)
        return_to_menu_button.grid(pady=6, row=3, column=0)
        tenant_label.grid(pady=6, row=5, column=1)
