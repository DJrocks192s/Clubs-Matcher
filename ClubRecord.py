from DataRecord import DataRecord


class ClubRecord(DataRecord):
    __capacity = 0
    __classroom = ""
    __house = ""

    def __init__(self, club_id, club_name, capacity, classroom, house="NIL"):
        super().__init__(club_id, club_name)
        self.__capacity = capacity
        self.__classroom = classroom
        self.__house = house

    def set_club_id(self, club_id):
        super().set_id(club_id)

    def get_club_id(self):
        return super().get_id()

    def set_club_name(self, club_name):
        super().set_name(club_name)

    def get_club_name(self):
        return super().get_name()

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def set_classroom(self, classroom):
        self.__classroom = classroom

    def get_classroom(self):
        return self.__classroom

    def set_house(self, house):
        self.__house = house

    def get_house(self):
        return self.__house

    def output_club(self):
        print(super().get_id(), super().get_name(), self.__capacity, self.__classroom, self.__house)
