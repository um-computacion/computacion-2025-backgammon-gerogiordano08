# Changelog

Todos los cambios notables del proyecto van a ser documentados en este changelog. 

## [30/08/2025]

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
        