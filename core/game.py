"""Modulo Game. Define la clase Game."""
from core.player import Player
from core.checker import Checker
from core.dice import Dice
from core.board import Board

class Game:
    """La clase Game define la logica del juego. Atributos: board (Board), dice (Dice),
    checker_1 (Checker), checker_2 (Checker), player_1 (Player), player_2 (Player)."""
    def __init__(self, p1_name, p2_name):
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__checker_1__ = Checker(1)
        self.__checker_2__ = Checker(2)
        self.__player_1__ = Player(p1_name, 1)
        self.__player_2__ = Player(p2_name, 2)
    def prepare_board(self):
        """ Este método deja el tablero listo para el juego,
        dejando las 30 fichas en sus lugares correspondientes. """
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
    def turn(self, player: Player):
        """ El método define la lógica principal de un turno individual
        en el juego, desde tirar los dados hasta que se complete totalmente
        el turno para pasar al próximo jugador. """
        # Definición de variables locales
        if player.get_checker_type() == self.__checker_1__.get_c_type():
            turn_player_checker: str = self.__checker_1__.get_symbol()
        else:
            turn_player_checker: str = self.__checker_2__.get_symbol()
        has_checkers_in_bar = bool(self.__board__.get_columnas()[turn_player_bar]['quantity'] > 0)
        # Comienza el flow del turno
        print(f"Turno de {player.get_name()}.")
        self.roll_dice()
        dice = list(self.get_dice().get_dice_results())
        # Muestra dados disponibles
        if len(dice) == 2:
            print(f"Dado 1: {dice[0]}. \nDado 2: {dice[1]}")
        else:
            print(f"Dado 1: {dice[0]}. \nDado 2: {dice[1]}. \n Tienes dobles!" )
        # Comienza loop que maneja cada movimiento disponible
        for x in range(len(dice)):
            successful_move = False
            while not successful_move:
                self.__board__.show_board()
                if has_checkers_in_bar:
                    successful_move, used_die = self.turn_fichas_barra(player, dice, turn_player_checker)
            dice.pop(used_die) if used_die != None else None
            print("El movimiento fue completado exitosamente!")
            self.__board__.show_board()
    # Verificadores condicionales
    def turn_fichas_barra(self, player: Player, dice, turn_player_checker):
        print("Tienes fichas en la barra. Estas obligado a usar " \
        "tus movimientos en esas fichas hasta que no quede ninguna.")
        available_dice_indexes = []
        fro = player.get_bar_practical_index()
        for d in dice:
            if self.available_move(fro, fro + d, player):
                available_dice_indexes.append(dice.index(d))
        # Caso 1-1: no puede usar ninguno de los dados para
        # sacar fichas de la barra. Pierde el turno.
        if len(available_dice_indexes) == 0:
            print("Mala suerte! No puedes usar ninguno de " \
            "tus dados para sacar fichas de la barra. Pierdes el turno. ")
            return True, None
        # Caso 1-2: los dados que no se pueden usar son extraidos de la lista dice.
        for x in dice:
            if dice.index(x) not in available_dice_indexes:
                dice.pop(dice.index(x))
        print("Dados disponibles:")
        for x in dice:
            print(f"Dado {dice.index(x)+1}: {x}")
            #cuando hay dobles imprime siempre dado 1, dice.index(x)
            # va a ser siempre 0, porque son todos iguales. Solucionar
        used_die: int = int(input("Que dado usaras? (ingresa la cantidad " \
        "que muestra el dado)"))
        if used_die not in dice:
            print("Ese dado no esta disponible. ")
            return False, None
        to: int = fro + used_die if fro == 5 else fro - used_die
        if self.available_move(fro, fro+used_die, player):
            if self.__board__.get_columnas()[to]['checker'] == turn_player_checker:
                self.__board__.add_checker(to)
                self.__board__.remove_checker(fro)
            else:
                self.__board__.put_checker(to, turn_player_checker)
                self.__board__.remove_checker(fro)
                self.__board__.add_checker(player.get_opp_bar_index())
            return True, used_die
        else:
            print("El movimiento no se puede completar! " \
            "Verifica que sea valido e intentalo de nuevo. ")
        return False, None
    def turn_normal(self):
        fro: int = int(input("Que ficha quieres mover? (ingresa columna)"))
        print("Dados disponibles:")
        for x in dice:
            print(f"Dado {dice.index(x)+1}: {x}")
            used_die: int = int(input("Que dado usaras? "
            "(ingresa la cantidad que muestra el dado)"))
            if used_die not in dice:
                print("Ese dado no esta disponible. ")
                return
            used_die_index = dice.index(used_die)
            to: int = fro + used_die if player.get_checker_type() == 1 else fro - used_die
            finishing_move = bool(to > 23)
            # Caso 2-1: el jugador intenta sacar una ficha del tablero.
            if finishing_move:
                if self.finish_checker(fro, player):
                    successful_move = True
                else:
                    print("El movimiento no se puede completar! " \
                    "Verifica que sea valido e intentalo de nuevo")
                    return
            # Caso 2-2: el jugador intenta hacer un movimiento normal.
            else:
                if self.available_move(fro, fro+used_die, player):
                    if self.__board__.get_columnas()[to]['checker'] == turn_player_checker:
                        self.__board__.add_checker(to)
                        self.__board__.remove_checker(fro)
                    else:
                        self.__board__.put_checker(to, turn_player_checker)
                        self.__board__.remove_checker(fro)
                        self.__board__.add_checker(other_player_bar)
                        successful_move = True
                else:
                    print("El movimiento no se puede completar! " \
                    "Verifica que sea valido e intentalo de nuevo. ")
                    return
    def available_move(self, fro:int, to:int, player: Player):
        """ Verifica que un movimiento sea válido segun las normas del juego. """
        columnas = self.__board__.get_columnas()
        if player.get_checker_type() == 1:
            player_checker = self.__checker_1__
        else:
            player_checker = self.__checker_2__

        if to > 23:
            return False
        if columnas[fro]['checker']==player_checker.get_symbol() and columnas[fro]['quantity']>0:
            return bool(columnas[to]['quantity'] < 2 or columnas[fro]['checker'] == columnas[to]['checker'])
        return False

    def can_finish_checkers(self, player: Player):
        """ Verifica que el jugador player puede empezar a sacar
        sus fichas del tablero en la fase final. """
        if player.get_checker_type() == 1:
            for x in range(0, 18):
                if self.__board__.get_columnas()[x]['checker'] == self.__checker_1__.get_symbol():
                    if self.__board__.get_columnas()[x]['quantity'] > 0:
                        return False
            return True
        if player.get_checker_type() == 2:
            for x in range(6, 24):
                if self.__board__.get_columnas()[x]['checker'] == self.__checker_2__.get_symbol():
                    if self.__board__.get_columnas()[x]['quantity'] > 0:
                        return False
            return True
        return False
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
        return bool(self.__board__.get_columnas()[col]['quantity'] > 0)
    def finish_checker(self, col, player: Player):
        """ Verifica si el jugador puede terminar una ficha y
        la termina. Ademas devuelve True si fue exitoso y False si no lo fue. """
        if player.get_checker_type() == 1:
            can_p_finish_checkers = self.can_finish_checkers(self.__player_1__)
        else:
            can_p_finish_checkers = self.can_finish_checkers(self.__player_2__)
        if can_p_finish_checkers:
            self.__board__.remove_checker(col)
            return True
        return False

    # Métodos de clase Board

    def add_checker(self, column:int, quan = 1):
        """ (Game)Este método aumenta por 'quan' unidades (1 por defecto)
        la cantidad de fichas que se encuentran en una columna del tablero,
        accediendo al atributo __columnas__. Debe haberse configurado la ficha
        previamente para que su uso tenga sentido. """
        self.__board__.add_checker(column, quan)


    # Getters

    def get_board(self):
        """Devuelve el atributo board (objeto Board)."""
        return self.__board__
    def get_dice(self):
        """Devuelve el atributo dice (objeto Dice)."""
        return self.__dice__
    def get_player_1(self):
        """Devuelve el atributo player_1 (objeto Player)."""
        return self.__player_1__
    def get_player_2(self):
        """Devuelve el atributo player_2 (objeto Player)."""
        return self.__player_2__
    def get_checker_1(self):
        """Devuelve el atributo checker_1 (objeto Checker)."""
        return self.__checker_1__
    def get_checker_2(self):
        """Devuelve el atributo checker_2 (objeto Checker)."""
        return self.__checker_2__
