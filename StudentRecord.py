from DataRecord import DataRecord


class StudentRecord(DataRecord):
    """
        -----------------------
        * Inherits from DataRecord
        * Defines a particular student
        * Student data encapsulated into getter and setter methods
        -----------------------
        """
    # The double underscore indicates private attributes
    __preferences = {}
    __house = ""
    __grade = ""

    def __init__(self, student_id, student_name, preferences, house, grade):
        # initialize inherited attributes
        super().__init__(student_id, student_name)
        # initialize new attributes
        self.__preferences = preferences
        self.__house = house
        self.__grade = grade

    def set_student_id(self, student_id):
        super().set_id(student_id)

    def get_student_id(self):
        return super().get_id()

    def set_student_name(self, student_name):
        super().set_name(student_name)

    def get_student_name(self):
        return super().get_name()

    def set_preferences(self, preferences):
        self.__preferences = preferences

    def get_preferences(self):
        return self.__preferences

    def set_house(self, house):
        self.__house = house

    def get_house(self):
        return self.__house

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def output_student(self):
        print(super().get_id(), super().get_name(), self.__house, self.__grade, self.__preferences)
