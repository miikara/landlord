from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class InsertUnitsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._address_field_input = None
        self._location_field_input = None
        self._construction_year_field_input = None
        self._sewage_year_field_input = None
        self._facade_year_field_input = None
        self._windows_year_field_input = None
        self._elevator_year_field_input = None
        self._has_elevator_field_state = None
        self._square_meters_field_input = None
        self._floor_field_input = None
        self._asking_price_field_input = None
        self._purchase_price_field_input = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def create_unit_to_database(self):
        chosen_address = self._address_field_input.get()
        chosen_location = self._location_field_input.get()
        chosen_construction_year = self._construction_year_field_input.get()
        chosen_sewage_year = self._sewage_year_field_input.get()
        chosen_facade_year = self._facade_year_field_input.get()
        chosen_windows_year = self._windows_year_field_input.get()
        chosen_elevator_year = self._elevator_year_field_input.get()
        if self._has_elevator_field_state.instate(['selected']):
            chosen_has_elevator = 1
        else:
            chosen_has_elevator = 0
        chosen_square_meters = self._square_meters_field_input.get()
        chosen_floor = self._floor_field_input.get()
        chosen_asking_price = self._asking_price_field_input.get()
        chosen_purchase_price = self._purchase_price_field_input.get()
        landlord_service.create_unit(chosen_address, chosen_location, chosen_construction_year, chosen_sewage_year, chosen_facade_year, chosen_windows_year, chosen_elevator_year, 
                                    chosen_has_elevator, chosen_square_meters, chosen_floor, chosen_asking_price, chosen_purchase_price)
        self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)
        address_label = Label(master=self._frame, text='Address')
        self._address_field_input = Entry(master=self._frame)
        location_label = Label(master=self._frame, text='Location')
        self._location_field_input = Entry(master=self._frame)
        construction_year_label = Label(master=self._frame, text='Construction year')
        self._construction_year_field_input = Entry(master=self._frame)
        sewage_year_label = Label(master=self._frame, text='Sewage repair year') 
        self._sewage_year_field_input = Entry(master=self._frame)
        facade_year_label = Label(master=self._frame, text='Facade repair year') 
        self._facade_year_field_input = Entry(master=self._frame)
        windows_year_label = Label(master=self._frame, text='Window repair year') 
        self._windows_year_field_input = Entry(master=self._frame)
        elevator_year_label = Label(master=self._frame, text='Elevator repair year') 
        self._elevator_year_field_input = Entry(master=self._frame)
        elevator_button = Checkbutton(master=self._frame, text='Building has elevator') 
        self._has_elevator_field_state = elevator_button
        square_meters_label = Label(master=self._frame, text='Square meters')
        self._square_meters_field_input = Entry(master=self._frame)
        floor_label = Label(master=self._frame, text='Floor')
        self._floor_field_input = Entry(master=self._frame)
        asking_price_label = Label(master=self._frame, text='Asking price')
        self._asking_price_field_input = Entry(master=self._frame)
        purchase_price_label = Label(master=self._frame, text='Purchase price')
        self._purchase_price_field_input = Entry(master=self._frame)

        address_label.grid(pady=6, row=0, column=0)
        self._address_field_input.grid(pady=6, row=0, column=1)
        location_label.grid(pady=6, row=1, column=0)
        self._location_field_input.grid(pady=6, row=1, column=1)
        construction_year_label.grid(pady=6, row=2, column=0)
        self._construction_year_field_input.grid(pady=6, row=2, column=1)
        sewage_year_label.grid(pady=6, row=3, column=0)
        self._sewage_year_field_input.grid(pady=6, row=3, column=1)
        facade_year_label.grid(pady=6, row=4, column=0)
        self._facade_year_field_input.grid(pady=6, row=4, column=1)
        windows_year_label.grid(pady=6, row=5, column=0)
        self._windows_year_field_input.grid(pady=6, row=5, column=1)
        elevator_year_label.grid(pady=6, row=6, column=0)
        self._elevator_year_field_input.grid(pady=6, row=6, column=1)
        elevator_button.grid(pady=6,row=7,column=1)
        square_meters_label.grid(pady=6, row=8, column=0)
        self._square_meters_field_input.grid(pady=6, row=8, column=1)
        floor_label.grid(pady=6, row=9, column=0)
        self._floor_field_input.grid(pady=6, row=9, column=1)
        asking_price_label.grid(pady=6, row=10, column=0)
        self._asking_price_field_input.grid(pady=6, row=10, column=1)
        purchase_price_label.grid(pady=6, row=11, column=0)
        self._purchase_price_field_input.grid(pady=6, row=11, column=1)

        create_unit_button = Button(
            master=self._frame,
            text='Add unit',
            command=self.create_unit_to_database
        )

        create_unit_button.grid(pady=6, row=12, column=1)

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=13, column=1)