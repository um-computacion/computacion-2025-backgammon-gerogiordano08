"""Modulo RedisStore. Define la clase RedisStore."""
import json
import redis
from redis import Redis
class RedisStore:
    """Esta clase es responsable de manejar la base de datos de redis."""
    def __init__(self) -> None:
        self.__r__: Redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
    def save_list_to_json(self, nombre_lista, lista):
        """Guarda una lista de python como string en redis."""
        self.__r__.set(nombre_lista, json.dumps(lista))
    def load_list(self, nombre_lista)-> list:
        """Carga una lista que esta guardada como string en redis. La devuelve como lista python."""
        raw = self.__r__.get(nombre_lista)
        if raw is None:
            return []
        if isinstance(raw, str):
            return json.loads(raw)
        return []
    def save_game(self, game):
        """Guarda el juego en la base de datos de redis."""
        self.save_list_to_json('columnas', game.get_board().get_columnas())
        self.set_value('actual_player_turn', game.get_actual_player_turn())
        self.set_value('name1', game.get_player_1().get_name())
        self.set_value('name2', game.get_player_2().get_name())
    def get_value(self, key):
        """Devuelve un valor guardado en redis. """
        return str(self.__r__.get(key))
    def set_value(self, key, value):
        """Guarda un par key value en redis."""
        self.__r__.set(key, value)
    def delete_db(self):
        """Borra los datos guardados en redis"""
        self.__r__.flushdb()
