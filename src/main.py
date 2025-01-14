from tkinter import *
from Widgets import Widgets
from RootWindow import RootWindow
from Frame1 import Frame1
from Frame2 import Frame2
from Frame3 import Frame3
from Frame4 import Frame4
from Frame5 import Frame5

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"


if __name__ == '__main__':
    root = Tk()
    root_screen = RootWindow(root, root.winfo_screenwidth(), root.winfo_screenheight())

    # initialising and placing all frames (currently empty)
    screen_1 = Frame1(root, root.winfo_screenwidth(), root.winfo_screenheight())
    Widgets.place_Widgets(screen_1.get_frame(), 0, 0)

    screen_2 = Frame2(root, root.winfo_screenwidth(), root.winfo_screenheight())
    Widgets.place_Widgets(screen_2.get_frame(), 0, 0)

    screen_3 = Frame3(root, root.winfo_screenwidth(), root.winfo_screenheight())
    Widgets.place_Widgets(screen_3.get_frame(), 0, 0)

    screen_4 = Frame4(root, root.winfo_screenwidth(), root.winfo_screenheight())
    Widgets.place_Widgets(screen_4.get_frame(), 0, 0)

    screen_5 = Frame5(root, root.winfo_screenwidth(), root.winfo_screenheight())
    Widgets.place_Widgets(screen_5.get_frame(), 0, 0)

    # connecting frames placing all the frame widgets

    screen_1.set_register_cmd(screen_2)
    screen_1.set_login_cmd(screen_3)
    screen_1.setupFrame()

    screen_2.set_back_cmd(screen_1)
    screen_2.set_register_cmd(screen_1)
    screen_2.setupFrame()

    screen_3.set_logout_cmd(screen_1)
    screen_3.set_match_cmd(screen_4)
    screen_3.setupFrame()

    screen_4.set_back_cmd(screen_3)
    screen_4.set_logout_cmd(screen_1)
    screen_4.set_view_cmd(screen_5)
    screen_4.setupFrame()

    screen_5.set_back_cmd(screen_4)
    screen_5.setupFrame()

    screen_1.get_frame().tkraise()

    root.mainloop()
