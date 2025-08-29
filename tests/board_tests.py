from core.board import Board
import unittest
from unittest.mock import patch, call
class BoardTests(unittest.TestCase):
    def setUp(self):
        tab = Board()
        for x in range(0,24):
            tab.put_checker(x, ' ')
        return tab
    @patch('builtins.print')
    def test_show_board(self, mock_print):
        """ Este test prepara el tablero con setUp(), llama al método show_board(), y verifica que imprima el tablero de manera correcta en la consola"""
        tab = self.setUp()
        tab.show_board()
        esperadas = [call("                          TABLERO DE BACKGAMMON"),
                    call("           24  23  22  21  20  19   |BAR|   18  17  16  15  14  13"), 
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
                    call("           1   2   3   4   5   6    |BAR|    7   8   9  10  11  12"),
                    call("- La columna central es la **BAR** (barra)."),
                    call("- Si un punto tiene más de 5 fichas, usa (6), (7), etc.")
                    ]
        
        mock_print.assert_has_calls(esperadas, any_order= True)
    def test_checker(self):
        """ Este test prepara el tablero, agrega la ficha x a la columna 5, suma una ficha en esa columna y luego verifica que el método checker(column, level) devuelve correctamente la ficha x en los niveles 1 y 2 y devuelve ' ' en el nivel 3 """
        tab = self.setUp()
        tab.put_checker(5, 'x')
        tab.add_checker(5)
        self.assertEqual(tab.checker(4, 1), 'x')
        self.assertEqual(tab.checker(4, 2), 'x')
        self.assertEqual(tab.checker(4, 3), ' ')
    def test_add_checker(self):
        """ Este test prepara el tablero, agrega la ficha x en la columna 5,
             le suma una ficha a la cantidad con el método add_checker(column) 
             y verifica que la cantidad de fichas en la columna 5 sea igual a 2"""
        tab = self.setUp()
        tab.put_checker(5, 'x')
        tab.add_checker(5)
        self.assertEqual(tab.get_columnas()[4]['quantity'], 2)
    def test_remove_checker(self):
        """Este test prepara el tablero, agrega la ficha x en la columna 5, le suma una ficha a la cantidad con el método add_checker(column), le resta una ficha con remove_checker(column) y verifica que la cantidad de fichas en la columna 5 sea igual a 1"""
        
        tab = self.setUp()
        tab.put_checker(5, 'x')
        tab.add_checker(5)
        tab.remove_checker(5)
        self.assertEqual(tab.get_columnas()[4]['quantity'], 1)
    def test_put_checker(self):
        """ Este test prepara el tablero, agrega distintas fichas en tres columnas distintas del tablero con put_checker(column, checker) y luego verifica que en __columnas__, en dichas columnas especificas se encuentren esas fichas, y que en una columna no elegida la ficha sea ' '."""
        tab = self.setUp()
        tab.put_checker(5, 'x')
        tab.put_checker(7, 'o')
        tab.put_checker(22, 'y')
        self.assertEqual(tab.get_columnas()[4]['checker'], 'x')
        self.assertEqual(tab.get_columnas()[6]['checker'], 'o')
        self.assertEqual(tab.get_columnas()[21]['checker'], 'y')
        self.assertEqual(tab.get_columnas()[10]['checker'], ' ')
if __name__ == '__main__':
    unittest.main()