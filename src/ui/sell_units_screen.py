import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import *
from services.service import landlord_service


class SellUnitsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._unit_id_field_input = None
        self._sold_date_field_input = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def sell_unit(self):
        chosen_unit_id = self._unit_id_field_input.get()
        chosen_sold_date = self._sold_date_field_input.get_date()
        landlord_service.sell_unit_and_set_sold_date(
            chosen_unit_id, chosen_sold_date)
        self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)
        this_year = datetime.datetime.now().year
        unit_id_label = Label(master=self._frame, text='Unit id')
        self._unit_id_field_input = Entry(master=self._frame)
        sold_date_label = Label(master=self._frame, text='Sold date')
        self._sold_date_field_input = Calendar(self._frame, selectmode='day',
                                               year=this_year, day=1, month=1, date_pattern='YYYY-MM-DD')

        unit_id_label.grid(pady=6, row=0, column=0)
        self._unit_id_field_input.grid(pady=6, row=0, column=1)
        sold_date_label.grid(pady=6, row=1, column=0)
        self._sold_date_field_input.grid(pady=6, row=1, column=1)

        sell_unit_button = Button(
            master=self._frame,
            text='Mark unit as sold',
            command=self.sell_unit
        )

        sell_unit_button.grid(pady=6, row=2, column=1)

        return_to_menu_button = Button(
            master=self._frame,
            text='Return to menu',
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=3, column=1)
