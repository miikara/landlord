from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class MenuScreen:
    def __init__(self, root, stay_on_screen, go_to_login_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_to_login_screen = go_to_login_screen # lisätty
        self._logged_in_user = landlord_service.get_logged_in_user()
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def logout(self):
        landlord_service.logout()
        self._logged_in_user = None
        self._go_to_login_screen()
        
    def initialize(self):
        self._frame = Frame(master=self._root)
        user_label = Label(master=self._frame, text=f'Logged in as {self._logged_in_user}')
        logout_button = Button(master=self._frame, text='Logout', command=self.logout)
        user_label.grid(row=1, column=1)
        logout_button.grid(row=2, column=1)
