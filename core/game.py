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
        self.__board__.clear_board()

        self.__board__.put_checker(1, self.__checker_1__.get_symbol(), 5)
        self.__board__.put_checker(12, self.__checker_1__.get_symbol(), 2)
        self.__board__.put_checker(18, self.__checker_1__.get_symbol(), 5)
        self.__board__.put_checker(20, self.__checker_1__.get_symbol(), 3)

        self.__board__.put_checker(5, self.__checker_2__.get_symbol(), 3)
        self.__board__.put_checker(7, self.__checker_2__.get_symbol(), 5)
        self.__board__.put_checker(13, self.__checker_2__.get_symbol(), 2)
        self.__board__.put_checker(24, self.__checker_2__.get_symbol(), 5)
    def get_board(self):
        return self.__board__

