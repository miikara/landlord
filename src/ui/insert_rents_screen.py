import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import *
from services.service import landlord_service


class InsertRentsScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._unit_id_field_input = None
        self._start_date_field_input = None
        self._amount_field_input = None
        self._due_dom_field_input = None
        self._end_date_field_input = None
        self._end_previous_rent_field_state = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def create_rent_to_database(self):
        chosen_unit_id = self._unit_id_field_input.get()
        chosen_start_date = self._start_date_field_input.get_date()
        chosen_amount = self._amount_field_input.get()
        chosen_due_dom = self._due_dom_field_input.get()
        if self._end_previous_rent_field_state.instate(['selected']):
            rent_id_to_end = landlord_service.get_latest_rent_id(chosen_unit_id)
            landlord_service.end_rent(rent_id_to_end, chosen_start_date)
            landlord_service.create_rent(chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom)
        else:
            landlord_service.create_maintenance_charge(chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom)
        self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)
        this_year = datetime.datetime.now().year

        unit_id_label = Label(master=self._frame, text='Unit id')
        self._unit_id_field_input = Entry(master=self._frame)      
        start_date_label = Label(master=self._frame, text='Rent start date')
        self._start_date_field_input = Calendar(self._frame, selectmode='day', 
            year=this_year, day=1, month=1, date_pattern='YYYY/MM/DD')  
        amount_label = Label(master=self._frame, text='Amount')
        self._amount_field_input = Entry(master=self._frame)  
        due_dom_label = Label(master=self._frame, text='Rent due day of month')
        self._due_dom_field_input = Entry(master=self._frame) 
        end_previous_label = Checkbutton(master=self._frame, text='End previous rent') 
        self._end_previous_rent_field_state = end_previous_label

        unit_id_label.grid(pady=6, row=0, column=0)
        self._unit_id_field_input.grid(pady=6, row=0, column=1)
        start_date_label.grid(pady=20, row=1, column=0)
        self._start_date_field_input.grid(pady=20, row=1, column=1)
        amount_label.grid(pady=6, row=2, column=0)
        self._amount_field_input.grid(pady=6, row=2, column=1)        
        due_dom_label.grid(pady=6, row=3, column=0)
        self._due_dom_field_input.grid(pady=6, row=3, column=1)
        end_previous_label.grid(pady=6, row=4, column=1)

        create_rent_button = Button(
            master=self._frame,
            text='Add rent to unit',
            command=self.create_rent_to_database
        )

        create_rent_button.grid(pady=8, row=5, column=1)

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=6, column=1)