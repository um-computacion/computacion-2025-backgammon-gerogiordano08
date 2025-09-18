"""Modulo Dice. Contiene la definicion de la clase Dice"""
import random
class Dice:
    """La clase Dice representa los dos dados que se usan a traves del juego.
    Sus unicos atributos son die_1(int) y die_2(int)."""
    def __init__(self):
        self.__die_1__ = 0
        self.__die_2__ = 0
    def roll_dice(self):
        """Genera un numero aleatorio entre 1 y 6 a cada uno de los dados."""
        self.__die_1__ = random.randint(1, 6)
        self.__die_2__ = random.randint(1, 6)
    def clear_dice(self):
        """Le da el valor 0 a cada dado."""
        self.__die_1__ = 0
        self.__die_2__ = 0
    def get_dice_results(self):
        """Devuelve los resultados de los dados en una tupla.
        Si los dados tienen el mismo valor, devuelve cuatro variables. (tuple[int...])"""
        if self.__die_1__ == self.__die_2__:
            die = self.__die_1__
            return die, die, die, die
        return self.__die_1__, self.__die_2__
