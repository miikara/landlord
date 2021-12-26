import tkinter as tk
from tkinter import ttk
from services.service import landlord_service
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


class MenuScreen:
    def __init__(self, root, stay_on_screen, go_to_login_screen, go_to_insert_units_screen, go_to_insert_leases_screen, go_to_insert_charges_screen, go_to_insert_rents_screen, go_to_sell_units_screen, go_to_statistics_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_login_screen = go_to_login_screen
        self._go_to_insert_units_screen = go_to_insert_units_screen
        self._go_to_insert_leases_screen = go_to_insert_leases_screen
        self._go_to_insert_charges_screen = go_to_insert_charges_screen
        self._go_to_insert_rents_screen = go_to_insert_rents_screen
        self._go_to_sell_units_screen = go_to_sell_units_screen
        self._go_to_statistics_screen = go_to_statistics_screen
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack(fill=tk.constants.X)

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

    def sell_units(self):
        self._go_to_sell_units_screen()

    def graph_units(self):
        current_username = str(self._logged_in_user.username)
        dates, units = landlord_service.get_units_history(current_username)
        plt.plot(dates, units)
        plt.title('Portfolio size per month')
        plt.ylim(bottom=0)
        plt.ylabel('Amount of units')
        plt.xlabel('Year & month')
        plt.show()

    def graph_occupancy(self):
        current_username = str(self._logged_in_user.username)
        dates, occupancies = landlord_service.get_occupancy_history(
            current_username)
        plt.plot(dates, occupancies)
        plt.title('Occupancy per month')
        plt.ylabel('Occupancy')
        plt.xlabel('Year & month')
        plt.show()

    def initialize(self):
        self._frame = tk.Frame(master=self._root)

        self._frame.grid_columnconfigure(0, weight=2)
        self._frame.grid_columnconfigure(1, weight=2)

        user_label = tk.Label(
            master=self._frame, text=f'Logged in as {self._logged_in_user}  ', anchor='e')
        logout_button = tk.Button(
            master=self._frame, text='Logout', command=self.logout)

        manage_portfolio_label = tk.Label(
            master=self._frame, text='Manage portfolio information:', borderwidth=3, relief='ridge')
        portfolio_statistics_label = tk.Label(
            master=self._frame, text='Portfolio statistcs:', borderwidth=3, relief='ridge')

        insert_unit_button = tk.Button(
            master=self._frame, text='Insert unit', command=self._go_to_insert_units_screen)
        insert_lease_button = tk.Button(
            master=self._frame, text='Insert lease', command=self._go_to_insert_leases_screen)
        insert_charge_button = tk.Button(
            master=self._frame, text='Insert charge', command=self._go_to_insert_charges_screen)
        insert_rent_button = tk.Button(
            master=self._frame, text='Insert change in rent', command=self._go_to_insert_rents_screen)
        sell_unit_button = tk.Button(
            master=self._frame, text='Mark unit as sold', command=self._go_to_sell_units_screen)
        get_statistics_button = tk.Button(
            master=self._frame, text='Get unit level statistics', command=self._go_to_statistics_screen)
        graph_units_button = tk.Button(
            master=self._frame, text='Graph portfolio unit amount', command=self.graph_units)
        graph_occupancy_button = tk.Button(
            master=self._frame, text='Graph portfolio occupancy', command=self.graph_occupancy)

        user_label.grid(row=0, column=0, ipadx=15, ipady=15, sticky="nsew")
        logout_button.grid(row=0, column=1, columnspan=2, sticky='w')

        manage_portfolio_label.grid(
            row=1, column=0, ipadx=15, ipady=15, sticky="nsew")
        portfolio_statistics_label.grid(
            row=1, column=1, ipadx=15, ipady=15, sticky="nsew")

        insert_unit_button.grid(row=2, column=0)
        insert_lease_button.grid(row=3, column=0)
        insert_charge_button.grid(row=4, column=0)
        insert_rent_button.grid(row=5, column=0)
        sell_unit_button.grid(row=6, column=0)
        get_statistics_button.grid(row=2, column=1)
        graph_units_button.grid(row=3, column=1)
        graph_occupancy_button.grid(row=4, column=1)
