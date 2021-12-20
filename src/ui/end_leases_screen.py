import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import *
from services.service import landlord_service

# Implement similar logic to statistics screen where you choose unit id and see leases and then choose lease to end
class EndLeasesScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._unit_id_field_input = None
        self._end_date_field_input = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def end_lease_in_database(self):
        self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)

        unit_id_label = Label(master=self._frame, text='Unit id')
        self._unit_id_field_input = Entry(master=self._frame)     

        # Input field grids here
        unit_id_label.grid(pady=6, row=0, column=0)
        self._unit_id_field_input.grid(pady=6, row=0, column=1)

        # Action buttons
        create_lease_button = Button(
            master=self._frame,
            text='End lease contract',
            command=self.create_lease_to_database
        )

        create_lease_button.grid(pady=8, row=8, column=1)

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=9, column=1)