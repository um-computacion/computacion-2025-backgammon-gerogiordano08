# **JUSTIFICACIÓN**  
## **Justificación** del diseño general  
## Justificación de las clases elegidas  
El diseño del juego, hasta ahora, usa las clases propuestas por la catedra, que son: Board, Checker, Player, Dice y Game.  Me pareció una distribución correcta.  
### Board  
La clase Board comprende todas las responsabilidades del tablero, principalmente definirlo gráficamente para la consola. Además, agregar o quitar fichas en donde sea necesario, y claramente lograr representar una lista que guarde qué ficha está en qué lugar, de manera gráfica. El único atributo que tiene esta clase es __columnas__. Es una lista con 26 diccionarios dentro. Cada diccionario representa una columna del tablero. Y dentro de cada diccionario hay ‘atributos’ (si es que los podemos llamar así) de cada columna. Para los primeros 24 dic, que representan las 24 columnas o ‘triángulos’ del tablero, podemos ver las keys ‘checker’ (string con la ficha que ocupa ese lugar) y ‘quantity’ (int que representa la cantidad de fichas). Los últimos 2 dic representan las barras de los jugadores, donde se guardan los ‘atributos’ de las barras de cada jugador. En este caso, la primera barra siempre pertenece al jugador uno (x) y la segunda al jugador dos (o). Además, tienen una key ‘bar’ con valor bool que más que nada sirve para distinguirlos de los primeros 24 diccionarios.  
### Checker  
La clase Checker es un objeto bastante estático. Dependiendo del tipo (1 o 2) que le demos, va a devolver el símbolo correspondiente. Tiene los atributos __type__: int, __symbol_1__: str y __symbol_2__: str.  
### Player  
La clase player es más importante porque define a cada uno de los dos jugadores, y se usa, por ejemplo, en los métodos de turnos en la clase Game, de manera clave para definir a qué lado van las fichas, qué barra usar, etc. Tiene los atributos __name__: str, __checker_type__: int y __bar_index__: int. Este último define cuál es el índice de la barra del jugador en el atributo __columnas__ de Board.  
### Dice  
Dice también es interesante porque simula un par de dados, además cumpliendo la regla de dobles directamente en la clase. Sus atributos son __die_1__:int y __die_2__: int. El getter de esta clase devuelve cuatro dados en el caso de que los dos dados sean iguales en valor.  
### Game  
La clase Game maneja la lógica del juego, incluido el método turn y además todos los métodos que verifican condiciones que se deben ir cumpliendo o no para lograr determinadas acciones. Como atributo tiene objetos de todas las clases anteriormente mencionadas. __board__: Board, __dice__: Dice, __checker_1__: Checker, __checker_2__: Checker, __player_1__: Player, __player_2__: Player.  
  
## Estrategias de testes  
Para todas las clases, elegí hacer los tests de todos sus métodos, a excepción de los getters y setters, dada su simplicidad.  
  
