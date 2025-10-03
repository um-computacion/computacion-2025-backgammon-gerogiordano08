"""Modulo Player.
Define la clase Player que representa a un jugador del juego."""
from core.redis_store import RedisStore
class Player:
    """La clase player define a cada uno de los dos jugadores
    junto con sus responsabilidades. Atributos: name, checker_type, bar_index"""
    def __init__(self, name:str, checker_type:int, testing:bool = False):
        self.__redis_store__ = RedisStore()
        self.__checker_type__ = checker_type
        if not self.__redis_store__.get_value(f'name{checker_type}') or testing:
            self.__name__ = name
        else:
            self.__name__ = self.__redis_store__.get_value(f'name{checker_type}')
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
    def get_bar_opp_index(self):
        """Devuelve el indice de la barra del jugador opuesto en
        el atributo columnas de Board (int: 24 o 25)."""
        if self.__bar_index__ == 24:
            return 25
        return 24
    def get_bar_practical_index(self):
        """Devuelve el indice que se debe usar al
        intentar mover fichas en el tablero desde la barra."""
        if self.__bar_index__ == 24:
            return 5
        return 18
    def get_bar_opp_practical_index(self):
        """Devuelve el indice que se debe usar al
        intentar mover fichas en el tablero desde la
        barra del jugador opuesto."""
        if self.__bar_index__ == 24:
            return 18
        return 5
