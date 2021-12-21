from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from typing import Collection
from services.service import landlord_service
import babel.numbers


class StatisticsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._selected_unit_id = IntVar(master=self._root, value=0)
        self._logged_in_user = landlord_service.get_logged_in_user()
        self._list_of_units = None
        self._tenant_name = StringVar(master=self._root, value="")
        self._cap_rate = StringVar(master=self._root, value="")
        self._noi = StringVar(master=self._root, value="")
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def main_menu(self):
        self.destroy_list_of_units()
        self._go_to_menu_screen()

    def populate_list_of_units(self):
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
            tree.insert(parent= "",index=i, iid=f'row{i}' ,values = unit_to_insert)
        self._list_of_units = tree

    def destroy_list_of_units(self):
        self._list_of_units.destroy()

    def get_selected_unit_id(self):
        selected_unit = self._list_of_units.focus()
        unit_id  = self._list_of_units.item(selected_unit).get('values')[0]
        self._selected_unit_id.set(value=int(unit_id))

    def get_latest_tenant(self):
        selected_unit_id = int(self._selected_unit_id.get())
        tenant = str(landlord_service.get_latest_active_lease_tenant(selected_unit_id))
        self._tenant_name.set(value=f'Current tenant: {tenant}')

    def get_latest_cap_rate(self):
        selected_unit_id = int(self._selected_unit_id.get())
        cap_rate = landlord_service.get_cap_rate(selected_unit_id)
        cap_rate_formatted = '{:.1%}'.format(cap_rate)
        self._cap_rate.set(value=f'Cap rate without renovations: {cap_rate_formatted}')

    def get_latest_noi(self):
        selected_unit_id = int(self._selected_unit_id.get())
        noi = str(landlord_service.get_noi(selected_unit_id))
        noi_formatted = babel.numbers.format_currency(noi, 'EUR', locale='en_US')
        self._noi.set(value=f'Current net operating income per year: {noi_formatted}')

    def get_all_statistics(self):
        self.get_selected_unit_id()
        self.get_latest_tenant()
        self.get_latest_cap_rate()
        self.get_latest_noi()


    def initialize(self):
        self._frame = Frame(master=self._root)

        Style().configure(style='green/black.TLabel', foreground = 'blue', background = 'white')

        get_unit_statistics_button = Button(
            master=self._frame,
            text='Show statistics',
            command=self.get_all_statistics
        )

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self.main_menu)
        
        message_label = Label(
            master=self._frame,
            style='green/black.TLabel',
            text='Click on unit and "show statistics" button to see core information for selected unit.'
        )

        tenant_text_label=Label(
            master=self._frame,
            text='Current tenant'
        )

        tenant_label = Label(
            master=self._frame,
            font=('Calibri', 12, 'bold'),
            textvariable=self._tenant_name
            )

        noi_label = Label(
            master=self._frame,
            font=('Calibri', 12, 'bold'),
            textvariable=self._noi)

        cap_rate_label = Label(
            master=self._frame,
            font=('Calibri', 12, 'bold'),
            textvariable=self._cap_rate)
        
        self.populate_list_of_units()
        self._list_of_units.pack(fill='x')
        if len(landlord_service.get_units_owned()) > 0:
            children = self._list_of_units.get_children()
            if children:
                self._list_of_units.focus(children[0])
                self._list_of_units.selection_set(children[0])

        get_unit_statistics_button.pack(expand=True)
        return_to_menu_button.pack(expand=True)
        message_label.pack(expand=True)
        tenant_label.pack(side='top', ipady=10, expand=True)
        cap_rate_label.pack(side='top', ipady=10, expand=True)
        noi_label.pack(side='top', ipady=10, expand=True)
