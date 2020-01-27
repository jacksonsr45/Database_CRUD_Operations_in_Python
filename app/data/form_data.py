__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.model.crud_model import *

class data(object):
    def __init__(self):
        self.namebox            = tkinter.Entry()
        self.lastnamebox        = tkinter.Entry()
        self.idbox              = tkinter.Entry()
        self.phonebox           = tkinter.Entry()
        self.frameList          = tkinter.Listbox()
        self.searchbox          = tkinter.Entry()

    def __View_frame__(self, *args):
        searchStd = self.frameList.curselection()[0]
        sd = self.frameList.get(searchStd)
        self.namebox.delete(0,tkinter.END)
        self.namebox.insert(tkinter.END,sd[1])
        self.lastnamebox.delete(0,tkinter.END)
        self.lastnamebox.insert(tkinter.END,sd[2])
        self.idbox.delete(0,tkinter.END)
        self.idbox.insert(tkinter.END,sd[3])
        self.phonebox.delete(0,tkinter.END)
        self.phonebox.insert(tkinter.END,sd[4])
        
    def __Search__(self):
        self.__Clear__()
        self.frameList.delete(0, tkinter.END)
        if self.searchbox.get():
            for row in Search(self.searchbox.get()):
                self.frameList.insert(tkinter.END, row)
        else:
            for row in Search_All():
                self.frameList.insert(tkinter.END, row)
    
    def __Save__(self):
        Save(self.namebox.get(), self.lastnamebox.get(), self.idbox.get(), self.phonebox.get())
        self.__Clear__()
        self.__Search__()
    
    def __Update__(self):
        Update(self.namebox.get(), self.lastnamebox.get(), self.idbox.get(), self.phonebox.get())
        self.__Clear__()
        self.__Search__()
    
    def __Delete__(self):
        Delele(self.namebox.get())
        self.__Clear__()
        self.__Search__()
    
    def __Clear__(self):
        self.namebox.delete(0,tkinter.END)
        self.lastnamebox.delete(0,tkinter.END)
        self.idbox.delete(0,tkinter.END)
        self.phonebox.delete(0,tkinter.END)

    def __InitDb__(self):
        Create()