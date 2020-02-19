__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.data.form_crud import Crude
from app.model.crud_model import Create


class Main:
    Create()
    root = tkinter.Tk()
    Crude(root)
    root.mainloop()