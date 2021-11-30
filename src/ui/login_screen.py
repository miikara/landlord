from tkinter import *
from tkinter.ttk import *

class LoginScreen:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = Frame(master = self._root)
        
        username_label = Label(master = self._frame, text = 'Username')
        username_entry = Entry(master = self._frame)
        password_label = Label(master = self._frame, text = 'Password')
        password_entry = Entry(master = self._frame)
        
        login_button = Button(master = self._frame, text = 'Login')

        create_account_button = Button(
            master = self._frame,
            text = 'Sign up'
        )

        username_label.grid(pady = 6, row = 0, column = 0)
        username_entry.grid(pady = 6,row = 0, column = 1)
        password_label.grid(pady = 2, row= 1 , column = 0)
        password_entry.grid(pady = 2,row = 1, column = 1)
        login_button.grid(row = 2, column = 1)
        create_account_button.grid(row = 3, column = 1)