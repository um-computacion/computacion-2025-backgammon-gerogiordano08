class Player:
    def __init__(self, name:str, checker_type:int):
        self.__name__ = name
        self.__checker_type__ = checker_type
    def get_name(self):
        return self.__name__
    def get_checker_type(self):
        return self.__checker_type__
    