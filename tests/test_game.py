from core.game import Game
import unittest
from unittest.mock import patch
class GameTests(unittest.TestCase):
    def setUp(self):
        self.game = Game('a', 'b', testing=True)
        self.game.prepare_board()
        self.c = 'checker'
        self.q = 'quantity'
        self.col = self.game.get_board().get_columnas()


    def test_prepare_board(self):
        """ Verifica que prepare_board() deja las fichas posicionadas correctamente para iniciar el juego. """


        self.game.prepare_board()
        c = self.c
        q = self.q
        self.assertTrue(
        self.col[11] == { c:'x', q:5} and
        self.col[0] == { c:'x', q:2} and
        self.col[18] == { c:'x', q:5} and
        self.col[16] == { c:'x', q:3} and

        self.col[5] == { c:'o', q:5} and
        self.col[7] == { c:'o', q:3} and
        self.col[12] == { c:'o', q:5} and
        self.col[23] == { c:'o', q:2}
        )
    def test_move_checker(self):
        """ Verifica que usar move_checker(fro, to) logra cambiar de posicion la ficha. """
        c = self.c
        q = self.q
        self.game.move_checker(11, 10)
        self.assertTrue(
            self.col[11] == { c: 'x', q: 4} and
            self.col[10] == { c: 'x', q: 1} 
        )
        self.game.move_checker(11, 0)
        self.assertTrue(
            self.col[11] == { c: 'x', q: 3} and
            self.col[10] == { c: 'x', q: 1} and
            self.col[0] == { c: 'x', q: 3}
        )
    def test_roll_dice(self):
        """ Compara los dados que salen con el método roll_dice() (de la clase Game) a el atributo __dice__. """
        self.game.roll_dice()
        for x in self.game.get_dice().get_dice_results():
            self.assertIn(x, (1, 2, 3, 4, 5, 6))
    
    # Tests del metodo turn

    @patch.object(Game, "turn_fichas_barra", side_effect=SystemExit)
    def test_turn_to_turn_fichas_barra(self, mock_tfb):
        """Verifica que si tiene fichas en la barra, el metodo turn acceda a turn_fichas_barra"""

        self.col[24][self.q] = 2
        with self.assertRaises(SystemExit):
            self.game.turn(self.game.get_player_1())
        mock_tfb.assert_called_once()

    @patch.object(Game, "turn_normal", side_effect=SystemExit)
    def test_turn_to_turn_normal(self, mock_tn):
        """Verifica que en un caso normal (no tiene fichas en la barra, no termina fichas),
        el metodo turn acceda a turn_normal"""

        with self.assertRaises(SystemExit):
            self.game.turn(self.game.get_player_1())
        mock_tn.assert_called_once()

    @patch.object(Game, "turn_finalizar_fichas", side_effect=SystemExit)
    def test_turn_to_turn_finalizar_fichas(self, mock_tff):
        """Verifica que si se deben sacar fichas del tablero,
        el metodo turn acceda a turn_finalizar_fichas"""
        for x in range(0, 17):
            if self.col[x][self.c] == 'x':
                self.col[x][self.q] = 0
        with self.assertRaises(SystemExit):
            self.game.turn(self.game.get_player_1())
        mock_tff.assert_called_once()
    
    # -----------------------------------

    # Tests del metodo turn_fichas_barra
    def test_turn_fichas_barra_dados_invalidos(self):
        """Verifica que si te tocan dados invalidos para sacar fichas de tu barra,
        devuelva True (successful_move) y None (used_die)"""
        self.col[24][self.q] = 1
        self.assertEqual(self.game.turn_fichas_barra(self.game.get_player_1(), (2, 2), 'x'), (True, None))

    @patch("builtins.input", return_value="3")
    def test_turn_fichas_barra_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""
        self.assertEqual(self.game.turn_fichas_barra(self.game.get_player_1(), (5, 6), 'x'), (False, None))
    
    @patch("builtins.input", return_value="3")
    def test_turn_fichas_barra_movimiento_correcto(self, mock_input):
        """Verifica que si se completa el movimiento,
        devuelva True (successful_move) y used_die (used_die)"""
        self.assertEqual(self.game.turn_fichas_barra(self.game.get_player_1(), (3, 6), 'x'), (True, 3))
    
    @patch("builtins.input", return_value="2")
    def test_turn_fichas_barra_movimiento_invalido(self, mock_input):
        """Verifica que si intenta hacer un movimiento invalido,
        devuelva False (successful_move) y None (used_die)"""
        self.assertEqual(self.game.turn_fichas_barra(self.game.get_player_1(), (3, 2), 'x'), (False, None))

    # -----------------------------------

    # Tests del metodo turn_normal

    @patch("builtins.input", return_value="2")
    def test_turn_normal_no_fichas(self, mock_input):
        """Verifica que si intentas mover fichas desde donde no tienes,
        devuelva False (successful_move) y None (used_die)"""
        
        self.assertEqual(self.game.turn_normal(self.game.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", side_effect=["1", "4"])
    def test_turn_normal_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""
        self.assertEqual(self.game.turn_normal(self.game.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", side_effect=["1", "2"])
    def test_turn_normal_movimiento_correcto(self, mock_input):
        """Verifica que si se completa el movimiento,
        devuelva True (successful_move) y used_die (used_die)"""
        self.assertEqual(self.game.turn_normal(self.game.get_player_1(), (3, 2), 'x'), (True, 2))
    
    @patch("builtins.input", side_effect=["1", "5"])
    def test_turn_normal_movimiento_invalido(self, mock_input):
        """Verifica que si intenta hacer un movimiento invalido,
        devuelva False (successful_move) y None (used_die)"""
        self.assertEqual(self.game.turn_normal(self.game.get_player_1(), (5, 2), 'x'), (False, None))

    # -----------------------------------

    # Tests del metodo turn_finalizar_fichas

    def test_turn_finalizar_fichas_dados_invalidos(self):
        """Verifica que si te tocan dados invalidos para sacar fichas del tablero,
        devuelva True (successful_move) y None (used_die)"""

        self.game.get_board().clear_board()
        self.col[21][self.q] = 2
        self.col[21][self.c] = 'x'
        self.assertEqual(self.game.turn_finalizar_fichas(self.game.get_player_1(), (2, 2), 'x'), (True, None))

    @patch("builtins.input", return_value="23")
    def test_turn_finalizar_fichas_no_fichas(self, mock_input):
        """Verifica que si intentas mover fichas desde donde no tienes,
        devuelva False (successful_move) y None (used_die)"""

        self.game.get_board().clear_board()
        self.col[22][self.q] = 2
        self.col[22][self.c] = 'x'

        self.assertEqual(self.game.turn_finalizar_fichas(self.game.get_player_1(), (3, 2), 'x'), (False, None))
    
    @patch("builtins.input", return_value="3")
    def test_turn_finalizar_fichas_dado_no_disponible(self, mock_input):
        """Verifica que si intentas elegir un dado no disponible,
        devuelva False (successful_move) y None (used_die)"""

        self.assertEqual(self.game.turn_finalizar_fichas(self.game.get_player_1(), (5, 6), 'x'), (False, None))
    
    # -----------------------------------

    # Tests para prepare_available_dice

    def test_prepare_available_dice_dados_mayores(self):
        """Verifica que si no quedan fichas en una casilla que requiere un dado mayor,
        se puede usar ese dado mayor para terminar una ficha que requiera un dado menor."""

        self.game.get_board().clear_board()
        self.col[19][self.q] = 1
        self.col[19][self.c] = 'x'
        self.assertEqual(self.game.prepare_available_dice(self.game.get_player_1(), [6, 5]), [6, 5])
    def test_prepare_available_dice_dados_menores(self):
        """Verifica que si quieres usar un dado menor para terminar una ficha, lo invalide."""

        self.game.get_board().clear_board()
        self.col[19][self.q] = 1
        self.col[19][self.c] = 'x'
        self.assertEqual(self.game.prepare_available_dice(self.game.get_player_1(), [6, 3]), [6])
    
    # -----------------------------------

    # Tests para finish_checker
    
    def test_finish_checker_sacar_ficha_cantidad_exacta(self):
        """Verifica que al usar un dado con la cantidad exacta necesaria para sacara el dado,
        devuelva True (successful_move) y used_die (used_die)"""
        self.assertEqual(self.game.finish_checker(22, self.game.get_player_1(), 2), (True, 2))
    def test_finish_checker_dados_mayores(self):
        """Verifica que si no quedan fichas en una casilla que requiere un dado mayor,
        se puede usar ese dado mayor para terminar una ficha que requiera un dado menor."""
        self.game.get_board().clear_board()
        self.col[19][self.q] = 1
        self.col[19][self.c] = 'x'
        self.assertEqual(self.game.finish_checker(19, self.game.get_player_1(), 6), (True, 6))

    def test_finish_checker_dice_dados_menores(self):
        """Verifica que si quieres usar un dado menor para terminar una ficha,
        devuelva False (successful_move) y None (used_die)"""
        self.game.get_board().clear_board()
        self.col[19][self.q] = 1
        self.col[19][self.c] = 'x'
        self.assertEqual(self.game.finish_checker(19, self.game.get_player_1(), 3), (False, None))
    
    # -----------------------------------

    def test_available_move(self):
        """ Verifica que available_move(fro, to) devuelve True para las condiciones suficientes y False para las condiciones insuficientes. """
        self.assertTrue(
            # de 'x' a 0
            self.game.available_move(0, 2) and 
            # de 'x' a 'x'
            self.game.available_move(0, 11)
        )
        self.assertFalse(
            # de 0 a 'x'
            self.game.available_move(3, 11) and
            # de 'x' a 'o'
            self.game.available_move(0, 4)
        )
    def test_can_finish_checkers_p1(self):
        """ Este test verifica que el método can_finish_checkers() devuelve True solo cuando se cumple la condicion. """
        for x in range(0, 18):
            self.col[x][self.q] = 0
        self.assertTrue(self.game.can_finish_checkers(self.game.__player_1__))
        self.game.prepare_board()
        self.assertFalse(self.game.can_finish_checkers(self.game.__player_1__))
    def test_can_finish_checkers_p2(self):
        """ Este test verifica que el método can_finish_checkers() devuelve True solo cuando se cumple la condicion. """
        for x in range(6, 24):
            self.col[x][self.q] = 0
        self.assertTrue(self.game.can_finish_checkers(self.game.__player_2__))
        self.game.prepare_board()
        self.assertFalse(self.game.can_finish_checkers(self.game.__player_2__))
    def test_win_condition(self):
        """ Este test verifica que el método win_condition() devuelve True solo cuando se cumple la condicion de victoria para el jugador señalado. """
        self.assertFalse(self.game.win_condition(self.game.get_player_1()))
        self.assertFalse(self.game.win_condition(self.game.get_player_2()))
        for x in range(0, 24):
            self.col[x][self.q] = 0
        self.assertTrue(self.game.win_condition(self.game.get_player_1()))
        self.assertTrue(self.game.win_condition(self.game.get_player_2()))
