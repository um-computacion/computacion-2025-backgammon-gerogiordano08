from core.cli import CLI
from core.game import Game
from core.board import Board
import unittest
from unittest.mock import Mock, patch, call
class CLITests(unittest.TestCase):
    def setUp(self):
        self.cli = CLI()

    @patch("builtins.print")
    @patch("builtins.input", side_effect=SystemExit)
    def test_do_start_prints(self, mock_print, mock_input):
        """Testea que la funcion muestre las indicaciones correctas en la consola"""
        with self.assertRaises(SystemExit):
            self.cli.do_start()
        mock_print.assert_any_call("Ingresa el nombre del jugador 1:\n")
        self.cli.set_contador(1)
        with self.assertRaises(SystemExit):
            self.cli.do_start()
        mock_print.assert_any_call("Ya hay un juego en progreso. Estas seguro que quieres sobreescribirlo? (y/n)")
    
    @patch('builtins.input', side_effect=['a', 'b'])
    def test_do_start(self, mock_input):
        """Testea que la funcion inicie correctamente el juego."""
        self.cli.do_start()
        self.assertEqual(self.cli.get_game().get_player_1().get_name(), 'a')
        self.assertEqual(self.cli.get_game().get_player_2().get_name(), 'b')
        self.assertEqual(self.cli.get_contador(), 1)

    @patch('builtins.print')
    def test_do_play_no_hay_juego(self, mock_print):
        self.cli.set_contador(0)
        self.cli.do_play()
        mock_print.assert_any_call("Primero debes usar el comando 'start' para iniciar un nuevo juego!")

    @patch("builtins.print")
    def test_do_play_winner_p1(self,mock_print):
        self.cli.set_contador(1)
        ng = Game('a', 'b')
        b = Board()
        b.put_checker(1, 'o')
        b.show_board()
        ng.set_board(b)
        self.cli.set_game(ng)
        self.cli.do_play()
        mock_print.assert_any_call("Felicitaciones a!!!\nGanaste el juego =)\nEspero que lo hayas disfrutado, gracias por jugar!")
    @patch("builtins.print")
    def test_do_play_winner_p2(self,mock_print):
        self.cli.set_contador(1)
        ng = Game('a', 'b')
        b = Board()
        b.put_checker(22, 'x')
        ng.set_board(b)
        self.cli.set_game(ng)
        self.cli.do_play()
        mock_print.assert_any_call("Felicitaciones b!!!\nGanaste el juego =)\nEspero que lo hayas disfrutado, gracias por jugar!")

    @patch('builtins.input', side_effect=['a', 'b'])
    @patch("core.cli.Game.turn")
    def test_do_play_to_turn_p1(self, mock_turn, mock_input):
        self.cli.do_start()
        self.cli.do_play()
        mock_turn.assert_called_once()

    @patch('builtins.input', side_effect=['a', 'b'])
    @patch("core.cli.Game.turn")
    def test_do_play_to_turn_p2(self, mock_turn, mock_input):
        self.cli.do_start()
        self.cli.set_contador(2)
        self.cli.do_play()
        mock_turn.assert_called_once()
    @patch("builtins.print")
    @patch('builtins.input', side_effect=['a', 'b'])
    def test_winner_message(self, mock_input, mock_print):
        self.cli.do_start()
        self.cli.winner_message(self.cli.get_game().get_player_1())
        mock_print.assert_any_call("Felicitaciones a!!!\nGanaste el juego =)\nEspero que lo hayas disfrutado, gracias por jugar!")

    def test_do_salir(self):
        self.assertTrue(self.cli.do_salir())
    @patch('builtins.print')
    def test_do_ayuda(self, mock_input):
        self.cli.do_ayuda()
        calls = (call(f"salir -> {self.cli.do_salir.__doc__}"),
                 call(f"reglas -> {self.cli.do_reglas.__doc__}"),
                 call(f"start -> {self.cli.do_start.__doc__}"),
                 call(f"play -> {self.cli.do_play.__doc__}"))
        mock_input.assert_has_calls(calls)

    @patch('builtins.print')
    def test_do_reglas(self, mock_print):
        reglas = {"tablero": "En el backgammon se enfrentan dos jugadores. Cada uno de ellos " \
                "utiliza 15 fichas, blancas y negras respectivamente, que se distribuyen sobre un "
                "tablero con 24 casillas triangulares.\n\nLos dos jugadores avanzan sus fichas "
                "sobre las casillas, en sentidos opuestos, según las tiradas que obtienen con los "
                "dados, con el objetivo de ser el primero en completar el recorrido y sacar todas "
                "sus fichas del tablero."

                , "mover fichas": "En cada tirada se lanzan dos dados. En la primera tirada del "
                "juego ambos jugadores tiran cada uno un dado. Si obtienen el mismo número, "
                "tiran de nuevo. Quien consigue el número más alto realiza la primera jugada,"
                " aprovechando los números ya obtenidos en esa tirada.\n\nLas fichas se mueven"
                " de acuerdo a las siguientes reglas:\n-Se mueven por separado los números"
                " obtenidos con los dos dados, con una única ficha o con fichas diferentes."
                "\n-Los movimientos de ambos números pueden hacerse en cualquier orden.\n-Las"
                " fichas no pueden caer en una casilla ocupada por más de una ficha rival. En "
                "este caso el movimiento no es posible.\n-Cuando la ficha se mueve a una casilla"
                " ocupada por una única ficha rival, esta es capturada.\n-Se puede acumular "
                "cualquier número de fichas de un mismo color en una sola casilla.\n-En caso de"
                " obtener un doble (el mismo número repetido) no se realizan dos avances con el "
                "mismo número, sino cuatro.\n-Es obligatorio completar los movimientos de la "
                "tirada, siempre que sea posible, utilizando fichas que no queden bloqueadas. "
                "Si es posible mover con una ficha cualquiera de los dos números pero no la suma "
                "de ambos, se moverá el número más alto."

                , "capturar": "Cuando la ficha jugada llega a una casilla ocupada por una única "
                "ficha rival, esta resulta capturada y se sitúa sobre la barra central del "
                "tablero.\n\nSiempre que un jugador tiene alguna ficha capturada en la barra, "
                "está obligado a introducirla de nuevo en el juego desde el primer cuadrante del"
                " recorrido usando las tiradas de los dados. Mientras no consiga liberarlas, el "
                "resto de fichas quedan bloqueadas.\n\nSi un jugador tiene alguna ficha capturada "
                "y el rival bloquea su último cuadrante (el primero para el jugador capturado)"
                " con un mínimo de dos fichas en cada casilla, pierde el turno porque no tiene"
                " posibilidad de realizar ningún movimiento."

                , "completar recorrido": "Cuando un jugador consigue llevar todas sus fichas "
                "hasta el último cuadrante, puede empezar a sacar las fichas del tablero "
                "llevándolas al cajón final.\n\nPara sacar una ficha debe utilizarse el número"
                " exacto. Tan solo puede utilizarse un número superior en los casos en los que "
                "las casillas más distantes del final del recorrido ya están libres.\n\nSi una "
                "ficha resulta capturada, la fase bearing off queda interrumpida, de manera que "
                "no puede seguir sacando fichas del tablero hasta que la ficha capturada "
                "alcanza de nuevo el cuadrante final."

                , "final": "Vence el jugador que logra sacar antes sus 15 fichas.\n\nEl vencedor"
                " logra un gammon cuando su rival no ha conseguido sacar ninguna de sus 15 "
                "fichas. En este caso, la victoria cuenta el doble.\n\nEl vencedor logra un "
                "backgammon cuando su rival no ha conseguido sacar ninguna de sus 15 fichas, "
                "y además todavía mantiene al menos una ficha en la barra de salida o el primer"
                " cuadrante. En este caso, la victoria cuenta el triple."

                , "": "Debes ingresar un tema, para recibir las reglas especificas de ese tema."
                "\nPor ejemplo >>> reglas tablero\nLos temas disponibles son: tablero, mover "
                "fichas, capturar, completar recorrido, final."
                }
        for x, y in reglas.items():
            self.cli.do_reglas(x)
            mock_print.assert_any_call(f'\n{y}')
    