__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.model.crud_model import *

class data(object):
    def __init__(self):
        self.namebox            = tkinter.Entry()
        self.lastnamebox        = tkinter.Entry()
        self.idbox              = tkinter.Entry()
        self.phonebox           = tkinter.Entry()

    def View_frame(self):
        pass

    def InitDb(self):
        Create()