"""Modulo CLI. Define la clase CLI."""
import cmd
from core.game import Game
from core.player import Player
class CLI(cmd.Cmd):
    """Definicion de la logica de CLI, que se encarga de darle al usuario una interfaz de 
    comandos para el desarrollo del juego. Incluye los atributos game (Game) y contador (int)."""
    intro = 'Bienvenido a Backgammon por Gerónimo Giordano. Escribe \'ayuda\' para ver los' \
    ' comandos disponibles, \'reglas\' para ver las reglas del juego. Cuando estes listo, ingresa' \
    ' \'start\' para iniciar el juego.'
    prompt = '(backgammon) >>> '
    def __init__(self):
        super().__init__()
        self.__game__ = Game('','')
        self.__contador__ = 0

    def do_start(self):
        """Comienza el juego"""
        if self.__contador__ != 0:
            while True:
                i = input("Ya hay un juego en progreso. " \
                "Estas seguro que quieres sobreescribirlo? (y/n)")
                if i.lower() == 'n':
                    return
                if i.lower() == 'y':
                    break
        try:
            nombrej1 = str(input("Ingresa el nombre del jugador 1:\n"))
            nombrej2 = str(input("Ingresa el nombre del jugador 2:\n"))
        except ValueError:
            print("Ingresaste un nombre no valido. Intenta de nuevo.")
            return
        self.__game__ = Game(nombrej1, nombrej2)
        self.__game__.prepare_board()
        self.__contador__ = 1
        print("El juego fue iniciado con exito!")

    def do_play(self):
        """Continua con el juego"""
        g: Game = self.__game__
        winner = None
        if g.win_condition(g.__player_1__):
            winner = g.__player_1__
        if g.win_condition(g.__player_2__):
            winner = g.__player_2__
        c = self.__contador__
        if c == 0:
            print("Primero debes usar el comando 'start' para iniciar un nuevo juego!")
            return
        if winner is not None:
            self.winner_message(winner)
            return
        if c == 1:
            g.turn(g.__player_1__)
            self.__contador__ = 2
            return
        if c == 2:
            g.turn(g.__player_2__)
            self.__contador__ = 1
            return
    def winner_message(self, winner: Player):
        """Finaliza el juego si algun jugador gano."""
        print(f"Felicitaciones {winner.get_name()}!!!\nGanaste el juego =)\nEspero que lo hayas" \
              "disfrutado, gracias por jugar!")
        self.__contador__ = 0

    def do_salir(self):
        """Cierra el programa."""
        print("Gracias por jugar!")
        return True
    def do_ayuda(self):
        """Muestra los comandos disponibles para ejecutar."""
        print(f"salir -> {self.do_salir.__doc__}")
        print(f"reglas -> {self.do_reglas.__doc__}")
        print(f"start -> {self.do_start.__doc__}")
        print(f"play -> {self.do_play.__doc__}")
    def do_reglas(self, line):
        """Muestra las reglas del juego."""
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
        if line not in reglas:
            line = ""
        print(f"\n{reglas[line]}")
    def get_game(self):
        """Devuelve el atributo game (objeto Game)"""
        return self.__game__
    def set_game(self, new_game:Game):
        """Define el atributo game (objeto Game)"""
        self.__game__ = new_game
    def get_contador(self):
        """Devuelve el atributo contador (int)"""
        return self.__contador__
    def set_contador(self, new_contador:int):
        """Define el atributo contador"""
        self.__contador__ = new_contador
