__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.source.form import form_crud

class main:
    master = tkinter.Tk()
    form_crud(master)
    master.mainloop()