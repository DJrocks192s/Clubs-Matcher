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

# Special characters for password verification

SPECIAL_CH = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}','[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']


class Frame2:
    """
    -----------------------
    * Frame for register screen
    * Allows user to create an account using username and password
    * Carries out validation and verification checks
    * Stores created user information in a text file. Password is hashed before being stored.
    -----------------------
    """

    # Initialize the frame's dimensions and colour
    def __init__(self, master, w, h):
        
        self.__width = w
        self.__height = h
        self.__master = Frame(master, width=self.__width, height=self.__height, bg=JET_BLACK)
    
    # Helper method
    # Store passed login screen frame object as an attribute to be called
    def set_back_cmd(self, frame_dir):
        self.__back_direct = frame_dir
    
    # Command for back button. Raise the frame for the login screen
    def go_back(self):
        self.__back_direct.get_frame().tkraise()
    
    # Helper method
    # Store passed login screen frame object as an attribute to be called
    def set_register_cmd(self, frame_dir):
        self.__reg_direct = frame_dir
    
    # Helper method
    # Raise the frame for the login screen
    def go_to_frame_1(self):
        self.__reg_direct.get_frame().tkraise()

    # Helper method
    @staticmethod
    def validate_username(username):
        """
        ------------------------
        * Validate username – presence check
        * Check if user file of the same name already exists
        ------------------------
        """
        # presence check
        if len(username) == 0:
            messagebox.showwarning("Unfilled field(s)", "Please enter a valid username")
            return False
        # check whether account already exists
        try:
            f = open(username, 'r') # checking if file of given username already exists
        except FileNotFoundError: # if no file exists, which indicates a new user
            return True
        else: # user already exists. Prompts to log in.
            messagebox.showwarning("User already exists", "The account already exists. Try logging in.")
            f.close()
            return False
    
    # Helper method
    @staticmethod
    def validate_password(password, confirm_password):
        """
        ------------------------
        * Validate password – presence check, length check, type check
        * Verify password – double entry
        ------------------------
        """
        # presence check
        if len(password) == 0:
            messagebox.showwarning("Unfilled field(s)", "Please enter a valid password")
            return False
        # password validation (type and length check)
        elif any((
                not any(ch in SPECIAL_CH for ch in password), # to be at least 1 special character
                not any(ch.isupper() for ch in password), # to be at least 1 uppercase character
                not any(ch.islower() for ch in password), # to be at least 1 lowercase character
                not any(ch.isdigit() for ch in password), # to be at least 1 number
                len(password) < 8 # to be at least 8 characters in length
                )):
                messagebox.showerror("Invalid Password", "Your password must be at least 8 characters with at least one uppercase, one lowercase, one number, and one special character.")
                return False
        # password verification using double entry
        elif password != confirm_password:
            messagebox.showwarning("Passwords must match", "Please make sure both passwords match")
            return False
        # reaches here if only if all details are correct
        else:
            return True

    # Command for register button
    def register_button_cmd(self):
        """
        ------------------------
        * Get username password, and confirm password from entry boxes
        * Call validate_username() validate_password() methods to validate fields
        * If fields are valid, then create and store user details in text file
        * Clear entry boxes and go to login screen
        ------------------------
        """

        self.__username = self.__username_entry.get()
        self.__password = self.__passwordentry.get()
        self.__confirm_password = self.__confirm_password_entry.get()

        # validating and verifying the fields
        is_valid_username = Frame2.validate_username(self.__username)
        if is_valid_username:
            is_valid_pwd = Frame2.validate_password(self.__password, self.__confirm_password)
            if is_valid_pwd:
                f = open(self.__username, 'w') # creating a file to store the user's details
                # writing the user details onto the file
                f.write(self.__username + "\n")
                # hashing the password using SHA256 before writing it onto the file
                self.__hashed_password = sha256(self.__password.encode()).hexdigest()
                f.write(self.__hashed_password)
                f.close()
                self.__username_entry.delete(0, END)
                self.__passwordentry.delete(0, END)
                messagebox.showinfo("User created successfully", f"An account with name \"{self.__username}\" has been created successfully. You may now login using this account.")
                self.go_to_frame_1()

    # Set up all the widgets inside the Frame
    def setupFrame(self):
        """
        ------------------------
        * Create instances of the Widgets class to create Tkinter widgets in the frame.
        * Widgets created in this frame include:
            * Labels: Heading, Username, Password, Confirm password
            * Buttons: Back, Register
            * Entry Boxes: Username, Password, Confirm password
        ------------------------
        """

        X_CENTRE = self.__width//2
        Y_CENTRE = self.__height//2
        EMAILSTARTX = X_CENTRE - 450
        EMAILENDY = Y_CENTRE - 100

        # Create back button
        self.__back_button = Widgets(self.__master).create_button("Back", D_BROWN, ("Times New Roman", 30), 4, lambda: self.go_back())
        Widgets.place_Widgets(self.__back_button, 0, 0)

        # Create heading label
        self.__heading = Widgets(self.__master).create_label("Register New User", CYAN, JET_BLACK, ("Times New Roman", 80))
        Widgets.place_Widgets(self.__heading, 200, 100)

        # Create username label
        self.__username_text = Widgets(self.__master).create_label("Username:", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__username_text, EMAILSTARTX, EMAILENDY - 30)

        # Create password label
        self.__password_text = Widgets(self.__master).create_label("Password:", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__password_text, EMAILSTARTX, EMAILENDY + 75)

        # Create confirm password label
        self.__confirm_password_text = Widgets(self.__master).create_label("Confirm Password:", WHITE, JET_BLACK, ("Times New Roman", 30))
        Widgets.place_Widgets(self.__confirm_password_text, EMAILSTARTX - 100, EMAILENDY + 175)

        # Create username entry box
        self.__username_entry = Widgets(self.__master).create_entry_box(25, ("Times New Roman", 30), "Enter a valid email", JET_BLACK)
        Widgets.place_Widgets(self.__username_entry, EMAILSTARTX + 200, EMAILENDY - 30)
        
        # Create password entry box
        self.__passwordentry = Widgets(self.__master).create_pwd_entry_box(25, ("Times New Roman", 30), "8-12 characters", JET_BLACK)
        Widgets.place_Widgets(self.__passwordentry, EMAILSTARTX + 200, EMAILENDY + 75)

        # Create confirm password entry box
        self.__confirm_password_entry = Widgets(self.__master).create_confirm_pwd_entry_box(25, ("Times New Roman", 30), "", JET_BLACK)
        Widgets.place_Widgets(self.__confirm_password_entry, EMAILSTARTX + 200, EMAILENDY + 175)

        # Create register button
        self.__register_button = Widgets(self.__master).create_button("REGISTER", D_BROWN, ("Times New Roman", 25), 10, lambda: self.register_button_cmd())
        Widgets.place_Widgets(self.__register_button, 690, 630)
    
    # Return the frame
    def get_frame(self):
        return self.__master