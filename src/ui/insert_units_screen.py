import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import *
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
        self._acquired_date_field_input = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def _input_not_empty_check(self, input_to_check, label=""):
        if input_to_check == "":
            messagebox.showinfo(title='Invalid input', message=f'{label} must not be empty', icon='error')
            return False
        else:
            return True

    def _input_integer_check(self, input_to_check, label=""):
        try:
            int(input_to_check)
            return True
        except ValueError:
            messagebox.showinfo(title='Invalid input', message=f'{label} must be an integer', icon='error')
            return False

    def _input_float_check(self, input_to_check, label=""):
        try:
            float(input_to_check)
            return True
        except ValueError:
            messagebox.showinfo(title='Invalid input', message=f'{label} must be an number', icon='error')
            return False

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
        chosen_acquired_date = self._acquired_date_field_input.get_date()
        if self._input_not_empty_check(chosen_address, label='Chosen address field') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_location, label='Chosen location field') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_location, label='Chosen construction year') ==  False:
            self._stay_on_screen()
        elif self._input_integer_check(chosen_construction_year, label='Chosen construction year') == False:
            self._stay_on_screen()
        elif self._input_integer_check(chosen_square_meters, label='Chosen square meters') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_address, label='Chosen purchase price field') == False:
            self._stay_on_screen()
        elif self._input_float_check(chosen_purchase_price, label='Chosen purchase price price') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_acquired_date, label='Chosen acquired date') == False:
            self._stay_on_screen()
        else:
            landlord_service.create_unit(chosen_address, chosen_location, chosen_construction_year, chosen_sewage_year, chosen_facade_year, chosen_windows_year, chosen_elevator_year, 
                                    chosen_has_elevator, chosen_square_meters, chosen_floor, chosen_asking_price, chosen_purchase_price, chosen_acquired_date)
            messagebox.showinfo(title='Success', message=f'Unit succesfully created')
            self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)
        this_year = datetime.datetime.now().year

        address_label = Label(master=self._frame, text='Address')
        self._address_field_input = Entry(master=self._frame)
        location_label = Label(master=self._frame, text='Location')
        self._location_field_input = Entry(master=self._frame)
        construction_year_label = Label(master=self._frame, text='Construction year')
        self._construction_year_field_input = Entry(master=self._frame)
        sewage_year_label = Label(master=self._frame, text='Sewage repair year (optional)') 
        self._sewage_year_field_input = Entry(master=self._frame)
        facade_year_label = Label(master=self._frame, text='Facade repair year (optional)') 
        self._facade_year_field_input = Entry(master=self._frame)
        windows_year_label = Label(master=self._frame, text='Window repair year (optional)') 
        self._windows_year_field_input = Entry(master=self._frame)
        elevator_year_label = Label(master=self._frame, text='Elevator repair year (optional)') 
        self._elevator_year_field_input = Entry(master=self._frame)
        elevator_button = Checkbutton(master=self._frame, text='Building has elevator (optional)') 
        self._has_elevator_field_state = elevator_button
        square_meters_label = Label(master=self._frame, text='Square meters')
        self._square_meters_field_input = Entry(master=self._frame)
        floor_label = Label(master=self._frame, text='Floor (optional)')
        self._floor_field_input = Entry(master=self._frame)
        asking_price_label = Label(master=self._frame, text='Asking price (optional)')
        self._asking_price_field_input = Entry(master=self._frame)
        purchase_price_label = Label(master=self._frame, text='Purchase price')
        self._purchase_price_field_input = Entry(master=self._frame)
        acquired_date_label = Label(master=self._frame, text='Acquired date')
        self._acquired_date_field_input = Calendar(self._frame, selectmode='day', 
            year=this_year, day=1, month=1, date_pattern='YYYY-MM-DD')

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
        acquired_date_label.grid(pady=6, row=12, column=0)
        self._acquired_date_field_input.grid(pady=6, row=12, column=1)

        create_unit_button = Button(
            master=self._frame,
            text='Add unit',
            command=self.create_unit_to_database
        )

        create_unit_button.grid(pady=6, row=13, column=1)

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=14, column=1)