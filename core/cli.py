import cmd
from game import Game
from player import Player
class CLI(cmd.Cmd):
    intro = 'Bienvenido a Backgammon por Gerónimo Giordano. Escribe \'ayuda\' para ver los comandos disponibles, \'reglas\' para ver las reglas del juego. Cuando estes listo, ingresa \'start\' para iniciar el juego.'
    prompt = '(backgammon) >>> '
    def __init__(self):
        super().__init__()
        self.__game__ = Game('','')
        self.__contador__ = 0

    def do_start(self, line):
        """Comienza el juego"""
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

    def do_play(self, line):
        """Continua con el juego"""
        winner = None
        c = self.__contador__
        if c == 0:
            print("Primero debes usar el comando 'start' para iniciar un nuevo juego!")
            return
        g: Game = self.__game__
        if winner == 'p1':
            self.winner_message(g.__player_1__)
        elif winner == 'p2':
            self.winner_message(g.__player_2__)
        if c == 1:
            g.turn(g.__player_1__)
            winner = 'p1' if g.win_condition(g.__player_1__) else None
            c = 2
        elif c == 2:
            g.turn(g.__player_2__)
            winner = 'p2' if g.win_condition(g.__player_2__) else None
            c = 1
    def winner_message(self, winner: Player):
        """Finaliza el juego si algun jugador gano."""
        print(f"Felicitaciones {winner.get_name()}!!!\nGanaste el juego =)\nEspero que lo hayas disfrutado, gracias por jugar!")
        self.__contador__ = 0

    def do_salir(self, line):
        """Cierra el programa."""
        print("Gracias por jugar!")
        return True
    def do_ayuda(self, line):
        """Muestra los comandos disponibles para ejecutar."""
        print(f"salir -> {self.do_salir.__doc__}")
        print(f"reglas -> {self.do_reglas.__doc__}")
        print(f"start -> {self.do_start.__doc__}")
        print(f"play -> {self.do_play.__doc__}")
    def do_reglas(self, line):
        """Muestra las reglas del juego."""
        print("Las reglas van a ser agregadas proximamente...")
if __name__ == '__main__':
    CLI().cmdloop()