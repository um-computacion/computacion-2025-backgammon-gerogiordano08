class Board:
    def __init__(self):

        self.__columnas__ = [{'checker' : 'x', 'quantity' : 9}, {'checker' : 'x', 'quantity' : 3}, {'checker' : 'x', 'quantity' : 5}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : 'o', 'quantity' : 3}, {'checker' : 'o', 'quantity' : 4}, {'checker' : 'o', 'quantity' : 4}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}]
        self.__barra__ = ()
    def show_board(self):
        """ Este método imprime el tablero, poniendo el método checker(column, level) con las respectivas coordenadas en cada espacio ocupable por fichas del tablero."""
        c = self.checker

        print("                          TABLERO DE BACKGAMMON")
        print("           24  23  22  21  20  19   |BAR|   18  17  16  15  14  13")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        for y in range(1, 6):
            left = ' | '.join([f"{c(x,y)}" for x in range(23, 17, -1)])
            right = ' | '.join([f"{c(x,y)}" for x in range(17, 11, -1)])
            print(f"Fila {y}   | {left} |  |   |  | {right} |")
        print("Fila 6   | v | v | v | v | v | v |  |   |  | v | v | v | v | v | v |")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("Fila 6   | ^ | ^ | ^ | ^ | ^ | ^ |  |   |  | ^ | ^ | ^ | ^ | ^ | ^ |")
        for y in range(5, 0, -1):
            left = ' | '.join([f"{c(x,y)}" for x in range(0, 6)])
            right = ' | '.join([f"{c(x,y)}" for x in range(6, 12)])
            print(f"Fila {y}   | {left} |  |   |  | {right} |")
        print("         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("           1   2   3   4   5   6    |BAR|    7   8   9  10  11  12")
        print("- La columna central es la **BAR** (barra).")
        print("- Si un punto tiene más de 5 fichas, usa (6), (7), etc.")
    
    def checker(self, column, level):
        """ Este método devuelve la ficha correspondiente (o ninguna) dependiendo de las coordenadas del tablero y la ocupacion, que analiza en el atributo __columnas__. """
        q = self.__columnas__[column]['quantity']
        if  q == 0:
            return ' '
        elif q > 5 and level == 5:
            return q
        elif q >= level:
            return self.__columnas__[column]["checker"]
        else:
            return ' '
        
    def add_checker(self, column):
        """ Este método aumenta por una unidad la cantidad de fichas que se encuentran en una columna del tablero, accediendo al atributo __columnas__. Debe haberse configurado la ficha previamente para que su uso tenga sentido. """
        self.__columnas__[column - 1]['quantity'] += 1
    
    def remove_checker(self, column):
        """ Este método reduce por una unidad la cantidad de fichas que se encuentran en una columna del tablero, accediendo al atributo __columnas__. Debe haberse configurado la ficha previamente y la cantidad debe ser mayor que 0 para que su uso tenga sentido. """
        self.__columnas__[column - 1]['quantity'] -= 1
    
    def put_checker(self, column, checker):
        """ Este método configura una ficha especifica en una columna, determinando que ficha es y la cantidad a 1. """
        self.__columnas__[column - 1]['checker'] = checker
        self.__columnas__[column - 1]['quantity'] = 1
   
    def get_columnas(self):
        """ Este método devuelve el atributo __columnas__ para su uso externamente. """
        return self.__columnas__


