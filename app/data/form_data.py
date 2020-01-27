__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.model.crud_model import *

class data(object):
    def __init__(self):
        self.namebox            = tkinter.Entry()
        self.lastnamebox        = tkinter.Entry()
        self.idbox              = tkinter.Entry()
        self.phonebox           = tkinter.Entry()

        self.searchbox          = tkinter.Entry()

    def __View_frame__(self):
        pass

    def __Search__(self):
        pass
    
    def __Save__(self):
        pass
    
    def __Update__(self):
        pass
    
    def __Delete__(self):
        pass

    def __InitDb__(self):
        Create()