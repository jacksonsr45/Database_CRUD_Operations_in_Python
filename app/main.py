__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app import colors, fonts
from app.screens.template import Template

class Main:
    root = tkinter.Tk()
    Template(root, colors, fonts)
    root.mainloop()