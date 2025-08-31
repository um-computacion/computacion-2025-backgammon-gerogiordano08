from core.game import Game
import unittest
class GameTests(unittest.TestCase):
    def test_prepare_board(self):
        g = Game('a', 'b')
        g.prepare_board()
        c = 'checker'
        q = 'quantity'
        col = g.get_board().get_columnas()
        self.assertTrue(
        col[0] == { c:'x', q:5} and
        col[11] == { c:'x', q:2} and
        col[17] == { c:'x', q:5} and
        col[19] == { c:'x', q:3} and

        col[4] == { c:'o', q:3} and
        col[6] == { c:'o', q:5} and
        col[12] == { c:'o', q:2} and
        col[23] == { c:'o', q:5}
        )