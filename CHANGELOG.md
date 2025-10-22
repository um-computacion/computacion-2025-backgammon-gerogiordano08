# Changelog

Todos los cambios notables del proyecto van a ser documentados en este changelog.

## [21/10/2025]

### Agregado
- Clase CLI
    - metodo do_interfaz(), que inicia la interfaz grafica
- Clase Game
    - Metodo no_available_moves(), que verifica si no hay movimientos disponibles.
- Clase UI
    - Se avanzo con la logica de turno para la interfaz grafica.
- Clase Controller
    - Metodo change_turn() que cambia el contador de turno.
## [20/10/2025] commit 3

### Agregado
- Clase Controller
    - Creado metodo que enseña una flecha en un triangulo dado, con una orientacion dada.
## [20/10/2025] commit 2

### Agregado
- Clase Controller
    - Creada la logica que muestra los dados y el nombre del jugador cuyo turno se esta jugando.
    - Creado el metodo que muestra el mensaje de victoria.

## [20/10/2025] commit 1

### Alterado
- El contador que marca de quien es el turno ahora es manejado por Game y no por CLI, para poder conectar de manera mas limpia el controlador de graficos con la logica del juego.

## [18/10/2025]

### Agregado
- Clase Controller 
    - Cuando hay mas de 4 fichas en una casilla, muestra solo cuatro junto con el numero en la cuarta casilla

## [17/10/2025]
### Agregado

- Se creo la clase controller que controla la logica del juego para enviarla a la interfaz grafica.

## [14/10/2025]

### Agregado
- Se creo la clase HitMap que define la logica necesaria para detectar donde clickea el usuario.

## [12/10/2025]

### Agregado

- Fue creado todo lo que debe ser renderizado todo el tiempo en el juego, como los triangulos o los margenes.

## [07/10/2025] commit 3

### Agregado
- Fueron creados los assets de caras de dados y fichas.

## [07/10/2025] commit 2

## Agregado
- Para comenzar con la implementacion de la interfaz grafica se creo la clase UI que por ahora inicializa pygame.
## [07/10/2025] commit 1

## Alterado
- Algunos tests habian quedado rotos. Fueron arreglados y se llego al 90% de coverage.

## [06/10/2025] commit 2

### Alterado
- Se corrigieron algunos errores no solo de dinamicas, sino de logica del juego.

## [06/10/2025] commit 1

### Agregado

- Se configuro la excepcion InputError que maneja los casos en los cuales se pide un entero y no se ingresa uno.

## [02/10/2025] commit 2

### Agregado

- Se agrego a cada clase que dependia de redis un parametro 'testing' que no usa la base de datos, porque se producian errores con los tests.
## [02/10/2025] commit 1

### Agregado

- Guardado de partida con redis. Funciona correctamente.

## [01/10/2025]

### Agregado

- Terminados los test de clase Game.

### Alterado

- cli.py puntuacion pylint 10/10

## [27/09/2025] commit 2

## Agregado
- En la clase Game:
    - Terminado el método turn_finalizar_fichas()
- Se termino el desarrollo de la logica del juego. Falta formatear y algunos detalles, pero actualmente el juego backgammon funciona correctamente respentando las reglas del juego
## [27/09/2025] commit 1

## Agregado
- En la clase Game:
    - Casi terminado el método turn_finalizar_fichas()

## [25/09/2025] commit 2

## Agregado
- En la clase Game:
    - Se escribio un draft del método turn_finalizar_fichas() para manejar la logica de finalizacion de fichas con datos correspondientes.
    
## [25/09/2025] commit 1

### Agregado

- Tests para CLI.

- Algunas funciones de la CLI, como advertencia al sobreescribir juego. 
### Alterado

- El juego ya es estable y se puede jugar normalmente. 

## [22/09/2025] commit 3

### Alterado

- Se continuo arreglando errores de game.py, el juego es casi completamente funcional, quedan pequeños errores que, de cualquier manera, no permiten que se pueda jugar correctamente.

## [22/09/2025] commit 2

### Alterado

- Se arreglaron errores de game.py

## [22/09/2025] commit 1

### Alterado

- Se progresó en la corrección de game.py

## [19/09/2025]

### Alterado
- Usando pylint, se modifico el archivo game.py, para cumplir con los estandares. Todavia no esta completo.
## [18/09/2025]

### Alterado
- - Usando pylint, se modificaron los archivos board.py para llegar a un puntajen de 10/10.

## [17/09/2025] commit 3

### Alterado
- Usando pylint, se modificaron los archivos checker.py, player.py y dice.py para llegar a un puntajen de 10/10.
## [17/09/2025] commit 2
- Esta listo el archivo main.py. A partir de ahora se puede correr el juego usando python main.py desde el directorio del programa
## [17/09/2025] commit 1

### Agragado
- En la clase CLI se completo el metodo do_reglas() para que el jugador pueda consultar las reglas durante la partida.

## [16/09/2025] commit 3

### Agregado
- Se termino la primera version de la CLI

## [16/09/2025] commit 2

### Agregado
- Creado el archivo cli.py, junto con una version basica que hereda cmd e incluye comandos claves.

## [16/09/2025] commit 1

### Alterado
- Se escribio la justificacion hasta la fecha en justificacion.md

## [15/09/2025] commit 2

### Agregado
- Se implementó coverage, con sus archivos necesarios
- Se implementó pylint, con sus archivos necesarios

### Alterado
- Se agregaron requerimentos en requirements.txt
## [15/09/2025] commit 1

### Agregado
- En la clase Game
    - Se agrega el setter set_dice()

### Alterado
- En la clase Game
    - Se modifica el método turn(), que tenia varios errores.
## [09/09/2025]

### Agregado
- En la clase Game
    - Se termina el desarrollo del método turn(player), logica de turno. 
    - Se agrega el test para el método finish_checker(col, player). 
- En la clase Player
    - Ahora todo objeto Player tiene atributo __bar_index__, que describe el indice de la barra para ese jugador especifico. 
- En la clase Checker
    - get_type()

### Alterado
- En la clase Dice
    - Se cambió la lógica del getter get_dice(). Para empezar se cambia el nombre, ahora get_dice_results(). Además, si salen dobles, el getter devuelve esa cantidad cuatro veces como tupla. 
    
## [08/09/2025]

### Agregado
- En la clase Game
    - Se agrego el método finish_checker(col, player) para poder completar la finalizacion de una ficha si es permitido. 
    - Se comenzo con el desarrollo del método turn(player) que maneja la logica de un turno dentro del juego. 

### Alterado
- En la clase Game
    - Se altero el método available_move(fro, to, player), que ahora es mas completo, verifica mas condiciones. 

## [04/09/2025] 

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
        