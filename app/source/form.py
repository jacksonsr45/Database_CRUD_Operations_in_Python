__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.data.form_data import data

class form_crud(data):
    def __init__(self, master):
        
        __font_Button__ = ("Ubunto", 15)

        self.master = master
        self.master.title("CRUD SQLITE3 IN PYTHON")
        self.master.geometry("900x600")

        self.frame_side_right = tkinter.Frame(self.master)
        self.frame_side_right.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        self.frame_side_left = tkinter.Frame(self.master)
        self.frame_side_left.configure(bg="powder blue")
        self.frame_side_left.place(relx=0, rely=0, relwidth=0.7, relheight=0.7)

        self.frame_side_down = tkinter.Frame(self.master)
        self.frame_side_down.configure(bg="powder blue")
        self.frame_side_down.place(relx=0, rely=0.7, relwidth=0.7, relheight=0.3)

        
        self.button_save = tkinter.Button(self.frame_side_down)
        self.button_save.configure(border=0)
        self.button_save.configure(font= __font_Button__)
        self.button_save.configure(bg="powder blue")
        self.button_save.configure(text="Save")
        
        self.button_update = tkinter.Button(self.frame_side_down)
        self.button_update.configure(border=0)
        self.button_update.configure(font= __font_Button__)
        self.button_update.configure(bg="powder blue")
        self.button_update.configure(text="Update")
        
        self.button_delete = tkinter.Button(self.frame_side_down)
        self.button_delete.configure(border=0)
        self.button_delete.configure(font= __font_Button__)
        self.button_delete.configure(bg="powder blue")
        self.button_delete.configure(text="Delete")
        
        
        self.button_save.place(relx=0.1, rely=0.5, relwidth=0.15, relheight=0.3)
        self.button_update.place(relx=0.3, rely=0.5, relwidth=0.15, relheight=0.3)
        self.button_delete.place(relx=0.5, rely=0.5, relwidth=0.15, relheight=0.3)