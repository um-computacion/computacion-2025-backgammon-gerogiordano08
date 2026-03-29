import unittest
from core.dice import Dice
class DiceTests(unittest.TestCase):
    def test_roll_dice(self):
        """ Este test verifica que al usar roll_dice() para tirar los dados, ambos numeros esten en el rango [1, 6]. """
        dice = Dice()
        dice.roll_dice()
        self.assertTrue(
            all( 0 < x < 7 for x in dice.get_dice_results())
        )
    def test_clear_dice(self):
        """ Este test verifica que, si usamos roll_dice() para que los dados den un numero natural y luego usamos clear_dice(), el valor de ambos dados vuelve a 0. """
        dice = Dice()
        dice.roll_dice()
        self.assertTrue(
            all( 0 < x < 7 for x in dice.get_dice_results())
        )
        dice.clear_dice()
        self.assertEqual(dice.get_dice_results(), (0, 0, 0, 0))