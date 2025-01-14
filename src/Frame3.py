from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from OutputProcessor import OutputProcessor
import numpy as np
from scipy.optimize import linear_sum_assignment
from Widgets import Widgets
from StudentDataReader import StudentDataReader
from ClubDataReader import ClubDataReader
from Processor import Processor

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"

class Frame3:
    """
    -----------------------
    * Frame for home screen
    * Allows user to upload student and club data as required, and then match students to clubs
    * Carries out validation checks on the entered data
    -----------------------
    """

    # Initialize the frame's dimensions and colour
    def __init__(self, master, w, h):
        
        self.__width = w
        self.__height = h
        self.__master = Frame(master, width=self.__width, height=self.__height, bg=JET_BLACK)
    
    # Resets data when user leaves the screen
    def initialise_details(self):
        self.__stu_msg_text.configure(text="Uploaded Student Data:          none")
        self.__club_msg_text.configure(text="Uploaded Club Data:              none")
        self.__student_records, self.__club_records = [] , {}

    # Helper method
    # Store passed login screen frame object as an attribute to be called
    def set_logout_cmd(self, frame_dir):
        self.__logout_direct = frame_dir
    
    # Helper method
    # Raise the frame for the login screen
    def go_to_frame_1(self):
        self.__logout_direct.get_frame().tkraise()
    
    # Command for logout button. Reset details and go to login screen.
    def logout_cmd(self):
        confirm_logout = messagebox.askyesno("Logout Confirmation", "Are you sure you wish to logout? You will lose all unsaved data.")
        if confirm_logout:
            self.initialise_details()
            self.go_to_frame_1()

    # Command for read student data button
    def read_stu_data(self):
        """
        ------------------------
        * Allow user to upload a file
        * Validate file – Presence check, type check, format check
        * If uploaded file is valid then get the data and show status that it has been uplaoded
        ------------------------
        """
        
        self.__student_file_name = fd.askopenfilename(title="Upload Student Data", initialdir="/")

        # validating the students file

        # presence check
        if self.__student_file_name != "":
            # type check
            if self.__student_file_name[-4:] == "xlsx" or self.__student_file_name[-3:] == "xls": # if the file is an excel file
                # format check
                try: # checking if the file can be processed
                    self.__student_file = StudentDataReader(self.__student_file_name)
                except KeyError:
                    messagebox.showerror("Excel file not in required format",
                    "Please ensure that the uploaded excel file is of the correct form, with correct data.")
                    return
            else: # not an excel file
                messagebox.showerror("Incorrect file format", "Please upload an excel file with extension .xls or .xlsx")
                return
        else: # no file uploaded
            messagebox.showwarning("No file uploaded", "Please upload a file")
            return
        self.__student_records = self.__student_file.get_student_records()
        self.__stu_msg_text.configure(text=f"Uploaded Student Data:       {self.__student_file_name} ✓")

    # Command for read club data button
    def read_club_data(self):
        """
        ------------------------
        * Allow user to upload a file
        * Validate file – Presence check, type check, format check
        * If uploaded file is valid then get the data and show status that it has been uplaoded
        ------------------------
        """

        self.__club_file_name = fd.askopenfilename(title="Upload Club Data", initialdir="/") # opening the clubs file
        
        # validating the clubs file

        # presence check
        if self.__club_file_name != "": # a file is uploaded
            # type check
            if self.__club_file_name[-4:] == "xlsx" or self.__club_file_name[-3:] == "xls": #if the file is an excel file
                # format check
                try: # checking if the file can be processed
                    self.__club_file = ClubDataReader(self.__club_file_name)
                except KeyError: 
                    messagebox.showerror("Excel file not in required format",
                    "Please ensure that the uploaded excel file is of the correct form, with correct data.")
                    return
            else: # not an excel file
                messagebox.showerror("Incorrect file format", "Please upload an excel file with extension .xls or .xlsx")
                return
        else: # no file uploaded
            messagebox.showwarning("No file uploaded", "Please upload a file")
            return
        self.__club_records = self.__club_file.get_club_records()
        self.__club_msg_text.configure(text=f"Uploaded Club Data:           {self.__club_file_name} ✓")

    # Helper method
    # Store the passed matching successful screen frame object as an attribute to be called
    def set_match_cmd(self, frame_dir):
        self.__match_direct = frame_dir
    
    # Helper method
    # Pass matching results to the matching successful frame and raise the frame
    def go_to_frame_4(self):
        self.__match_direct.set_output_processor(self.__FINAL_results)
        self.__match_direct.get_frame().tkraise()

    # Command for match button.
    def match_results(self):
        """
        ------------------------
        * Carry out main functionality of the application:
            * Processing input data:
                * Call the Processor helper class to process raw student records to a hash map
                * Convert the hash map to a graph by calling the convert_hashmap_to_graph() method
            * Matching students to clubs
                * Take the graph and find a maximum weighted matching using the Scipy library
            * Processing output assingments
                * Take the output matching and process it by calling the OutputProcessor helper class
        * Reset details of entered data before going to the matching successful screen
        * Show an error in matching if any of the above operations fail
        ------------------------
        """

        try:
            # Process raw student and club data into a hash map
            self.__last_dict = Processor.process(self.__student_records, self.__club_records)
            # Converting the hash map to a graph with student nodes and club nodes
            self.__final_list = Frame3.convert_hashmap_to_graph(self.__last_dict, [])
            self.__final_graph = np.array(self.__final_list)
            # Matching students to clubs
            row_indices, col_indices = linear_sum_assignment(self.__final_graph, maximize=True)
            row_names = [i for i in self.__last_dict.keys()]
            column_names = [i for i in self.__last_dict[1]]
            self.__final_assignment_list = [((row_names[r], column_names[c])) for r, c in zip(row_indices, col_indices)]
            # Process output assignment
            self.__output_object = OutputProcessor(self.__student_file, self.__club_file, self.__final_assignment_list)
            self.__FINAL_results = self.__output_object.process()
            # Reset details
            self.initialise_details()
            # Go to matching successful screen
            self.go_to_frame_4()
        except:
            messagebox.showwarning("Could Not Match!", "Please make sure you've uploaded the correct files and that they have the right data.")
    
    # Helper method
    # Convert Hash map to graph
    @staticmethod
    def convert_hashmap_to_graph(hashmap, graph_matrix):
        """
        ------------------------
        * Input:
            * HashMap has key as student ID, and value as another hash map
            * This second hash map has key as club ID, and value as the happiness score of the student to the particular club
            * Graph is empty to begin with
        * Convert the hash map to a graph that is stored as a 2D matrix. Rows are student ID nodes; Columns are club ID nodes.
          A value in the matrix, graph_matrix[i][j] is an edge in the graph with a weight of the happiness score of student i
          being mapped to club j
        ------------------------
        """
        for i in range(len(hashmap)): 
            row = []
            for j in hashmap[int(i+1)].values():
                row.append(j)
            graph_matrix.append(row)
        return graph_matrix

    # exposes the final graph attribute
    def get_final_list(self):
        return self.__final_list


    # Set up all the widgets inside the Frame
    def setupFrame(self):
        """
        ------------------------
        * Create instances of the Widgets class to create Tkinter widgets in the frame.
        * Widgets created in this frame include:
            * Labels: Heading, Uploaded student data, Uploaded club data
            * Buttons: Logout, Read student data, Read club data, Match
        ------------------------
        """

        X_CENTRE = self.__width//2
        Y_CENTRE = self.__height//2
        EMAILSTARTX = X_CENTRE - 450
        EMAILENDY = Y_CENTRE - 100
        HEADING_START = X_CENTRE-248
        HEADING_END = X_CENTRE+248

        # Create logout button
        self.__logout_button = Widgets(self.__master).create_button("Logout", D_BROWN, ("Times New Roman", 30), 7, lambda: self.logout_cmd())
        Widgets.place_Widgets(self.__logout_button, self.__width - 135, 0)

        # Create heading label
        self.__heading = Widgets(self.__master).create_label("Clubs Matcher", CYAN, JET_BLACK, ("Times New Roman", 80))
        Widgets.place_Widgets(self.__heading, HEADING_START, 100)

        # Create read student data button
        self.__student_data = Widgets(self.__master).create_button("1) Read Student Data", D_BROWN, ("Times New Roman", 30), 20, lambda: self.read_stu_data())
        Widgets.place_Widgets(self.__student_data, EMAILSTARTX - 50, EMAILENDY)

        # Create read club data button
        self.__club_data = Widgets(self.__master).create_button("2) Read Club Data", D_BROWN, ("Times New Roman", 30), 20, lambda: self.read_club_data())
        Widgets.place_Widgets(self.__club_data, X_CENTRE - 150, EMAILENDY)

        # Create match button
        self.__match = Widgets(self.__master).create_button("3) Match!", D_BROWN, ("Times New Roman", 30), 20, lambda: self.match_results())
        Widgets.place_Widgets(self.__match, X_CENTRE + 200, EMAILENDY)

        # Create uploaded student data label
        self.__stu_msg_text = Widgets(self.__master).create_label("Uploaded Student Data:          none", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__stu_msg_text, EMAILSTARTX - 50, EMAILENDY + 100)

        # Create uploaded club data label
        self.__club_msg_text = Widgets(self.__master).create_label("Uploaded Club Data:              none", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__club_msg_text, EMAILSTARTX - 50, EMAILENDY + 150)

    # Return the frame    
    def get_frame(self):
        return self.__master