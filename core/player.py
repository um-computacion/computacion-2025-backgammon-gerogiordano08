class Player:
    def __init__(self, name:str, checker_type:int):
        self.__name__ = name
        self.__checker_type__ = checker_type
        self.__bar_index__ = 24 if checker_type == 1 else 25
    def get_name(self):
        return self.__name__
    def get_checker_type(self):
        return self.__checker_type__
    def get_bar_index(self):
        return self.__bar_index__
    