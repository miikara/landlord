from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service


class LoginScreen:
    def __init__(self, root, go_to_signup_screen, stay_on_screen, go_to_menu_screen):
        self._root = root
        self._frame = None
        self._go_to_signup_screen = go_to_signup_screen
        self._stay_on_screen = stay_on_screen
        self._go_to_menu_screen = go_to_menu_screen
        self._username_field_input = None
        self._password_field_input = None
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def attempt_login(self):
        entered_username = self._username_field_input.get()
        entered_password = self._password_field_input.get()
        if landlord_service.get_user(entered_username) is None:
            messagebox.showinfo(
                title='Invalid input', message='Username not found, please check your input!', icon='error')
            self._stay_on_screen()
        else:
            password_in_database = landlord_service.get_password(
                entered_username)
            if password_in_database == str(entered_password):
                landlord_service.login(entered_username, entered_password)
                self._go_to_menu_screen()
            else:
                messagebox.showinfo(
                    title='Invalid input', message='Incorrect password, please check your input!', icon='error')
                self._stay_on_screen()

    def initialize(self):
        self._frame = Frame(master=self._root)
        username_label = Label(master=self._frame, text='Enter username')
        self._username_field_input = Entry(master=self._frame)
        password_label = Label(master=self._frame, text='Enter password')
        self._password_field_input = Entry(master=self._frame)

        login_button = Button(master=self._frame,
                              text='Login', command=self.attempt_login)

        create_account_button = Button(
            master=self._frame, text='Sign up', command=self._go_to_signup_screen)

        username_label.grid(pady=6, row=0, column=0)
        self._username_field_input.grid(pady=6, row=0, column=1)
        password_label.grid(pady=2, row=1, column=0)
        self._password_field_input.grid(pady=2, row=1, column=1)
        login_button.grid(row=2, column=1)
        create_account_button.grid(row=3, column=1)
