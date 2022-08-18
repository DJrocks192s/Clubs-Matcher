from tkinter import *
from Widgets import Widgets
from tkinter import messagebox
from hashlib import sha256

# COLOURS

JET_BLACK = "#2e2e2e"
WHITE = "#d6d6d6"
CYAN = "#00bca9"
D_BROWN = "#91755e"
L_BROWN = "#c3aa92"

class Frame1:
    """
    -----------------------
    * Frame for login screen
    * Allows user to log in using username and password
    * Provides Register button to allow user to go to registration screen
    -----------------------
    """
    
    # Initialize the frame's dimensions and colour
    def __init__(self, master, w, h):

        self.__width = w
        self.__height = h
        self.__master = Frame(master, width=self.__width, height=self.__height, bg=JET_BLACK)

    # Helper method
    # Store passed registration screen frame object as an attribute to be called
    def set_register_cmd(self, frame_dir):
        self.__reg_direct = frame_dir
    
    # Helper method
    # Raise the frame for the registration screen
    def go_to_frame_2(self):
        self.__reg_direct.get_frame().tkraise()
    
    # Command for register button. Clear entry boxes and go to registration screen
    def register_button_cmd(self):
        self.__usernameentry.delete(0, END)
        self.__passwordentry.delete(0, END)
        self.go_to_frame_2()

    # Helper method
    # Store the passed home screen frame object as an attribute to be called
    def set_login_cmd(self, frame_dir):
        self.__login_direct = frame_dir
    
    # Helper method
    # Raise the frame for the home screen
    def go_to_frame_3(self):
        self.__login_direct.get_frame().tkraise()

    # Helper method
    @staticmethod
    def validate_login(username, password):
        """
        ------------------------
        * Validate passed username by checking if user file exists
        * Validate passed password by checking if its hash matches the hash stored in the user's text file
        * Show error message if user not found or if username and password don't match
        ------------------------
        """

        try: # check if the user exists
            f = open(username, 'r')
        except FileNotFoundError: # if user doesn't exist
            messagebox.showwarning("Username or password incorrect", "User not found or incorrect password entered.")
            return False
        else:
            # validating password
            details = f.read().splitlines()
            if sha256(password.encode()).hexdigest() != details[1]:
                messagebox.showwarning("Username or password incorrect", "User not found or incorrect password entered.")
                return False
            else:
                return True

    # Command for login button
    def login_button_cmd(self):
        """
        ------------------------
        * Get username and password from entry boxes
        * Call validate_login() method to determine if login was successful
        * If login successful then clear entry boxes and go to home screen
        ------------------------
        """

        self.__entered_username = self.__usernameentry.get()
        self.__entered_password = self.__passwordentry.get()
        is_valid_login = Frame1.validate_login(self.__entered_username, self.__entered_password)
        if is_valid_login:
            self.__usernameentry.delete(0, END)
            self.__passwordentry.delete(0, END)
            self.go_to_frame_3()


    # Set up all the widgets inside the Frame
    def setupFrame(self):
        """
        ------------------------
        * Create instances of the Widgets class to create Tkinter widgets in the frame.
        * Widgets created in this frame include:
            * Labels: Heading, Username, Password, No account?
            * Buttons: Login, Register
            * Entry Boxes: Username, Password
        ------------------------
        """

        X_CENTRE = self.__width//2
        Y_CENTRE = self.__height//2
        HEADING_START = X_CENTRE-248
        HEADING_END = X_CENTRE+248

        # Create heading label
        self.__heading = Widgets(self.__master).create_label("Clubs Matcher", CYAN, JET_BLACK, ("Times New Roman", 80))
        Widgets.place_Widgets(self.__heading, HEADING_START, 10)

        # Create username label
        self.__username_text = Widgets(self.__master).create_label("Username:", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__username_text, HEADING_START - 45, 205)

        # Create password label
        self.__password_text = Widgets(self.__master).create_label("Password:", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__password_text, HEADING_START - 45, 305)

        # Create username entry box
        self.__usernameentry = Widgets(self.__master).create_entry_box(25, ("Times New Roman", 30), "Enter your username", JET_BLACK)
        Widgets.place_Widgets(self.__usernameentry, HEADING_END - 345, 200)

        # Create password entry box
        self.__passwordentry = Widgets(self.__master).create_pwd_entry_box(25, ("Times New Roman", 30), "Enter your password", JET_BLACK)
        Widgets.place_Widgets(self.__passwordentry, HEADING_END - 345, 300)

        # Create login button
        self.__login_button = Widgets(self.__master).create_button("LOGIN", D_BROWN, ("Times New Roman", 25), 10, lambda: self.login_button_cmd())
        Widgets.place_Widgets(self.__login_button, HEADING_END - 130, 450)

        # Create register button
        self.__register_button = Widgets(self.__master).create_button("REGISTER", D_BROWN, ("Times New Roman", 25), 10, lambda: self.register_button_cmd())
        Widgets.place_Widgets(self.__register_button, HEADING_START - 45, 450)
    
    # Return the frame
    def get_frame(self):
        return self.__master