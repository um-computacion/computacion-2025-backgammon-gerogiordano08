class Board:
    def __init__(self):
        self.__filas__ = [[' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ],
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ], 
                           [' ', ' ', ' ', ' ', ' ', ' ' ], [' ', ' ', ' ', ' ', ' ', ' ' ]]

        self.__barra__ = ()
    def show_board(self):
        print(f""" 
                           TABLERO DE BACKGAMMONSs
           24  23  22  21  20  19   |BAR|   18  17  16  15  14  13
         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
Fila 1   | {' | '.join(self.__filas__[0])} |  |   |  | {' | '.join(self.__filas__[1])} |
Fila 2   | {' | '.join(self.__filas__[2])} |  |   |  | {' | '.join(self.__filas__[3])} |
Fila 3   | {' | '.join(self.__filas__[4])} |  |   |  | {' | '.join(self.__filas__[5])} |
Fila 4   | {' | '.join(self.__filas__[6])} |  |   |  | {' | '.join(self.__filas__[7])} |
Fila 5   | {' | '.join(self.__filas__[8])} |  |   |  | {' | '.join(self.__filas__[9])} |
Fila 6   | v | v | v | v | v | v |  |   |  | v | v | v | v | v | v |
         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
Fila 6   | ^ | ^ | ^ | ^ | ^ | ^ |  |   |  | ^ | ^ | ^ | ^ | ^ | ^ |
Fila 5   | {' | '.join(self.__filas__[10])} |  |   |  | {' | '.join(self.__filas__[11])} |
Fila 4   | {' | '.join(self.__filas__[12])} |  |   |  | {' | '.join(self.__filas__[13])} |
Fila 3   | {' | '.join(self.__filas__[14])} |  |   |  | {' | '.join(self.__filas__[15])} |
Fila 2   | {' | '.join(self.__filas__[16])} |  |   |  | {' | '.join(self.__filas__[17])} |
Fila 1   | {' | '.join(self.__filas__[18])} |  |   |  | {' | '.join(self.__filas__[19])} |
         +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
           1   2   3   4   5   6    |BAR|    7   8   9  10  11  12
Leyenda:
- La columna central es la **BAR** (barra).
- Si un punto tiene más de 6 fichas, usa (7), (8), etc.
""")
    def put_checker(self, row, column):
        if column >= 13:
            if column <= 18:
                y = 5 - (column - 13)
                x = 1 + 2*(row-1)
            else:
                y = 5 - (column - 19)
                x = 0 + 2 * (row-1)
        else:
            if column <= 6:
                y = column - 1
                x = 20 - row * 2
            else:
                y = column - 7
                x = 19 - 2 * (row-1)
                
             

                    
        self.__filas__[x][y] = 'x'
#tab = Board()
#tab.put_checker(4, 10)
#tab.put_checker(3, 17)
#tab.put_checker(2, 21)
#tab.put_checker(1, 5)
#tab.show_board()

