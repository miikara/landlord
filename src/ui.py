from ui.login_screen import LoginScreen
from ui.signup_screen import SignupScreen
from ui.menu_screen import MenuScreen
from ui.insert_units_screen import InsertUnitsScreen
from ui.insert_leases_screen import InsertLeasesScreen
from ui.insert_charges_screen import InsertChargesScreen
from ui.insert_rents_screen import InsertRentsScreen
from ui.sell_units_screen import SellUnitsScreen
from ui.get_statistics_screen import StatisticsScreen
from tkinter import *


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def hide_view(self):
        if self._current_view is not None:
            self._current_view.destroy()
        self._current_view = None

    def initialize(self):
        self._current_view = LoginScreen(
            self._root, self.show_signup_screen, self.show_login_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_login_screen(self):
        self.hide_view()
        self._current_view = LoginScreen(
            self._root, self.show_signup_screen, self.show_login_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_signup_screen(self):
        self.hide_view()
        self._current_view = SignupScreen(
            self._root, self.show_signup_screen, self.show_login_screen)
        self._current_view.pack()

    def show_menu_screen(self):
        self.hide_view()
        self._current_view = MenuScreen(self._root, self.show_menu_screen, self.show_login_screen, self.show_insert_units_screen, self.show_insert_leases_screen, self.show_insert_charges_screen, self.show_insert_rents_screen, self.show_sell_units_screen, self.show_statistics_screen)
        self._current_view.pack()

    def show_insert_units_screen(self):
        self.hide_view()
        self._current_view = InsertUnitsScreen(self._root, self.show_insert_units_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_insert_leases_screen(self):
        self.hide_view()
        self._current_view = InsertLeasesScreen(self._root, self.show_insert_leases_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_insert_charges_screen(self):
        self.hide_view()
        self._current_view = InsertChargesScreen(self._root, self.show_insert_charges_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_insert_rents_screen(self):
        self.hide_view()
        self._current_view = InsertRentsScreen(self._root, self.show_insert_rents_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_sell_units_screen(self):
        self.hide_view()
        self._current_view = SellUnitsScreen(self._root, self.show_sell_units_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_statistics_screen(self):
        self.hide_view()
        self._current_view = StatisticsScreen(self._root, self.show_statistics_screen, self.show_menu_screen)
        self._current_view.pack()


window = Tk()
window.title("LANDLORD APP")
window.geometry('1000x700')
running_interface = UI(window)
running_interface.initialize()
window.mainloop()
