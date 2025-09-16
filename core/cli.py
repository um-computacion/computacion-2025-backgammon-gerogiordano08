import cmd
from core.game import Game
class CLI(cmd.Cmd):
    intro = 'Bienvenido a Backgammon por Geronimo Giordano. Escribe \'ayuda\' para ver los comandos disponibles, \'reglas\' para ver las reglas del juego. Cuando estes listo, ingresa \'start\' para iniciar el juego.'
    prompt = '(backgammon) >>> '
    def __init__(self):
        super().__init__()
        self.__game__ = None

    def do_start(self, line):
        """Comienza el juego"""
        try:
            nombrej1 = str(input("Ingresa el nombre del jugador 1:\n"))
            nombrej2 = str(input("Ingresa el nombre del jugador 2:\n"))
        except ValueError:
            print("Ingresaste un nombre no valido. Intenta de nuevo.")
            return
        self.__game__ = Game(nombrej1, nombrej2)
        print("El juego fue iniciado con exito!")
    def do_salir(self, line):
        """Cierra el programa."""
        print("Gracias por jugar!")
        return True
    def do_ayuda(self, line):
        """Muestra los comandos disponibles para ejecutar."""
        print(f"salir -> {self.do_salir.__doc__}")
        print(f"reglas -> {self.do_reglas.__doc__}")
        print(f"start -> {self.do_start.__doc__}")
    def do_reglas(self, line):
        """ Muestra las reglas del juego."""
        print("Estas son las reglas:")
if __name__ == '__main__':
    CLI().cmdloop()