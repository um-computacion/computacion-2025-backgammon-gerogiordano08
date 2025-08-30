class Checker:
    def __init__(self, type: int):
        self.__type__ = type
        self.__symbol_1__ = 'x'
        self.__symbol_2__ = 'o'
    def get_symbol(self):
        if self.__type__ == 1:
            return self.__symbol_1__
        elif self.__type__ == 2:
            return self.__symbol_2__
        