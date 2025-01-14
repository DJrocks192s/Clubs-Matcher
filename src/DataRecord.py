class DataRecord:
    __record_id = 0
    __record_name = ""

    def __init__(self, record_id, name):
        self.__record_id = record_id
        self.__record_name = name

    def set_id(self, record_id):
        self.__record_id = record_id

    def get_id(self):
        return self.__record_id

    def set_name(self, record_name):
        self.__record_name = record_name

    def get_name(self):
        return self.__record_name
