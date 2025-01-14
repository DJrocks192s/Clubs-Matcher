class Processor:

    # Helper method
    @staticmethod  # static because it doesn't depend upon an instance of an object
    def get_capacity(club_id, club_record):
       return int(club_record[club_id].get_capacity())

    # Helper method
    @staticmethod  # as it doesn't depend upon an instance of an object
    def remap(first_map, club_record):
        second_map = {}
        for student_id,pref_list in first_map.items():
            each_student_map = {}
            sorted_each_student_map = {}
            for club_id,happiness_score in pref_list.items():
                club_capacity = Processor.get_capacity(club_id,club_record)
                for x in range(1, club_capacity + 1):
                    # create new club ID by concatanating old ID with a unique integer
                    new_club_id = club_id + "_" + str(x)
                    each_student_map[new_club_id] = happiness_score
            sorted_each_student_map = dict(sorted(each_student_map.items()))
            second_map[student_id] = sorted_each_student_map
        return second_map

    # Helper method
    @staticmethod
    def create_hungarian_map(student_record, club_record):
       """
        ------------------------
        * Input:
            * student_record is an Array of student objects
            * club_record is a HashMap of club IDs mapped to club objects
        * Construct a HashMap of Student ID mapped to another HashMap:
            * Second HashMap should map Club ID to the happiness score of the student being mapped to that club
            * This Club ID is created with the help of the has_club static method
        * Call remap method to create new club IDs based on the capacity of each club
        ------------------------
        """
       # initialize HashMap
       first_map = {}
       HOUSES = ["Pioneers", "Discoverers", "Explorers", "Voyagers"]

       for stu_record in student_record:  # iterating through each StudentRecord object
           stu_id = stu_record.get_student_id()  # unique student id and "key" in first map dict
           stu_club_pref_list = stu_record.get_preferences().split(";")[:-1]  # creating an array of club preference for a particular student
           # initialize inner HashMap
           club_pref_happiness = {}  # choice of clubs with happiness scores

           for rank, pref in enumerate(stu_club_pref_list): # iterating through array of club preference for a specific student
               happiness = len(stu_club_pref_list) - rank # calculating student happiness score for each club based on preference order
               # Create Unique Club ID
               is_nil = Processor.has_club(pref, club_record) # checking if the club is restricted only to a particular house
               if is_nil:
                    club_id = str(pref + "_NIL") # creating unique club ID
                    club_pref_happiness[club_id] = happiness # populating inner HashMap
               else: # if the club is restricted to a particular house
                    for h in HOUSES:  # iterating through all houses
                       club_id = str(pref + "_" + h)
                       if h != stu_record.get_house():  # if the student doesn't belong to the house
                           happiness = 0 # since they're inelgibile
                           club_pref_happiness[club_id] = happiness # populating inner HashMap
                       else: # the student is eligible, and belongs to the house
                           happiness = len(stu_club_pref_list) - rank # calculating student happiness score as before
                           club_pref_happiness[club_id] = happiness # populating inner HashMap
                       
           first_map[stu_id] = club_pref_happiness # populating outer HashMap (process repeated for each student ID)
       second_map = Processor.remap(first_map,club_record)
       return second_map

    @staticmethod
    def process(student_record, club_record):
       final_map = Processor.create_hungarian_map(student_record, club_record)
       return final_map

    # Helper method
    @staticmethod
    def has_club (pref_name, club_record):
        for x in club_record.values():
            if pref_name == x.get_club_name():
                return x.get_house() == "NIL"
