from tkinter import *
from tkinter import ttk

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"


class Widgets:
    def __init__(self, root):
        self.__root = root

    def create_label(self, text, fg, bg, font):
        self.__label = Label(
            self.__root,
            text=text,
            fg=fg,
            bg=bg,
            font=font
        )
        return self.__label

    def create_button(self, text, fg, font, breadth, command):
        self.__button = Button(
            self.__root,
            text=text,
            fg=fg,
            font=font,
            width=breadth,
            command=command,
        )
        return self.__button

    def create_entry_box(self, breadth, font, textvariable, fg):
        self.__entry_box = Entry(
            self.__root,
            width=breadth,
            font=font,
            textvariable=textvariable,
            fg=fg
        )
        return self.__entry_box

    def create_pwd_entry_box(self, breadth, font, textvariable, fg):
        self.__pwdentry_box = Entry(
            self.__root,
            width=breadth,
            font=font,
            textvariable=textvariable,
            fg=fg,
            show="*"
        )
        return self.__pwdentry_box
    
    def create_confirm_pwd_entry_box(self, breadth, font, textvariable, fg):
        self.__confirm_pwdentry_box = Entry(
            self.__root,
            width=breadth,
            font=font,
            textvariable=textvariable,
            fg=fg,
            show="*"
        )
        return self.__confirm_pwdentry_box

    def create_treeview(self, columns):
        self.__treeview_table = ttk.Treeview(
            self.__root,
            columns=columns
        )
        return self.__treeview_table

    def place_Widgets(widget, x, y):
        widget.place(
            x=x,
            y=y
        )
