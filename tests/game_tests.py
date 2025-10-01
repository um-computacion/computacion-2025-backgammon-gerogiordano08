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
    
    # Tests del metodo turn

    @patch.object(Game, "turn_fichas_barra", side_effect=SystemExit)
    def test_turn_to_turn_fichas_barra(self, mock_tfb):
        """Verifica que si tiene fichas en la barra, el metodo turn acceda a turn_fichas_barra"""
        g, c, q, col = self.setUp()
        col[24][q] = 2
        with self.assertRaises(SystemExit):
            g.turn(g.get_player_1())
        mock_tfb.assert_called_once()

    @patch.object(Game, "turn_normal", side_effect=SystemExit)
    def test_turn_to_turn_normal(self, mock_tn):
        """Verifica que en un caso normal (no tiene fichas en la barra, no termina fichas),
        el metodo turn acceda a turn_normal"""
        g= self.setUp()[0]
        with self.assertRaises(SystemExit):
            g.turn(g.get_player_1())
        mock_tn.assert_called_once()

    @patch.object(Game, "turn_finalizar_fichas", side_effect=SystemExit)
    def test_turn_to_turn_finalizar_fichas(self, mock_tff):
        """Verifica que si se deben sacar fichas del tablero,
        el metodo turn acceda a turn_finalizar_fichas"""
        g, c, q, col = self.setUp()
        for x in range(0, 17):
            if col[x][c] == 'x':
                col[x][q] = 0
        with self.assertRaises(SystemExit):
            g.turn(g.get_player_1())
        mock_tff.assert_called_once()
    
    # -----------------------------------

    # Tests del metodo turn_fichas_barra
    def test_turn_fichas_barra_dados_invalidos(self):
        """Verifica que si te tocan dados invalidos para sacar fichas de tu barra,
        devuelva True (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        col[24][q] = 1
        self.assertEqual(g.turn_fichas_barra(g.get_player_1(), (2, 2), 'x'), (True, None))

    @patch("builtins.input", return_value="3")
    def test_turn_fichas_barra_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""
        g = self.setUp()[0]
        self.assertEqual(g.turn_fichas_barra(g.get_player_1(), (5, 6), 'x'), (False, None))
    
    @patch("builtins.input", return_value="3")
    def test_turn_fichas_barra_movimiento_correcto(self, mock_input):
        """Verifica que si se completa el movimiento,
        devuelva True (successful_move) y used_die (used_die)"""
        g = self.setUp()[0]
        self.assertEqual(g.turn_fichas_barra(g.get_player_1(), (3, 6), 'x'), (True, 3))
    
    @patch("builtins.input", return_value="2")
    def test_turn_fichas_barra_movimiento_invalido(self, mock_input):
        """Verifica que si intenta hacer un movimiento invalido,
        devuelva False (successful_move) y None (used_die)"""
        g = self.setUp()[0]
        self.assertEqual(g.turn_fichas_barra(g.get_player_1(), (3, 2), 'x'), (False, None))

    # -----------------------------------

    # Tests del metodo turn_normal

    @patch("builtins.input", return_value="2")
    def test_turn_normal_no_fichas(self, mock_input):
        """Verifica que si intentas mover fichas desde donde no tienes,
        devuelva False (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        
        self.assertEqual(g.turn_normal(g.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", side_effect=["1", "4"])
    def test_turn_normal_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()        
        self.assertEqual(g.turn_normal(g.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", side_effect=["1", "2"])
    def test_turn_normal_movimiento_correcto(self, mock_input):
        """Verifica que si se completa el movimiento,
        devuelva True (successful_move) y used_die (used_die)"""
        g, c, q, col = self.setUp()
        self.assertEqual(g.turn_normal(g.get_player_1(), (3, 2), 'x'), (True, 2))
    
    @patch("builtins.input", side_effect=["1", "5"])
    def test_turn_normal_movimiento_invalido(self, mock_input):
        """Verifica que si intenta hacer un movimiento invalido,
        devuelva False (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        self.assertEqual(g.turn_normal(g.get_player_1(), (5, 2), 'x'), (False, None))

    # -----------------------------------

    # Tests del metodo turn_finalizar_fichas

    def test_turn_finalizar_fichas_dados_invalidos(self):
        """Verifica que si te tocan dados invalidos para sacar fichas del tablero,
        devuelva True (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[21][q] = 2
        col[21][c] = 'x'
        self.assertEqual(g.turn_finalizar_fichas(g.get_player_1(), (2, 2), 'x'), (True, None))

    @patch("builtins.input", return_value="23")
    def test_turn_finalizar_fichas_no_fichas(self, mock_input):
        """Verifica que si intentas mover fichas desde donde no tienes,
        devuelva False (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[22][q] = 2
        col[22][c] = 'x'

        self.assertEqual(g.turn_finalizar_fichas(g.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", return_value="3")
    def test_turn_finalizar_fichas_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""
        g = self.setUp()[0]
        self.assertEqual(g.turn_finalizar_fichas(g.get_player_1(), (5, 6), 'x'), (False, None))
    
    # -----------------------------------

    # Tests para prepare_available_dice

    def test_prepare_available_dice_dados_mayores(self):
        """Verifica que si no quedan fichas en una casilla que requiere un dado mayor,
        se puede usar ese dado mayor para terminar una ficha que requiera un dado menor."""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[19][q] = 1
        col[19][c] = 'x'
        self.assertEqual(g.prepare_available_dice(g.get_player_1(), [6, 5]), [6, 5])
    def test_prepare_available_dice_dados_menores(self):
        """Verifica que si quieres usar un dado menor para terminar una ficha, lo invalide."""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[19][q] = 1
        col[19][c] = 'x'
        self.assertEqual(g.prepare_available_dice(g.get_player_1(), [6, 3]), [6])
    
    # -----------------------------------

    # Tests para finish_checker
    
    def test_finish_checker_sacar_ficha_cantidad_exacta(self):
        """Verifica que al usar un dado con la cantidad exacta necesaria para sacara el dado,
        devuelva True (successful_move) y used_die (used_die)"""
        g = self.setUp()[0]
        self.assertEqual(g.finish_checker(22, g.get_player_1(), 2), (True, 2))
    
    def test_finish_checker_dados_mayores(self):
        """Verifica que si no quedan fichas en una casilla que requiere un dado mayor,
        se puede usar ese dado mayor para terminar una ficha que requiera un dado menor."""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[19][q] = 1
        col[19][c] = 'x'
        self.assertEqual(g.finish_checker(19, g.get_player_1(), 6), (True, 6))

    def test_finish_checker_dice_dados_menores(self):
        """Verifica que si quieres usar un dado menor para terminar una ficha,
        devuelva False (successful_move) y None (used_die)"""
        g, c, q, col = self.setUp()
        g.get_board().clear_board()
        col[19][q] = 1
        col[19][c] = 'x'
        self.assertEqual(g.finish_checker(19, g.get_player_1(), 3), (False, None))
    
    # -----------------------------------

    def test_available_move(self):
        """ Verifica que available_move(fro, to) devuelve True para las condiciones suficientes y False para las condiciones insuficientes. """
        g = self.setUp()[0]
        
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
    def test_can_finish_checkers_p1(self):
        """ Este test verifica que el método can_finish_checkers() devuelve True solo cuando se cumple la condicion. """

        g, c, q, col = self.setUp()
        for x in range(0, 18):
            col[x][q] = 0
        self.assertTrue(g.can_finish_checkers(g.__player_1__))
        g.prepare_board()
        self.assertFalse(g.can_finish_checkers(g.__player_1__))
    def test_can_finish_checkers_p2(self):
        """ Este test verifica que el método can_finish_checkers() devuelve True solo cuando se cumple la condicion. """
        g, c, q, col = self.setUp()
        for x in range(6, 24):
            col[x][q] = 0
        self.assertTrue(g.can_finish_checkers(g.__player_2__))
        g.prepare_board()
        self.assertFalse(g.can_finish_checkers(g.__player_2__))
    def test_win_condition(self):
        """ Este test verifica que el método win_condition() devuelve True solo cuando se cumple la condicion de victoria para el jugador señalado. """
        g, c, q, col = self.setUp()
        self.assertFalse(g.win_condition(g.get_player_1()))
        self.assertFalse(g.win_condition(g.get_player_2()))
        for x in range(0, 24):
            col[x][q] = 0
        self.assertTrue(g.win_condition(g.get_player_1()))
        self.assertTrue(g.win_condition(g.get_player_2()))
