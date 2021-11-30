from login_screen import LoginScreen
from tkinter import *

class UI:
    def __init__(self, root):
        self._root = root
        self._view = None

    def hide_view(self):
        if self._view is not None:
            self._view.destroy()
        self._view = None

    def initialize(self):
        self._current_view = LoginScreen(self._root)
        self._current_view.pack()

window = Tk()
window.title("LANDLORD APP")
window.geometry('500x300')
running_interface = UI(window)
running_interface.initialize()
window.mainloop()