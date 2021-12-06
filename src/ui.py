from ui.login_screen import LoginScreen
from ui.signup_screen import SignupScreen
from ui.menu_screen import MenuScreen
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
        self._current_view = LoginScreen(self._root, self.show_signup_screen, self.show_login_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_login_screen(self):
        self.hide_view()
        self._current_view = LoginScreen(self._root, self.show_signup_screen, self.show_login_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_signup_screen(self):
        self.hide_view()
        self._current_view = SignupScreen(self._root, self.show_signup_screen, self.show_login_screen, self.show_menu_screen)
        self._current_view.pack()

    def show_menu_screen(self):
        self.hide_view()
        self._current_view = MenuScreen(self._root, self.show_menu_screen)
        self._current_view.pack()

window = Tk()
window.title("LANDLORD APP")
window.geometry('500x300')
running_interface = UI(window)
running_interface.initialize()
window.mainloop()