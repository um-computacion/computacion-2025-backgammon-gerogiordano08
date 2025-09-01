from core.game import Game
import unittest
class GameTests(unittest.TestCase):
    def setUp(self):
        g = Game('a', 'b')
        g.prepare_board()
        c = 'checker'
        q = 'quantity'
        col = g.get_board().get_columnas()
        return g, c, q, col

    def test_prepare_board(self):
        """ Verifica que prepare_board() deja las fichas posicionadas correctamente para iniciar el juego. """
        g, c, q, col = self.setUp()

        g.prepare_board()

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
    def test_move_checker(self):
        """ Verifica que usar move_checker(fro, to) logra cambiar de posicion la ficha. """
        g, c, q, col = self.setUp()
        g.move_checker(0, 1)
        self.assertTrue(
            col[0] == { c: 'x', q: 4} and
            col[1] == { c: 'x', q: 1} 
        )
        g.move_checker(0, 11)
        self.assertTrue(
            col[0] == { c: 'x', q: 3} and
            col[1] == { c: 'x', q: 1} and
            col[11] == { c: 'x', q: 3}
        )
    def test_roll_dice(self):
        """ Compara los dados que salen con el método roll_dice() (de la clase Game) a el atributo __dice__. """
        g = self.setUp()[0]
        self.assertEqual(g.roll_dice(), g.get_dice().get_dice())
    def test_available_move(self):
        """ Verifica que available_move(fro, to) devuelve True para las condiciones suficientes y False para las condiciones insuficientes. """
        g, c, q, col = self.setUp()
        self.assertTrue(
            # de 'x' a 0
            g.available_move(0, 2) and 
            # de 'x' a 'x'
            g.available_move(0, 11)
        )
        self.assertFalse(
            # de 0 a 'x'
            g.available_move(3, 11) and
            # de 'x' a 'o'
            g.available_move(0, 4)
        )