from core.player import Player
from core.checker import Checker
from core.dice import Dice
from core.board import Board

class Game:
    def __init__(self, p1_name, p2_name):
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__checker_1__ = Checker(1)
        self.__checker_2__ = Checker(2)
        self.__player_1__ = Player(p1_name, 1)
        self.__player_2__ = Player(p2_name, 2)
    def prepare_board(self):
        """ Este método deja el tablero listo para el juego, dejando las 30 fichas en sus lugares correspondientes. """
        self.__board__.clear_board()
        put = self.__board__.put_checker
        c1 = self.__checker_1__.get_symbol()
        c2 = self.__checker_2__.get_symbol()
        put(1, c1, 5)
        put(12, c1, 2)
        put(18, c1, 5)
        put(20, c1, 3)

        put(5, c2, 3)
        put(7, c2, 5)
        put(13, c2, 2)
        put(24, c2, 5)
    def move_checker(self, fro, to):
        """ Este método saca una ficha de una columna fro y la suma en la columna to"""
        self.__board__.remove_checker(fro + 1)
        columnas = self.__board__.get_columnas()
        if columnas[to]['quantity'] == 0:

            self.__board__.put_checker(to + 1, columnas[fro]['checker'])
        else:
            self.__board__.add_checker(to + 1)
    def roll_dice(self):
        self.__dice__.roll_dice()
        return self.__dice__.get_dice()
    def available_move(self, fro, to):
        columnas = self.__board__.get_columnas()
        if columnas[fro]['quantity'] > 0:
            if columnas[to]['quantity'] == 0 or columnas[fro]['checker'] == columnas[to]['checker']:
                return True
            else: 
                return False
        else:
            return False


    def get_board(self):
        return self.__board__
    def get_dice(self):
        return self.__dice__

