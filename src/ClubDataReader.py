import pandas as pd
from ClubRecord import ClubRecord


class ClubDataReader:
    """
    -----------------------
    * Parses an excel file and stores club data encapsulated in an object.
    * Creates and populates HashMap of club_id mapped to club object
    -----------------------
    """

    # Initialize empty hash map
    __club_records = {}

    def __init__(self, club_file_path):
        # Read excel file containting club details
        club_df = pd.read_excel(club_file_path, engine="openpyxl")

        # Parse file to draw out all relevant data
        for index, row in club_df.iterrows():
            club_name = row["Club Name"]
            capacity = row["Capacity"]
            classroom = str(row["Classroom"])
            house = row["House"]
            # create unique club_id
            club_id = str(club_name + "_" + house)  # always unique

            # map club_id to club object to populate HashMap
            club = ClubRecord(club_id, club_name, capacity, classroom, house)
            self.__club_records[club_id] = club

    # returns HashMap of club_id mapped to club object
    def get_club_records(self):
        return self.__club_records

    def get_club_record(self, club_id): # query club object using its club_id
        return self.__club_records[club_id]
