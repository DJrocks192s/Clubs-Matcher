from tkinter import *
from Widgets import Widgets
from tkinter import ttk

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"

class Frame5:

    def __init__(self, master, w, h):
        
        self.__width = w
        self.__height = h
        self.__master = Frame(master, width=self.__width, height=self.__height, bg=JET_BLACK)
    
    #helper methods
    
    def set_back_cmd(self, frame_dir):
        self.__back_direct = frame_dir
    
    def go_back(self):
        self.__back_direct.get_frame().tkraise()
    
    def set_view_results(self, view_output):
        self.__view_results = view_output # a dataframe of final assignments to be inputted into treeview
    
    def get_view_results(self):
        df_rows = self.__view_results.to_numpy().tolist()
        for row in df_rows:
            self.__treeview_results.insert("", "end", values=row)
        Widgets.place_Widgets(self.__treeview_results, 100, 200)
        for col in self.__columns_treeview:
            self.__treeview_results.heading(col, text=col.title())
        self._clickme_button.configure(state=DISABLED)
    def setupFrame(self):
        
        X_CENTRE = self.__width//2
        Y_CENTRE = self.__height//2
        EMAILSTARTX = X_CENTRE - 450
        EMAILENDY = Y_CENTRE - 100
        HEADING_START = X_CENTRE-248
        HEADING_END = X_CENTRE+248

        self.__back_button = Widgets(self.__master).create_button("Back", D_BROWN, ("Times New Roman", 30), 4, lambda: self.go_back())
        Widgets.place_Widgets(self.__back_button, 0, 0)
        
        self.__heading = Widgets(self.__master).create_label("Matching Results", CYAN, JET_BLACK, ("Times New Roman", 80))
        Widgets.place_Widgets(self.__heading, HEADING_START, 50)

        self._clickme_button = Widgets(self.__master).create_button("Click Here to load results", D_BROWN, ("Times New Roman", 15), 18, lambda: self.get_view_results())
        Widgets.place_Widgets(self._clickme_button, 100, 200)

        self.__columns_treeview = ["Student Name","Grade and Section", "House", "Club Assigned", "Classroom"]
        self.__treeview_results = Widgets(self.__master).create_treeview(self.__columns_treeview)
        Widgets.place_Widgets(self.__treeview_results, 100, 250)

    def get_frame(self):
        return self.__master