__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.data.form_crud import Crude

class Main:
    root = tkinter.Tk()
    Crude(root)
    root.mainloop()