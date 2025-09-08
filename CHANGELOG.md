# Changelog

Todos los cambios notables del proyecto van a ser documentados en este changelog. 

## [31/08/2025] 

### Agregado
- En la clase 'Game'
    - Fue creado el método check_bar(player) que verifica si hay alguna ficha en la barra de algun jugador. 
    - Ademas los métodos de la clase Board tambien fueron agregados a la clase Game para seguir los principios de encapsulacion. 
    - Fueron documentadas los métodos con docstrings
    - Fueron agregados 'getters'
    - Fueron agregados tests. 

### Alterado
- En la clase Board
    - Se elimino el atributo __barra__, ahora las fichas de la barra se encuentran en las columnas [24] y [25] de el atributo __columnas__ para implementar de manera mas practica las funciones que tengan que ver con la barra. 


## [31/08/2025] commit 3

### Agregado
- En la clase 'Game'
    - Fueron creados los métodos:
        - can_finish_checkers_p1() y can_finish_checkers_p2() que verifican si cada jugador puede empezar a sacas sus fichas del tablero. 
        - win_condition(player) que verifica si el jugador indicado en el argumento (1 o 2) ha ganado. 
    - Tests para estos metodos
### Alterado
Se modifico la orientacion de las columnas del tablero, que seguia una numeracion antihoraria, cuando en realidad debe ser horaria. Se adaptaron todos los metodos y tests que se habian creado teniendo en cuenta la orientacion antihoraria. 
## [31/08/2025] commit 2

### Agregado
- En la clase 'Game'
    - Fueron creados los métodos:
        - move_checker(fro, to), que de acuerdo a los argumentos, mueve una ficha de una columna a otra. No toma en cuenta las condiciones necesarias para hacer un movimiento valido. 
        - roll_dice(), toma el método roll_dice() de la clase 'Dice' para conseguir dos numeros aleatorios entre 1 y 6. 
        - available_move(fro, to) verifica que se cumplan las condiciones necesarias para que un movimiento de ficha sea valido de acorde a las reglas del juego. 
    - Tests para estos métodos. 
## [31/08/2025] commit 1

### Agregado
- Fue creada la clase 'Game'
    - Atributos:
        - __board__, es un objeto de clase 'Board'. 
        - __dice__, es un objeto de clase 'Dice'. 
        - __checker_1__, es un objeto de clase 'Checker'. 
        - __checker_2__, es un objeto de clase 'Checker'. 
        - __player_1__, es un objeto de clase 'Player'. 
        - __player_2__, es un objeto de clase 'Player'. 
    - Métodos:
        - prepare_board(), deja las 30 fichas en sus lugares correspondientes para iniciar el juego. 
    - Tests para prepare_board()
- Método clear_board() que limpia los objetos Board, dejando 0 fichas en cada columna. Tests para este método. 

### Alterado
- Los métodos add_checker(column, quan), remove_checker(column, quan) y put_checker(column, quan) ahora aceptan el argumento quan para determinar el numero de fichas a agregar o restar, con un valor por defecto de 1. 
## [30/08/2025] commit 3

### Agregado
- Fue creada la clase 'Player'
    - Atributos:
        - __name__, corresponde al nombre que el jugador quiera usar. 
        - __checker_type__, corresponde al tipo de ficha que le toca a ese jugador (1, 2)
## [30/08/2025] commit 2

### Agregado
- Fue creada la clase 'Dice':
    - Atributos:
        - __die_1__, corresponde al valor del primer dado. 
        - __die_2__, corresponde al valor del segundo dado. 
    - Métodos:
        - roll_dice() le da un valor al azar entre 1 y 6 a cada uno de los dados. 
        - clear_dice() le da el valor 0 a ambos dados. 
    - Se configuraron los tests para todos los métodos de la clase. 

## [30/08/2025] commit 1

### Agregado
- Fue creada la clase 'Checker'
    - Atributos:
        - __type__, que ingresa como argumento de la clase necesario para inicializarse. Diferencia si es una ficha 'x' o una ficha 'o'. 
        - __symbol_1__, es el simbolo 'x' correspondiente al tipo 1. 
        - __symbol_2__, es el simbolo 'o' correspondiente al tipo 2. 
    - Métodos:
        - get_symbol() devuelve el simbolo correspondiente al tipo de ficha ('x', 'o'). 
    - Se configuraron los tests para todos los métodos de la clase. 

## [29/08/2025]

### Agregado
- En la clase 'Board'
    - Se configuraron los tests para todos los métodos de la clase. 
    - Se documentaron todos los docstrings de todos los tests y todos los métodos de la clase. 

## [28/08/2025]

### Agregado
- En la clase 'Board' 
    - El atributo __columnas__ que consiste de una lista de 24 diccionarios (columnas del tablero) que dentro incluyen que ficha y cuantas fichas van en esa columna. 
    - El método checker(column, level) que interpreta a partir de __columnas__ si en la coordenada brindada debe ir una u otra ficha, o ninguna. 
    - Los métodos add_checker(column) y remove_checker(column) que restan en una unidad la cantidad de fichas que se encuentran en dicha columna. 
### Alterado
- La logica que seguia la clase 'Board' fue alterada. 
    - Se reemplazo el atributo __filas__ por __columnas__ para asi tener un acercamiento mas ordenado, no solo para el tablero ASCII sino tambien para la futura implementacion de graficos Pygame
    - El método show_board() ahora usa loops para insertar dentro del tablero la nueva funcion checker(x, y) que imprime la ficha adecuada de acuerdo con la lista de columnas. 
    - El método put_checker(row, column, checker) fue reemplazado por put_checker(column, checker) que ahora agrega a una columna una nueva ficha en una sola unidad. Debe ser usado solo para columnas en las que anteriormente no habia ninguna ficha. 

## [26/08/2025]

### Agregado
- Fue creada la clase 'Board'.     
    - Atributos:
        - __filas__, lista que consiste de las 20 filas (listas) que podemos ver en un tablero graficamente. 
        - __barra__, que comprende las fichas que roban los jugadores de acuerdo al juego.
    - Métodos:
        - show_board(), que usa las filas para graficar el tablero en la consola.
        -put_checker(row, column, checker), que sabe donde poner la ficha en el atributo __filas__ de acuerdo a la fila y columna que le sea proporcionada. 
        