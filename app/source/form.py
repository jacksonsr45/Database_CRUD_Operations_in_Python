__author__ = 'jacksonsr45@gmail.com'

import tkinter
from app.data.form_data import data

class form_crud(data):
    def __init__(self, master):
        
        __font_Button__ = ("Ubunto", 17)
        __font__ = ("Ubunto", 12)

        self.master = master
        self.master.title("CRUD SQLITE3 IN PYTHON")
        self.master.geometry("900x300")

        self.frame_side_right = tkinter.Frame(self.master)
        self.frame_side_right.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        self.frame_side_left = tkinter.Frame(self.master)
        self.frame_side_left.configure(bg="powder blue")
        self.frame_side_left.place(relx=0, rely=0, relwidth=0.7, relheight=0.7)

        #Campos de novo cadastro
        self.name = tkinter.Label(self.frame_side_left)
        self.name.configure(bg="powder blue")
        self.name.configure(font=__font__)
        self.name.configure(text="Name:")
        self.name.configure(anchor=tkinter.E)
        self.namebox = tkinter.Entry(self.frame_side_left)

        self.lastname = tkinter.Label(self.frame_side_left)
        self.lastname.configure(bg="powder blue")
        self.lastname.configure(font=__font__)
        self.lastname.configure(text="Last Name:")
        self.lastname.configure(anchor=tkinter.E)
        self.lastnamebox = tkinter.Entry(self.frame_side_left)
        
        self.id = tkinter.Label(self.frame_side_left)
        self.id.configure(bg="powder blue")
        self.id.configure(font=__font__)
        self.id.configure(anchor=tkinter.E)
        self.id.configure(text="ID:")
        self.idbox = tkinter.Entry(self.frame_side_left)
        
        self.phone = tkinter.Label(self.frame_side_left)
        self.phone.configure(bg="powder blue")
        self.phone.configure(font=__font__)
        self.phone.configure(anchor=tkinter.E)
        self.phone.configure(text="Phone:")
        self.phonebox = tkinter.Entry(self.frame_side_left)

        self.name.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)
        self.namebox.place(relx=0.2, rely=0.1, relwidth=0.20, relheight=0.1)

        self.lastname.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.1)
        self.lastnamebox.place(relx=0.2, rely=0.25, relwidth=0.25, relheight=0.1)
        
        self.id.place(relx=0.1, rely=0.40, relwidth=0.1, relheight=0.1)
        self.idbox.place(relx=0.2, rely=0.40, relwidth=0.25, relheight=0.1)
        
        self.phone.place(relx=0.1, rely=0.55, relwidth=0.1, relheight=0.1)
        self.phonebox.place(relx=0.2, rely=0.55, relwidth=0.20, relheight=0.1)


        
        

        #=============================Buttons============================================================================================#
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