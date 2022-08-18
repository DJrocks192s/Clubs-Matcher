from tkinter import *
from tkinter import messagebox
from Widgets import Widgets
import pandas as pd
from tkinter import filedialog as fd

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"

class Frame4:

    def __init__(self, master, w, h):
        
        self.__width = w
        self.__height = h
        self.__master = Frame(master, width=self.__width, height=self.__height, bg=JET_BLACK)
    
    #helper methods
    
    def set_back_cmd(self, frame_dir):
        self.__back_direct = frame_dir
    
    def go_back(self):
        self.__back_direct.get_frame().tkraise()

    def set_logout_cmd(self, frame_dir):
        self.__logout_direct = frame_dir
    
    def go_to_frame_1(self):
        self.__logout_direct.get_frame().tkraise()
    
    def logout_button_cmd(self):
        confirm_logout = messagebox.askyesno("Logout Confirmation", "Are you sure you wish to logout? You will lose all unsaved data.")
        if confirm_logout:
            self.go_to_frame_1()

    def set_view_cmd(self, frame_dir):
        self.__view_direct = frame_dir
    
    def go_to_frame_5(self):
        self.__view_direct.set_view_results(self.__output) # sends DataFrame acrosss to frame 8
        self.__view_direct.get_frame().tkraise()

    def export_results_cmd(self):
        """
        ------------------------
        * Write DataFrame to Excel file to save results
        ------------------------
        """

        # getting path to save results file
        self.__output_file_path = fd.asksaveasfilename(confirmoverwrite=True, defaultextension='xlsx', title="Save Results")
        try:
            self.__writer_object = pd.ExcelWriter(self.__output_file_path)
            self.__output.to_excel(self.__writer_object) # writing the DataFrame to excel
            self.__writer_object.save()
        except:
            pass
        else:
            messagebox.showinfo("Results Exported!", f"The final assignment has been exported into an excel file at the following location: {self.__output_file_path}")
    
    def set_output_processor(self, output): # passed on from frame 6
        self.__output = output # dataframe of final assignments

    def view_results_cmd(self):
        self.go_to_frame_5()

    def setupFrame(self):
        
        X_CENTRE = self.__width//2
        Y_CENTRE = self.__height//2
        EMAILSTARTX = X_CENTRE - 450
        EMAILENDY = Y_CENTRE - 100
        HEADING_START = X_CENTRE-248
        HEADING_END = X_CENTRE+248

        self.__back_button = Widgets(self.__master).create_button("Back", D_BROWN, ("Times New Roman", 30), 4, lambda: self.go_back())
        Widgets.place_Widgets(self.__back_button, 0, 0)
        
        self.__logout_button = Widgets(self.__master).create_button("Logout", D_BROWN, ("Times New Roman", 30), 7, lambda: self.logout_button_cmd())
        Widgets.place_Widgets(self.__logout_button, self.__width - 135, 0)

        self.__heading = Widgets(self.__master).create_label("Matching Results", CYAN, JET_BLACK, ("Times New Roman", 80))
        Widgets.place_Widgets(self.__heading, HEADING_START, 100)

        self.__matching_success = Widgets(self.__master).create_label("The matching was successful.", WHITE, JET_BLACK, ("Times New Roman", 50))
        Widgets.place_Widgets(self.__matching_success, HEADING_START - 15, Y_CENTRE - 150)

        self.__view_button = Widgets(self.__master).create_button("View Results", D_BROWN, ("Times New Roman", 30), 15, lambda: self.view_results_cmd())
        Widgets.place_Widgets(self.__view_button, X_CENTRE - 250, EMAILENDY + 200)

        self.__export_button = Widgets(self.__master).create_button("Save Results", D_BROWN, ("Times New Roman", 30), 15, lambda: self.export_results_cmd())
        Widgets.place_Widgets(self.__export_button, X_CENTRE + 100, EMAILENDY + 200)

    def get_frame(self):
        return self.__master