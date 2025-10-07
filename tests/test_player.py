from core.player import Player
import unittest
class PlayerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.p1 = Player('a', 1, testing=True)
        self.p2 = Player('a', 2, testing=True)
    def test_get_opp_bar_index(self):
        self.assertEqual(self.p1.get_bar_opp_index(), 25)
        self.assertEqual(self.p2.get_bar_opp_index(), 24)
    def test_get_bar_practical_index(self):
        """Verifica que la funcion devuelva el indice practico de la barra correcto."""
        self.assertEqual(self.p1.get_bar_practical_index(), -1)
        self.assertEqual(self.p2.get_bar_practical_index(), 24)
    def test_get_opp_bar_practical_index(self):
        """Verifica que la funcion devuelva el indice practico de la barra del oponente correcto."""
        self.assertEqual(self.p1.get_bar_opp_practical_index(), 24)
        self.assertEqual(self.p2.get_bar_opp_practical_index(), -1)
