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
        put(0, c1, 2)
        put(11, c1, 5)
        put(16, c1, 3)
        put(18, c1, 5)

        put(5, c2, 5)
        put(7, c2, 3)
        put(12, c2, 5)
        put(23, c2, 2)
    def prepare_final(self):
        self.__board__.clear_board()
        put = self.__board__.put_checker
        c1 = self.__checker_1__.get_symbol()
        c2 = self.__checker_2__.get_symbol()
        put(19, c1, 2)

        put(21, c1, 2)

        put(23, c1, 2)
        
        put(0, c2, 2)

        put(2, c2, 2)

        put(4, c2, 2)

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
        has_checkers_in_bar = bool(self.__board__.get_columnas()[player.get_bar_index()]['quantity'] > 0)
        loop_times = len(dice)
        if has_checkers_in_bar:
            bar_quan = self.__board__.get_columnas()[player.get_bar_index()]['quantity']
            loop_times = bar_quan
        for x in range(loop_times):
            successful_move = False
            while not successful_move:
                self.__board__.show_board()
                if has_checkers_in_bar:
                    successful_move, used_die = self.turn_fichas_barra(player, dice, turn_player_checker)
                elif self.can_finish_checkers(player):
                    successful_move, used_die = self.turn_finalizar_fichas(player, dice, turn_player_checker)
                else:
                    successful_move, used_die = self.turn_normal(player, dice, turn_player_checker)
            dice.pop(dice.index(used_die)) if used_die != None else None
            print("El movimiento fue completado exitosamente!")
        self.__board__.show_board()    
    # Verificadores condicionales
    def turn_fichas_barra(self, player: Player, dice, turn_player_checker):
        print("Tienes fichas en la barra. Estas obligado a usar " \
        "tus movimientos en esas fichas hasta que no quede ninguna.")
        available_dice = []
        fro = player.get_bar_practical_index()
        for i, d in enumerate(dice):
            to = fro + d if fro == 5 else fro - d
            if self.available_move(player.get_bar_index(), to):
                available_dice.append(d)
        # Caso 1-1: no puede usar ninguno de los dados para
        # sacar fichas de la barra. Pierde el turno.
        if len(available_dice) == 0:
            print("Mala suerte! No puedes usar ninguno de " \
            "tus dados para sacar fichas de la barra. Pierdes el turno. ")
            return True, None
        # Caso 1-2: los dados que no se pueden usar son extraidos de la lista dice.

        print("Dados disponibles:")
        for i, x in enumerate(available_dice):
            print(f"Dado {i + 1}: {x}")

        used_die: int = int(input("Que dado usaras? (ingresa la cantidad " \
        "que muestra el dado)\n"))
        if used_die not in available_dice:
            print("Ese dado no esta disponible. ")
            return False, None
        to: int = fro + used_die if fro == 5 else fro - used_die
        bo = self.__board__
        if self.available_move(player.get_bar_index(), to):
            if bo.get_columnas()[to]['checker'] == turn_player_checker:
                bo.add_checker(to)
                bo.remove_checker(player.get_bar_index())
            elif bo.get_columnas()[to]['quantity'] == 0:
                bo.put_checker(to, turn_player_checker)
                bo.remove_checker(player.get_bar_index())
            else:
                bo.put_checker(to, turn_player_checker)
                bo.remove_checker(player.get_bar_index())
                bo.add_checker(player.get_opp_bar_index())
            return True, used_die
        print("El movimiento no se puede completar! " \
        "Verifica que sea valido e intentalo de nuevo. ")
        return False, None
    def turn_normal(self, player: Player, dice, turn_player_checker):
        # player_available_froms es una lista con lugares donde el jugador tenga fichas.
        player_available_froms = []
        cols = self.__board__.get_columnas()
        for i, x in enumerate(cols):
            if x['checker'] == turn_player_checker and x['quantity'] > 0:
                player_available_froms.append(i)
        fro: int = int(input("Que ficha quieres mover? (ingresa columna)\n"))-1
        if fro not in player_available_froms:
            print("No tienes fichas en esa posicion.")
            return False, None
        print("Dados disponibles:")
        for i, x in enumerate(dice):
            print(f"Dado {i+1}: {x}")
        used_die: int = int(input("Que dado usaras? "
        "(ingresa la cantidad que muestra el dado)\n"))
        if used_die not in dice:
            print("Ese dado no esta disponible. ")
            return False, None
        to: int = fro + used_die if player.get_checker_type() == 1 else fro - used_die
        # Caso 2-1: el jugador intenta sacar una ficha del tablero.
        if to > 23 or to < 0:
            if self.finish_checker(fro, player):
                print("Bien! Pudiste sacar la ficha del tablero.")
                return True, used_die
            else:
                print("El movimiento no se puede completar! " \
                "Verifica que sea valido e intentalo de nuevo")
                return False, None
        # Caso 2-2: el jugador intenta hacer un movimiento normal.
        else:
            bo = self.__board__
            if self.available_move(fro, to):
                if bo.get_columnas()[to]['checker'] == turn_player_checker:
                    bo.add_checker(to)
                    bo.remove_checker(fro)
                elif bo.get_columnas()[to]['quantity'] == 0:
                    bo.put_checker(to, turn_player_checker)
                    bo.remove_checker(fro)
                else:
                    bo.put_checker(to, turn_player_checker)
                    bo.remove_checker(fro)
                    bo.add_checker(player.get_opp_bar_index())
                return True, used_die
            
            print("El movimiento no se puede completar! " \
            "Verifica que sea valido e intentalo de nuevo. ")
            return False, None
    def turn_finalizar_fichas(self, player: Player, dice, turn_player_checker):
        print("Para finalizar el recorrido de una ficha, debes sacar exactamente el numero que" \
        " le falta en los dados, o uno mayor si ya sacaste esa ficha")
        required_dice = [1, 2, 3, 4, 5, 6]
        list_pop = []
        if player.get_checker_type() == 1:
            for i, x in enumerate(range(23, 19, -1)):
                if (self.get_board().get_columnas()[x]['quantity'] == 0):
                    list_pop.append(i)
                if (self.get_board().get_columnas()[x]['quantity'] > 0):
                    break
        if player.get_checker_type() == 2:
            for i, x in enumerate(range(0, 6)):
                if (self.get_board().get_columnas()[x]['quantity'] == 0):
                    list_pop.append(i)

                if (self.get_board().get_columnas()[x]['quantity'] > 0):
                    break

        for i in sorted(list_pop, reverse=True):
            required_dice.pop(i)
        available_dice = []

        for x in dice:
            if x in required_dice:
                available_dice.append(x)

        if len(available_dice) == 0:
            print("Mala suerte! No tienes ningun dado para usar.")
            return True, None
        
        print("Puedes usar los siguientes dados:")
        for i, x in enumerate(available_dice):
            print(f"Dado {i+1}: {x}")

        player_available_froms = []
        cols = self.__board__.get_columnas()
        for i, x in enumerate(cols):
            if x['checker'] == turn_player_checker and x['quantity'] > 0:
                player_available_froms.append(i)

        fro: int = int(input("Que ficha quieres mover? (ingresa columna)\n"))-1

        if fro not in player_available_froms:
            print("No tienes fichas en esa posicion.")
            return False, None
        
        used_die: int = int(input("Que dado usaras? (ingresa la cantidad " \
        "que muestra el dado)\n"))

        if used_die not in available_dice:
            print("Ese dado no esta disponible. ")
            return False, None
        
        if (player.get_checker_type() == 1 and fro + used_die == 24 or
            player.get_checker_type() == 2 and fro - used_die == -1):
            print("Bien! Pudiste sacar la ficha!")
            self.finish_checker(fro, player)
            return True, used_die
        if player.get_checker_type() == 1:
            for x in range(1, 6):
                if (fro != 18 and
                    self.get_board().get_columnas()[fro - x]['quantity'] == 0 and
                    fro + used_die - x == 24):
                    self.finish_checker(fro, player)
                    return True, used_die
                if self.get_board().get_columnas()[fro - x]['quantity'] != 0:
                    break
        if player.get_checker_type() == 2:
            for x in range(1, 6):
                if (fro != 5 and
                    self.get_board().get_columnas()[fro + x]['quantity'] == 0 and
                    fro - used_die + x == -1):
                    self.finish_checker(fro, player)
                    return True, used_die
                if self.get_board().get_columnas()[fro + x]['quantity'] != 0:
                    break
        if (player.get_checker_type() == 1 and fro + used_die != 24 or
            player.get_checker_type() == 2 and fro - used_die != -1):
            print("El movimiento no se puede completar! " \
            "Verifica que sea valido e intentalo de nuevo")

        return False, None


    def available_move(self, fro:int, to:int):
        """ Verifica que un movimiento sea válido segun las normas del juego. """
        columnas = self.__board__.get_columnas()
        if to > 23 or to < 0:
            return False
        if columnas[to]['quantity'] < 2:
            return True
        if columnas[fro]['checker'] == columnas[to]['checker']:
            return True
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
        for x in range(0, 24):
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
    def set_board(self, new_board: Board):
        self.__board__ = new_board
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
