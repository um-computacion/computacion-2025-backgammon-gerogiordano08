from core.player import Player
import unittest
from unittest.mock import Mock, patch
class PlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Player('a', 1)
        self.p2 = Player('a', 2)
    def test_get_opp_bar_index(self):
        self.assertEqual(self.p1.get_bar_opp_index(), 25)
        self.assertEqual(self.p2.get_bar_opp_index(), 24)
    def test_get_bar_practical_index(self):
        """Verifica que la funcion devuelva el indice practico de la barra correcto."""
        self.assertEqual(self.p1.get_bar_practical_index(), 5)
        self.assertEqual(self.p2.get_bar_practical_index(), 18)
    def test_get_opp_bar_practical_index(self):
        """Verifica que la funcion devuelva el indice practico de la barra del oponente correcto."""
        self.assertEqual(self.p1.get_bar_opp_practical_index(), 18)
        self.assertEqual(self.p2.get_bar_opp_practical_index(), 5)
