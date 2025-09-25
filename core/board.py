"""Modulo Board. Contiene la definicion de la clase Board."""
class Board:
    """La clase Board define la lógica del tablero junto con
    todos los metodos necesarios para la actividad sobre este. Atributo: columnas (dict)."""
    def __init__(self):

        self.__columnas__ = [{'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'bar': True, 'checker' : 'x', 'quantity' : 0},
                             {'bar': True, 'checker' : 'o', 'quantity' : 0}]
    def show_board(self):
        """ Este método imprime el tablero, poniendo el método checker(column, level)
        con las respectivas coordenadas en cada espacio ocupable por fichas del tablero."""
        c = self.checker

        print("                          TABLERO DE BACKGAMMON")
        print("           13  14  15  16  17  18   |BAR|   19  20  21  22  23  24")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        for y in range(1, 6):
            left = ' | '.join([f"{c(x,y)}" for x in range(12, 18, 1)])
            right = ' | '.join([f"{c(x,y)}" for x in range(18, 24, 1)])
            bar_o = c(25, y)
            print(f"Fila {y}   | {left} |  | {bar_o} |  | {right} |")
        print("Fila 6   | v | v | v | v | v | v |  |   |  | v | v | v | v | v | v |")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("Fila 6   | ^ | ^ | ^ | ^ | ^ | ^ |  |   |  | ^ | ^ | ^ | ^ | ^ | ^ |")
        for y in range(5, 0, -1):
            left = ' | '.join([f"{c(x,y)}" for x in range(11, 5, -1)])
            right = ' | '.join([f"{c(x,y)}" for x in range(5, -1, -1)])
            bar_x = c(24, y)
            print(f"Fila {y}   | {left} |  | {bar_x} |  | {right} |")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("          12  11  10   9   8   7    |BAR|    6   5   4   3   2   1")
        print("- La columna central es la **BAR** (barra).")
        print("- Si un punto tiene más de 5 fichas, usa (6), (7), etc.")
    def checker(self, column:int, level:int):
        """ Este método devuelve la ficha correspondiente (o ninguna)
        dependiendo de las coordenadas del tablero y la ocupacion,
        que analiza en el atributo __columnas__ y __barra__ (para fichas en las barras)  """
        q = self.__columnas__[column]['quantity']
        if  q == 0:
            return ' '
        if q > 5 and level == 5:
            return q
        if q >= level:
            return self.__columnas__[column]["checker"]
        return ' '
    def add_checker(self, column:int, quan = 1):
        """ Este método aumenta por 'quan' unidades (1 por defecto) 
        la cantidad de fichas que se encuentran en una columna del tablero, 
        accediendo al atributo __columnas__. Debe haberse configurado 
        la ficha previamente para que su uso tenga sentido. """
        self.__columnas__[column]['quantity'] += quan
    def remove_checker(self, column:int, quan = 1):
        """ Este método reduce por 'quan' unidades (1 por defecto)
        la cantidad de fichas que se encuentran en una columna del tablero,
        accediendo al atributo __columnas__. Debe haberse configurado
        la ficha previamente y la cantidad debe ser mayor que 0 para que su uso tenga sentido. """
        self.__columnas__[column]['quantity'] -= quan
    def put_checker(self, column:int, checker:str, quan = 1):
        """ Este método configura una ficha especifica en una columna,
        determinando que ficha es y la cantidad a 'quan' unidades (1 por defecto). """
        self.__columnas__[column]['checker'] = checker
        self.__columnas__[column]['quantity'] = quan
    def clear_board(self):
        """ Este método limpia el tablero dejando la ficha ' '
        con cantidad = 0 en todas las columnas. """
        for x in range(0,24):
            self.put_checker(x, ' ')
            self.__columnas__[x]['quantity'] = 0
    def get_columnas(self):
        """ Este método devuelve el atributo __columnas__ para su uso externamente. """
        return self.__columnas__
