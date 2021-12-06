from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from services.service import landlord_service

class SignupScreen:
    def __init__(self, root, stay_on_screen, go_back_screen):
        self._root = root
        self._frame = None
        self._stay_on_screen = stay_on_screen
        self._go_back_screen = go_back_screen
        self._username_field_input = None
        self._password_field_input = None
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def create_user_to_database(self):
        chosen_username = self._username_field_input.get()
        chosen_password = self._password_field_input.get()
        if landlord_service.get_user(chosen_username) is not None:
            messagebox.showinfo(title='Invalid input', message='Username already taken, please choose again!', icon='error')
            self._stay_on_screen()
        elif len(chosen_password) < 5:
            messagebox.showinfo(title='Invalid input', message='Password length less than five characters, please choose again!', icon='error')
            self._stay_on_screen()
        else:    
            landlord_service.create_user(chosen_username, chosen_password)
            self._go_back_screen()

    def initialize(self):
        self._frame = Frame(master=self._root)
        username_label = Label(master=self._frame, text='Choose username')
        self._username_field_input = Entry(master=self._frame)
        password_label = Label(master=self._frame, text='Choose Password')
        self._password_field_input = Entry(master=self._frame)
        
        create_user_button = Button(
            master=self._frame,
            text='Create account',
            command=self.create_user_to_database
        )

        go_back_button = Button(
            master=self._frame,
            text='Go back to login',
            command=self._go_back_screen
        )

        username_label.grid(pady=6, row=0, column=0)
        self._username_field_input.grid(pady=6, row=0, column=1)
        password_label.grid(pady=2, row=1, column=0)
        self._password_field_input.grid(pady=2, row=1, column=1)
        create_user_button.grid(row=2, column=1)
        go_back_button.grid(row=3, column=1)