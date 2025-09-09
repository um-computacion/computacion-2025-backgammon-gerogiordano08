import random
class Dice:
    def __init__(self):
        self.__die_1__ = 0
        self.__die_2__ = 0
    def roll_dice(self):
        self.__die_1__ = random.randint(1, 6)
        self.__die_2__ = random.randint(1, 6)
    def clear_dice(self):
        self.__die_1__ = 0
        self.__die_2__ = 0
    def get_dice_results(self):
        if self.__die_1__ == self.__die_2__:
            die = self.__die_1__
            return die, die, die, die
        else:
            return self.__die_1__, self.__die_2__
