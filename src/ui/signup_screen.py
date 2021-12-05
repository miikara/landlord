from tkinter import *
from tkinter.ttk import *
from services.service import LandlordService # toimii
s = LandlordService() # testi

class SignupScreen:
    def __init__(self, root, handle_show_login_screen):
        self._root = root
        self._frame = None
        self._handle_show_login_screen = handle_show_login_screen
        self._handle_create_user = None
        self.initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = Frame(master=self._root)

        choose_username_label = Label(master=self._frame, text='Choose your username')
        choose_username_entry = Entry(master=self._frame)
        choose_password_label = Label(master=self._frame, text='Choose your password')
        choose_password_entry = Entry(master=self._frame)
        
        signup_button = Button(
            master=self._frame,
            text='Create account'
        )

        go_back_button = Button(
            master=self._frame,
            text='Go back',
            command=self._handle_show_login_screen
        )


        choose_username_label.grid(pady=6, row=0, column=0)
        choose_username_entry.grid(pady=6, row=0, column=1)
        choose_password_label.grid(pady=2, row=1, column=0)
        choose_password_entry.grid(pady=2, row=1, column=1)
        signup_button.grid(row=2,column=1)
        go_back_button.grid(row=3, column=1)