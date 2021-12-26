import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from services.service import landlord_service


class InsertChargesScreen:
    def __init__(self, root, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._unit_id_field_input = None
        self._start_date_field_input = None
        self._type_field_input = None
        self._amount_field_input = None
        self._due_dom_field_input = None
        self._description_field_input = None
        self._end_date_field_input = None
        self._end_previous_charge_field_state = None
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
            messagebox.showinfo(
                title='Invalid input', message=f'{label} must not be empty', icon='error')
            return False
        else:
            return True

    def _input_integer_check(self, input_to_check, label=""):
        try:
            int(input_to_check)
            return True
        except ValueError:
            messagebox.showinfo(
                title='Invalid input', message=f'{label} must be an integer', icon='error')
            return False

    def _input_float_check(self, input_to_check, label=""):
        try:
            float(input_to_check)
            return True
        except ValueError:
            messagebox.showinfo(
                title='Invalid input', message=f'{label} must be an number', icon='error')
            return False

    def create_maintenance_charge_to_database(self):
        chosen_unit_id = self._unit_id_field_input.get()
        chosen_start_date = self._start_date_field_input.get_date()
        chosen_amount = self._amount_field_input.get()
        chosen_due_dom = self._due_dom_field_input.get()

        if self._input_not_empty_check(chosen_unit_id, label='Chosen unit id') == False:
            self._stay_on_screen()
        elif self._input_integer_check(chosen_unit_id, label='Chosen unit id') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_start_date, label='Chosen start date') == False:
            self._stay_on_screen()
        elif self._input_not_empty_check(chosen_amount, label='Chosen amount') == False:
            self._stay_on_screen()
        elif self._input_float_check(chosen_amount, label='Chosen amount') == False:
            self._stay_on_screen()
        elif self._end_previous_charge_field_state.instate(['selected']):
            charge_id_to_end = landlord_service.get_latest_maintenance_charge_id(
                chosen_unit_id)
            landlord_service.end_maintenance_charge(
                charge_id_to_end, chosen_start_date)
            landlord_service.create_maintenance_charge(
                chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom)
            messagebox.showinfo(
                title='Success', message=f'Charge succesfully created')
            self._main_menu()
        else:
            landlord_service.create_maintenance_charge(
                chosen_unit_id, chosen_start_date, chosen_amount, chosen_due_dom)
            messagebox.showinfo(
                title='Success', message=f'Charge succesfully created')
            self._main_menu()

    def initialize(self):
        self._frame = tk.Frame(master=self._root)
        this_year = datetime.datetime.now().year

        unit_id_label = tk.Label(master=self._frame, text='Unit id')
        self._unit_id_field_input = tk.Entry(master=self._frame)
        start_date_label = tk.Label(
            master=self._frame, text='Charge start date')
        self._start_date_field_input = Calendar(self._frame, selectmode='day',
                                                year=this_year, day=1, month=1, date_pattern='YYYY/MM/DD')
        amount_label = tk.Label(master=self._frame, text='Amount')
        self._amount_field_input = tk.Entry(master=self._frame)
        due_dom_label = tk.Label(master=self._frame,
                                 text='Charge due day of month (optional)')
        self._due_dom_field_input = tk.Entry(master=self._frame)
        end_previous_label = ttk.Checkbutton(
            master=self._frame, text='End previous charge')
        self._end_previous_charge_field_state = end_previous_label

        unit_id_label.grid(pady=6, row=0, column=0)
        self._unit_id_field_input.grid(pady=6, row=0, column=1)
        start_date_label.grid(pady=20, row=1, column=0)
        self._start_date_field_input.grid(pady=20, row=1, column=1)
        amount_label.grid(pady=6, row=2, column=0)
        self._amount_field_input.grid(pady=6, row=2, column=1)
        due_dom_label.grid(pady=6, row=3, column=0)
        self._due_dom_field_input.grid(pady=6, row=3, column=1)
        end_previous_label.grid(pady=6, row=4, column=1)

        create_charge_button = tk.Button(
            master=self._frame,
            text='Add charge to unit',
            command=self.create_maintenance_charge_to_database
        )

        create_charge_button.grid(pady=8, row=5, column=1)

        return_to_menu_button = tk.Button(
            master=self._frame,
            text='Return to menu',
            command=self._go_to_menu_screen)

        return_to_menu_button.grid(pady=6, row=6, column=1)
