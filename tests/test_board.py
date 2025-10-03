from core.board import Board
import unittest
from core.redis_store import RedisStore
from unittest.mock import patch, call
class BoardTests(unittest.TestCase):
    def setUp(self):
        self.tab = Board()

    @patch('builtins.print')
    def test_show_board(self, mock_print):
        """ Este test prepara el tablero con setUp(), llama al método show_board(), y verifica que imprima el tablero de manera correcta en la consola"""
        self.tab.show_board()
        esperadas = [call("                          TABLERO DE BACKGAMMON"),
                    call("           13  14  15  16  17  18   |BAR|   19  20  21  22  23  24"), 
                    call("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+"), 
                    call("Fila 1   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 2   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 3   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 4   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 5   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 6   | v | v | v | v | v | v |  |   |  | v | v | v | v | v | v |"),
                    call("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+"),
                    call("Fila 6   | ^ | ^ | ^ | ^ | ^ | ^ |  |   |  | ^ | ^ | ^ | ^ | ^ | ^ |"),
                    call("Fila 5   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 4   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 3   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 2   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("Fila 1   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |"),
                    call("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+"),
                    call("          12  11  10   9   8   7    |BAR|    6   5   4   3   2   1"),
                    call("- La columna central es la **BAR** (barra)."),
                    call("- Si un punto tiene más de 5 fichas, usa (6), (7), etc.")
                    ]
        
        mock_print.assert_has_calls(esperadas, any_order= True)
    def test_checker(self):
        """ Este test prepara el tablero, agrega la ficha x a la columna 5, suma una ficha en esa columna y luego verifica que el método checker(column, level) devuelve correctamente la ficha x en los niveles 1 y 2 y devuelve ' ' en el nivel 3 """
        self.tab.put_checker(4, 'x')
        self.tab.add_checker(4)
        self.assertEqual(self.tab.checker(4, 1), 'x')
        self.assertEqual(self.tab.checker(4, 2), 'x')
        self.assertEqual(self.tab.checker(4, 3), ' ')
    def test_add_checker(self):
        """ Este test prepara el tablero, agrega la ficha x en la columna 5,
             le suma una ficha a la cantidad con el método add_checker(column) 
             y verifica que la cantidad de fichas en la columna 5 sea igual a 2"""
        self.tab.put_checker(4, 'x')
        self.tab.add_checker(4)
        self.assertEqual(self.tab.get_columnas()[4]['quantity'], 2)
    def test_remove_checker(self):
        """Este test prepara el tablero, agrega la ficha x en la columna 5, le suma una ficha a la cantidad con el método add_checker(column), le resta una ficha con remove_checker(column) y verifica que la cantidad de fichas en la columna 5 sea igual a 1"""
        self.tab.put_checker(4, 'x')
        self.tab.add_checker(4)
        self.tab.remove_checker(4)
        self.assertEqual(self.tab.get_columnas()[4]['quantity'], 1)
    def test_put_checker(self):
        """ Este test prepara el tablero, agrega distintas fichas en tres columnas distintas del tablero con put_checker(column, checker) y luego verifica que en __columnas__, en dichas columnas especificas se encuentren esas fichas, y que en una columna no elegida la ficha sea ' '."""
        self.tab.put_checker(4, 'x')
        self.tab.put_checker(6, 'o')
        self.tab.put_checker(21, 'y')
        self.assertEqual(self.tab.get_columnas()[4]['checker'], 'x')
        self.assertEqual(self.tab.get_columnas()[6]['checker'], 'o')
        self.assertEqual(self.tab.get_columnas()[21]['checker'], 'y')
        self.assertEqual(self.tab.get_columnas()[10]['checker'], '')
    def test_clear_board(self):
        """ Este test verifica que al usar clear_board() el tablero queda limpio. """
        self.tab.put_checker(1, 'x')
        self.assertFalse(
        all(
        column['quantity'] == 0
        for column in self.tab.get_columnas()
        ))
        self.tab.clear_board()
        self.assertTrue(
        all(
        column['quantity'] == 0
        for column in self.tab.get_columnas()
        ))
if __name__ == '__main__':
    unittest.main()