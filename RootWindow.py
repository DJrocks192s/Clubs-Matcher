from tkinter import *

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"


class RootWindow():

    def __init__(self, master, width, height):
        self.__master = master
        self.__master.title("Clubs Matching System")

        self.__width = width
        self.__height = height
        self.__master.geometry(f"{self.__width}x{self.__height}")

        self.__master.configure(bg=L_BROWN)
