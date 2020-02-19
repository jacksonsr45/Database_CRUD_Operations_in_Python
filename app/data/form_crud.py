__author__ = "jacksonsr45@gmail.com"

import tkinter
from .import *


class Crude:
    def __init__( self, root):
        self.root = root
        x = (self.root.winfo_screenwidth() // 2) - (900 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        self.root.geometry("900x300+{}+{}".format( x, y))
        self.root.resizable(width=False, height=False)
        self.root.title("CRUD")


        self.list = tkinter.StringVar()

        self.frame_side_right = self.__frame__( self.root, color['black'],
                            0, 0, color['blue'], 0.7, 0, 0.3, 1)

        self.frame_side_left = self.__frame__( self.root, color['black'],
                            0, 0, color['blue'], 0, 0, 0.7, 0.7)

        self.frame_side_down = self.__frame__( self.root, color['black'],
                            0, 0, color['blue'], 0, 0.7, 0.7, 0.3)

        self.frame_list = self.__listbox__(self.frame_side_right, 0, 
                font['font_list'], self.list.get(), self.view_frame, 
                0.01, 0, 0.95, 0.9)

        self.scrollbar = self.__scrollbar__(self.frame_side_right, 
                        self.frame_list.yview, 0.95, 0, 0.5, 0.9)

        self.frame_list.configure(yscrollcommand=self.scrollbar.set)


    def view_frame(self):
        pass


    def __button__(self, root, text, font, bd, bg, state, x, 
                    y, width, height, command=None):
        button = tkinter.Button(root)
        button.configure(text=text)
        button.configure(font=font)
        button.configure(bd=bd)
        button.configure(bg=bg)
        button.configure(state=state)
        button.configure(command=command)
        button.place(relx=x, rely=y, relwidth=width, relheight=height)
        return button


    def __frame__(self, root, highlightbackground, 
                highlightthickness, bd, bg, x, y, width, height):
        frame = tkinter.Frame(root)
        frame.configure(highlightbackground=highlightbackground)
        frame.configure(highlightthickness=highlightthickness)
        frame.configure(bd=bd)
        frame.configure(bg=bg)
        frame.place(relx=x, rely=y, relwidth=width, relheight=height)
        return frame


    def __entry__(self, root, font, textvariable, bd, state, 
                    bg, x, y, width, height, show=None):
        entry = tkinter.Entry(root)
        entry.configure(font=font)
        entry.configure(show=show)
        entry.configure(textvariable=textvariable)
        entry.configure(bd=0)
        entry.configure(state=state)
        entry.configure(bg=bg)
        entry.place(relx=x, rely=y, relwidth=width, relheight=height)
        return entry


    def __label__(self, root, font, bg, text, x, y, width, height):
        label = tkinter.Label(root)
        label.configure(font=font)
        label.configure(anchor=tkinter.E)
        label.configure(bg=bg)
        label.configure(text=text)
        label.place(relx=x, rely=y, relwidth=width, relheight=height)
        return label


    def __listbox__(self, root, bd, font, 
                insert_value, in_command, x, y, width, height):
        listbox = tkinter.Listbox(root)
        listbox.configure(bd = bd)
        listbox.configure(font = font)
        listbox.insert(tkinter.END, insert_value)
        listbox.bind('<<ListboxSelect>>', in_command)
        listbox.place(relx=x, rely=y, relwidth=width, relheight=height)
        return listbox


    def __scrollbar__( self, root, command, x, y, width, height):
        scrollbar = tkinter.Scrollbar(root)
        scrollbar.configure(command=command)
        scrollbar.place(relx=x, rely=y, relwidth=width, relheight=height)
        return scrollbar


    def __text__(self, root, bd, font, x, y, width, height):
        text = tkinter.Text(root)
        text.configure( bd= bd)
        text.configure( font= font)
        text.place(relx=x, rely=y, relwidth=width, relheight=height)
        return text