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
    def turn(self, player: Player):
        """ El método define la lógica principal de un turno individual en el juego, desde tirar los dados hasta que se complete totalmente el turno para pasar al próximo jugador. """
        # Definición de variables locales
        turn_player_checker: str = self.__checker_1__.get_symbol() if player.get_checker_type() == self.__checker_1__.get_type() else self.__checker_2__.get_symbol()
        turn_player_bar = player.get_bar_index()
        other_player_bar = 24 if turn_player_bar == 25 else 25
        has_checkers_in_bar = True if self.__board__.get_columnas()[turn_player_bar]['quantity'] > 0 else False
        # Comienza el flow del turno
        print(f"Turno de {player.get_name()}.")
        self.roll_dice()
        dice = list(self.get_dice().get_dice_results())
        
        # Muestra dados disponibles
        if len(dice) == 2:
            print(f"Dado 1: {dice[0]}. \n Dado 2: {dice[1]}") 
        else:
            print(f"Dado 1: {dice[0]}. \n Dado 2: {dice[1]}. \n Tienes dobles!" )
        # Comienza loop que maneja cada movimiento disponible
        for x in range(len(dice)):
            successful_move = False
            while not successful_move:
                # Caso 1: fichas en barra. OBLIGADO A SACARLAS. 
                if has_checkers_in_bar:
                    print("Tienes fichas en la barra. Estas obligado a usar tus movimientos en esas fichas hasta que no quede ninguna.")                     
                    available_dice_indexes = []
                    for d in dice:
                        if self.available_move(turn_player_bar, turn_player_bar + d, player):
                            available_dice_indexes.append(dice.index(d))
                    # Caso 1-1: no puede usar ninguno de los dados para sacar fichas de la barra. Pierde el turno.
                    if len(available_dice_indexes) == 0:
                        print("Mala suerte! No puedes usar ninguno de tus dados para sacar fichas de la barra. Pierdes el turno. ")
                        successful_move = True
                        return
                    # Caso 1-2: los dados que no se pueden usar son extraidos de la lista dice. 
                    for x in dice:
                        dice.pop(x) if x not in available_dice_indexes else None
                    fro: int = turn_player_bar
                    print("Dados disponibles:")
                    for x in dice:
                        print(f"Dado {x+1}: {dice[x]}")
                    used_die: int = int(input("Que dado usaras? (ingresa la cantidad que muestra el dado)"))
                    if used_die not in dice:
                        print("Ese dado no esta disponible. ")
                        return
                    else:
                        used_die_index = dice.index(used_die)
                    to: int = fro + used_die
                    if self.available_move(fro, fro+used_die, player):
                        if self.__board__.get_columnas()[to]['checker'] == turn_player_checker:
                            self.add_checker(to)
                            self.remove_checker(fro)
                        else:
                            self.put_checker(to, turn_player_checker)
                            self.remove_checker(fro)
                            self.add_checker(other_player_bar)
                            successful_move = True
                    else:
                        print("El movimiento no se puede completar! Verifica que sea valido e intentalo de nuevo. ")
                        return
                else:
                    # Caso 2: no tiene fichas en barra. Puede elegir movimientos
                    fro: int = int(input("Que ficha quieres mover? (ingresa columna)"))
                    print("Dados disponibles:")
                    for x in dice:
                        print(f"Dado {x+1}: {dice[x]}")
                    used_die: int = int(input("Que dado usaras? (ingresa la cantidad que muestra el dado)"))
                    if used_die not in dice:
                        print("Ese dado no esta disponible. ")
                        return
                    else:
                        used_die_index = dice.index(used_die)
                    to: int = fro + used_die
                    finishing_move = True if to > 23 else False
                    # Caso 2-1: el jugador intenta sacar una ficha del tablero. 
                    if finishing_move:
                        if self.finish_checker(fro, player):
                            successful_move = True
                        else:
                            print("El movimiento no se puede completar! Verifica que sea valido e intentalo de nuevo")
                            return
                    # Caso 2-2: el jugador intenta hacer un movimiento normal.  
                    else:
                        if self.available_move(fro, fro+used_die, player):
                            if self.__board__.get_columnas()[to]['checker'] == turn_player_checker:
                                self.add_checker(to)
                                self.remove_checker(fro)
                            else:
                                self.put_checker(to, turn_player_checker)
                                self.remove_checker(fro)
                                self.add_checker(other_player_bar)
                                successful_move = True
                        else:
                            print("El movimiento no se puede completar! Verifica que sea valido e intentalo de nuevo. ")
                            return
                # Si no hay ningun problema, succesful_move va a ser True y se va a seguir con el proximo dado. 
                dice.pop(used_die_index)
                print("El movimiento fue completado exitosamente!")
                self.show_board()
                    
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
