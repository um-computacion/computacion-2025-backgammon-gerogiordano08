"""Modulo Player.
Define la clase Player que representa a un jugador del juego."""
class Player:
    """La clase player define a cada uno de los dos jugadores
    junto con sus responsabilidades. Atributos: name, checker_type, bar_index"""
    def __init__(self, name:str, checker_type:int):
        self.__name__ = name
        self.__checker_type__ = checker_type
        self.__bar_index__ = 24 if checker_type == 1 else 25
    def get_name(self):
        """Devuelve el nombre del jugador (str)."""
        return self.__name__
    def get_checker_type(self):
        """Devuelve el tipo de ficha del jugador (int: 1 o 2)."""
        return self.__checker_type__
    def get_bar_index(self):
        """Devuelve el indice de la barra del jugador en 
        el atributo columnas de Board (int: 24 o 25)."""
        return self.__bar_index__
