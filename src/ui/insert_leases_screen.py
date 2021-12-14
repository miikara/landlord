import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import *
from services.service import landlord_service


class InsertLeasesScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._unit_id_field_input = None
        self._start_date_field_input = None
        self._end_date_on_contract_field_input = None
        self._tenant_field_input = None
        self._original_monthly_rent_field_input = None
        self._maximum_annual_rent_increase_field_input = None
        self._rent_due_date_field_input = None
        self._deposit_field_input = None
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _main_menu(self):
        self._go_to_menu_screen()

    def create_lease_to_database(self):
        chosen_unit_id = self._unit_id_field_input.get()
        chosen_start_date = self._start_date_field_input.get_date()
        chosen_end_date_on_contract = self._end_date_on_contract_field_input.get_date()
        chosen_tenant = self._tenant_field_input.get()
        chosen_original_monthly_rent = self._original_monthly_rent_field_input.get()
        chosen_maximum_annual_rent_increase = self._maximum_annual_rent_increase_field_input.get()
        chosen_rent_due_date = self._rent_due_date_field_input.get()
        chosen_deposit = self._deposit_field_input.get()
        landlord_service.create_lease(chosen_unit_id, chosen_start_date, chosen_end_date_on_contract, chosen_tenant, chosen_original_monthly_rent, chosen_maximum_annual_rent_increase, chosen_rent_due_date, chosen_deposit)
        self._main_menu()

    def initialize(self):
        self._frame = Frame(master=self._root)
        this_year = datetime.datetime.now().year

        unit_id_label = Label(master=self._frame, text='Unit id')
        self._unit_id_field_input = Entry(master=self._frame)      
        start_date_label = Label(master=self._frame, text='Lease start date')
        self._start_date_field_input = Calendar(self._frame, selectmode='day', 
            year=this_year, day=1, month=1, date_pattern='dd/MM/yyyy')
        end_date_on_contract_label = Label(master=self._frame, text='Lease contract end date')
        self._end_date_on_contract_field_input = Calendar(self._frame, selectmode='day', 
            year=this_year, day=1, month=1, date_pattern='dd/MM/yyyy')
        tenant_label = Label(master=self._frame, text='Tenant name')
        self._tenant_field_input = Entry(master=self._frame)   
        original_monthly_rent_label = Label(master=self._frame, text='Monthly rent')
        self._original_monthly_rent_field_input = Entry(master=self._frame) 
        maximum_annual_rent_increase_label = Label(master=self._frame, text='Maximum annual rent increase (%)')
        self._maximum_annual_rent_increase_field_input = Entry(master=self._frame) 
        rent_due_date_label = Label(master=self._frame, text='Rent due day of month')
        self._rent_due_date_field_input = Entry(master=self._frame) 
        deposit_label = Label(master=self._frame, text='Deposit')
        self._deposit_field_input = Entry(master=self._frame) 


        # Input field grids here
        unit_id_label.grid(pady=6, row=0, column=0)
        self._unit_id_field_input.grid(pady=6, row=0, column=1)
        start_date_label.grid(pady=20, row=1, column=0)
        self._start_date_field_input.grid(pady=20, row=1, column=1)
        end_date_on_contract_label.grid(pady=20, row=2, column=0)
        self._end_date_on_contract_field_input.grid(pady=20, row=2, column=1)
        tenant_label.grid(pady=6, row=3, column=0)
        self._tenant_field_input.grid(pady=6, row=3, column=1)        
        original_monthly_rent_label.grid(pady=6, row=4, column=0)
        self._original_monthly_rent_field_input.grid(pady=6, row=4, column=1)
        maximum_annual_rent_increase_label.grid(pady=6, row=5, column=0)
        self._maximum_annual_rent_increase_field_input.grid(pady=6, row=5, column=1)
        rent_due_date_label.grid(pady=6, row=6, column=0)
        self._rent_due_date_field_input.grid(pady=6, row=6, column=1)
        deposit_label.grid(pady=6, row=7, column=0)
        self._deposit_field_input.grid(pady=7, row=7, column=1)

        # Action buttons
        create_lease_button = Button(
            master=self._frame,
            text='Add lease contract',
            command=self.create_lease_to_database
        )

        create_lease_button.grid(pady=8, row=8, column=1)

        return_to_menu_button = Button(
            master=self._frame, 
            text='Return to menu', 
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=9, column=1)