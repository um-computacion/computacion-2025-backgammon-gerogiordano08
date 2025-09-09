from core.player import Player
from core.checker import Checker
from core.dice import Dice
from core.board import Board

class Game:
    def __init__(self, p1_name, p2_name):
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__checker_1__ = Checker(1)
        self.__checker_2__ = Checker(2)
        self.__player_1__ = Player(p1_name, 1)
        self.__player_2__ = Player(p2_name, 2)
    def prepare_board(self):
        """ Este método deja el tablero listo para el juego, dejando las 30 fichas en sus lugares correspondientes. """
        self.__board__.clear_board()
        put = self.__board__.put_checker
        c1 = self.__checker_1__.get_symbol()
        c2 = self.__checker_2__.get_symbol()
        put(11, c1, 5)
        put(0, c1, 2)
        put(18, c1, 5)
        put(16, c1, 3)

        put(5, c2, 5)
        put(7, c2, 3)
        put(12, c2, 5)
        put(23, c2, 2)
    def move_checker(self, fro, to):
        """ Este método saca una ficha de una columna fro y la suma en la columna to"""
        self.__board__.remove_checker(fro)
        columnas = self.__board__.get_columnas()
        if columnas[to]['quantity'] == 0:

            self.__board__.put_checker(to, columnas[fro]['checker'])
        else:
            self.__board__.add_checker(to)
    def roll_dice(self):
        """ Usa el método roll_dice() de la clase Dice. """
        self.__dice__.roll_dice()
        dice = self.__dice__.get_dice()
        return dice and dice if dice[0] == dice[1] else dice
    def turn(self, player: Player):
        print(f"Turno de {player.get_name()}.")
        dice = self.roll_dice()
        doubles = False
        if len(dice) == 2:
            print(f"Dado 1: {dice[0]}. \n Dado 2: {dice[1]}") 
        else:
            print(f"Dado 1: {dice[0]}. \n Dado 2: {dice[1]}. \n Tienes dobles!" )
            doubles = True
        if doubles == False:
            for x in range(0, 2):
                successful_move = False
                while not successful_move:
                    fro: int = int(input("Que ficha quieres mover? (ingresa columna)"))
                    print("Dados disponibles:")
                    for x in dice:
                        print(f"Dado {x+1}: {dice[x]}")
                    used_die: int = int(input("Que dado usaras? (ingresa la cantidad que muestra el dado)"))
                    if used_die not in dice:
                        print("Ese dado no esta disponible. ")
                        return
                    to: int = fro + used_die
                    finishing_move = True if to > 23 else False

                    if finishing_move:
                        if self.finish_checker(fro, player):
                            successful_move = True
                        else:
                            print("El movimiento no se puede completar! Verifica que sea valido e intentalo de nuevo")
                            return
                    else:
                        if self.available_move(fro, fro+used_die, player):
                            successful_move = True
                        else:
                            return
                    
    # Verificadores condicionales

    def available_move(self, fro:int, to:int, player: Player):
        """ Verifica que un movimiento sea válido segun las normas del juego. """
        columnas = self.__board__.get_columnas()
        player_checker = self.__checker_1__ if player.get_checker_type() == 1 else self.__checker_2__

        if to > 23:
            return False
        else:
            if columnas[fro]['checker'] == player_checker.get_symbol() and columnas[fro]['quantity'] > 0:
                if columnas[to]['quantity'] < 2 or columnas[fro]['checker'] == columnas[to]['checker']:
                    return True
                else: 
                    return False
            else:
                return False
    def can_finish_checkers_p1(self):
        """ Verifica que el jugador 1 puede empezar a sacar sus fichas del tablero en la fase final. """
        for x in range(0, 18):
            if self.__board__.get_columnas()[x]['checker'] == self.__checker_1__.get_symbol():
                if self.__board__.get_columnas()[x]['quantity'] > 0:
                    return False
        return True
    def can_finish_checkers_p2(self):
        """ Verifica que el jugador 2 puede empezar a sacar sus fichas del tablero en la fase final. """
        for x in range(6, 24):
            if self.__board__.get_columnas()[x]['checker'] == self.__checker_2__.get_symbol():
                if self.__board__.get_columnas()[x]['quantity'] > 0:
                    return False
        return True
    def win_condition(self, player: Player):
        """ Verifica si el jugador dado como argumento ha ganado o sigue en juego. """
        if player.get_checker_type() == 1:
            c = self.__checker_1__
        else:
            c = self.__checker_2__
        for x in range(0, 18):
            if self.__board__.get_columnas()[x]['checker'] == c.get_symbol():
                if self.__board__.get_columnas()[x]['quantity'] > 0:
                    return False
        return True
    def check_bar(self, player: Player):
        """ Verifica si el jugador en cuestion tiene fichas en la barra. """
        col = 24 if player.get_checker_type() == 1 else 25
        return True if self.__board__.get_columnas()[col]['quantity'] > 0 else False
    def finish_checker(self, col, player: Player):
        """ Verifica si el jugador puede terminar una ficha y la termina. Ademas devuelve True si fue exitoso y False si no lo fue. """
        can_p_finish_checkers = self.can_finish_checkers_p1() if player.get_checker_type() == 1 else self.can_finish_checkers_p2()
        if can_p_finish_checkers:
            self.remove_checker(col)
            return True
        else:
            return False

    # Métodos de clase Board

    def add_checker(self, column:int, quan = 1):
        """ Este método aumenta por 'quan' unidades (1 por defecto) la cantidad de fichas que se encuentran en una columna del tablero, accediendo al atributo __columnas__. Debe haberse configurado la ficha previamente para que su uso tenga sentido. """
        self.__board__.add_checker(column, quan)
    def remove_checker(self, column:int, quan = 1):
        """ Este método reduce por 'quan' unidades (1 por defecto) la cantidad de fichas que se encuentran en una columna del tablero, accediendo al atributo __columnas__. Debe haberse configurado la ficha previamente y la cantidad debe ser mayor que 0 para que su uso tenga sentido. """
        self.__board__.remove_checker(column, quan)
    def put_checker(self, column:int, checker:str, quan = 1):
        """ Este método configura una ficha especifica en una columna, determinando que ficha es y la cantidad a 'quan' unidades (1 por defecto). """
        self.__board__.put_checker(column, checker, quan)
    def clear_board(self):
        """ Este método limpia el tablero dejando la ficha ' ' con cantidad = 0 en todas las columnas. """
        self.__board__.clear_board()
    def show_board(self):
        """ Este método imprime el tablero, poniendo el método checker(column, level) con las respectivas coordenadas en cada espacio ocupable por fichas del tablero."""
        self.__board__.show_board()

    # Getters

    def get_board(self):
        return self.__board__
    def get_dice(self):
        return self.__dice__
    def get_player_1(self):
        return self.__player_1__
    def get_player_2(self):
        return self.__player_2__
    def get_checker_1(self):
        return self.__checker_1__
    def get_checker_2(self):
        return self.__checker_2__
g = Game('a', 'b')
g.prepare_board()
