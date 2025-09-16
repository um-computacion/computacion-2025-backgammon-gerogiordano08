from core.game import Game
import unittest
from unittest.mock import Mock, patch
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
        col[11] == { c:'x', q:5} and
        col[0] == { c:'x', q:2} and
        col[18] == { c:'x', q:5} and
        col[16] == { c:'x', q:3} and

        col[5] == { c:'o', q:5} and
        col[7] == { c:'o', q:3} and
        col[12] == { c:'o', q:5} and
        col[23] == { c:'o', q:2}
        )
    def test_move_checker(self):
        """ Verifica que usar move_checker(fro, to) logra cambiar de posicion la ficha. """
        g, c, q, col = self.setUp()
        g.move_checker(11, 10)
        self.assertTrue(
            col[11] == { c: 'x', q: 4} and
            col[10] == { c: 'x', q: 1} 
        )
        g.move_checker(11, 0)
        self.assertTrue(
            col[11] == { c: 'x', q: 3} and
            col[10] == { c: 'x', q: 1} and
            col[0] == { c: 'x', q: 3}
        )
    def test_roll_dice(self):
        """ Compara los dados que salen con el método roll_dice() (de la clase Game) a el atributo __dice__. """
        g = self.setUp()[0]
        g.roll_dice()
        for x in g.get_dice().get_dice_results():
            self.assertIn(x, (1, 2, 3, 4, 5, 6))
    def test_available_move(self):
        """ Verifica que available_move(fro, to) devuelve True para las condiciones suficientes y False para las condiciones insuficientes. """
        g = self.setUp()[0]
        
        self.assertTrue(
            # de 'x' a 0
            g.available_move(0, 2, g.__player_1__) and 
            # de 'x' a 'x'
            g.available_move(0, 11, g.__player_1__)
        )
        self.assertFalse(
            # de 0 a 'x'
            g.available_move(3, 11, g.__player_1__) and
            # de 'x' a 'o'
            g.available_move(0, 4, g.__player_1__)
        )
    def test_can_finish_checkers_p1(self):
        """ Este test verifica que el método can_finish_checkers_p1() devuelve True solo cuando se cumple la condicion. """

        g, c, q, col = self.setUp()
        for x in range(0, 18):
            col[x][q] = 0
        self.assertTrue(g.can_finish_checkers_p1())
        g.prepare_board()
        self.assertFalse(g.can_finish_checkers_p1())
    def test_can_finish_checkers_p2(self):
        """ Este test verifica que el método can_finish_checkers_p2() devuelve True solo cuando se cumple la condicion. """
        g, c, q, col = self.setUp()
        for x in range(6, 24):
            col[x][q] = 0
        self.assertTrue(g.can_finish_checkers_p2())
        g.prepare_board()
        self.assertFalse(g.can_finish_checkers_p2())
    def test_win_condition(self):
        """ Este test verifica que el método win_condition() devuelve True solo cuando se cumple la condicion de victoria para el jugador señalado. """
        g, c, q, col = self.setUp()
        self.assertFalse(g.win_condition(g.get_player_1()))
        self.assertFalse(g.win_condition(g.get_player_2()))
        for x in range(0, 24):
            col[x][q] = 0
        self.assertTrue(g.win_condition(g.get_player_1()))
        self.assertTrue(g.win_condition(g.get_player_2()))
    def test_check_bar(self):
        """ El test verifica que check_bar(player) devuelve True o False correctamente de acuerdo al caso. """
        g, c, q, col = self.setUp()
        self.assertFalse(g.check_bar(g.get_player_1()))
        self.assertFalse(g.check_bar(g.get_player_2()))
        g.add_checker(24)
        self.assertTrue(g.check_bar(g.get_player_1()))
        self.assertFalse(g.check_bar(g.get_player_2()))
        g.add_checker(25)
        self.assertTrue(g.check_bar(g.get_player_1()))
        self.assertTrue(g.check_bar(g.get_player_2()))
    def test_finish_checker(self):
        """ Verifica que la funcion finish_checker(col, player) devuelve True cuando exitosamente termina una ficha. """
        g, c, q, col = self.setUp()
        self.assertFalse(g.finish_checker(18, g.__player_1__))
        for x in range(0, 18):
            col[x][q] = 0
        self.assertTrue(g.finish_checker(18, g.__player_1__))
