import pandas as pd


class OutputProcessor:

    def __init__(self, student_list, club_list, final_list):
        self.__student_list = student_list
        self.__club_list = club_list
        self.__final_list = final_list

    def strip_number(self, string):
        x = string.split("_")
        y = f"{x[0]}_{x[1]}"
        return y

    def process(self):
        my_columns = ["Student Name","Grade and Section", "House", "Club Assigned", "Classroom"]
        df = pd.DataFrame(columns=my_columns)
        for pair in self.__final_list:
            student_id = pair[0]
            club_id = self.strip_number(pair[1])
            student_record = self.__student_list.get_student_record(student_id)
            club_record = self.__club_list.get_club_record(club_id)
            df.loc[len(df)] = [student_record.get_student_name(), student_record.get_grade(), student_record.get_house(), club_record.get_club_name(), club_record.get_classroom()]
        
        return df


