"""Modulo checker.
Contiene la definicion de la clase Checker"""
class Checker:
    """La clase Player define a cada una de los dos tipos de fichas que se usan en el juego.
    Contiene los atributos type(int), symbol_1(str='x'), symbol_2(str='o')"""
    def __init__(self, c_type: int):
        self.__type__ = c_type
        self.__symbol_1__ = 'x'
        self.__symbol_2__ = 'o'
    def get_symbol(self):
        """Devuelve el simbolo (str)."""
        if self.__type__ == 1:
            return self.__symbol_1__
        if self.__type__ == 2:
            return self.__symbol_2__
        return ' '
    def get_c_type(self):
        """Devuelve el tipo de ficha (int:1 o 2)."""
        return self.__type__
