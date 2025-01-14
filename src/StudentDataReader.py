import pandas as pd
from StudentRecord import StudentRecord

class StudentDataReader:
    """
    -----------------------
    * Parses an excel file and stores student data encapsulated in an object.
    * Creates and populates Array of student objects
    -----------------------
    """
    
    # Initialize empty array
    __student_records = []

    def __init__(self, student_file_path):
        # Read excel file containting student details
        student_df = pd.read_excel(student_file_path, engine="openpyxl")
        
        # Parse file to draw out all relevant data
        for index, row in student_df.iterrows():
            student_id = row['ID']
            student_name = row['Full Name']
            preferences = row['Club Preference Ranking']
            house = row['House']
            grade = row['Grade and Section']

            # populate array of Student objects
            student = StudentRecord(student_id, student_name, preferences, house, grade)
            self.__student_records.append(student) # array is pre-sorted by student ID


    def get_student_records(self):
        return self.__student_records

    # call binary search to query for a student object using student ID
    def get_student_record(self, student_id):
        result = self.recursive_binary_search(self.__student_records, student_id)
        return result

    # recursively search the array for a student record, and return the student object
    def recursive_binary_search(self, arr, element, low=0, high=None):
        if high is None:
            high = len(arr) - 1
        if low > high:
            return False

        mid = (low + high) // 2 
        if element == arr[mid].get_student_id():
            return arr[mid]
        if element < arr[mid].get_student_id():
            return self.recursive_binary_search(arr, element, low, mid-1)
        # element > arr[mid]
        return self.recursive_binary_search(arr, element, mid+1, high)


"""
    # iteratively search the array for a student record, and return the student object
    def get_student_record_iter(self, student_id):
        for stu_object in self.__student_records:
            if stu_object.get_student_id() == student_id:
                return stu_object
"""