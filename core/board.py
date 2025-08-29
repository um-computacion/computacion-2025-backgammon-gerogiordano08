class Board:
    def __init__(self):

        self.__columnas__ = [{'checker' : 'x', 'quantity' : 9}, {'checker' : 'x', 'quantity' : 3}, {'checker' : 'x', 'quantity' : 5}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0},
                             {'checker' : 'o', 'quantity' : 3}, {'checker' : 'o', 'quantity' : 4}, {'checker' : 'o', 'quantity' : 4}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}, {'checker' : '', 'quantity' : 0}]
        self.__barra__ = ()
    def show_board(self):
        
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
        print("""
- La columna central es la **BAR** (barra).
- Si un punto tiene más de 5 fichas, usa (6), (7), etc."
              """)

    def checker(self, column, level):
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
        self.__columnas__[column - 1]['quantity'] += 1
    def remove_checker(self, column):
        self.__columnas__[column - 1]['quantity'] -= 1
    def put_checker(self, column, checker):
        self.__columnas__[column - 1]['checker'] = checker
        self.__columnas__[column - 1]['quantity'] += 1
# tab = Board()
# tab.show_board()

