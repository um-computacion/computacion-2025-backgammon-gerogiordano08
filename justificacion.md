# **JUSTIFICACIÓN**  
## Core y lógica central
core constituye el Modelo de la aplicación. Su objetivo es encapsular todo el estado, las reglas y la lógica fundamental del juego de Backgammon, independientemente de cualquier interfaz de usuario (ya sea gráfica o de consola).

El diseño se centra en la clase Game actúa como el punto de entrada principal y orquestador. Esta clase coordina las interacciones entre los componentes de datos (Board, Player, Checker) y los componentes de lógica (Dice).

### Justificación de las clases elegidas  
El diseño del juego, hasta ahora, usa las clases propuestas por la catedra, que son: Board, Checker, Player, Dice y Game.  Me pareció una distribución correcta.  
#### Board  
La clase Board comprende todas las responsabilidades del tablero, principalmente definirlo gráficamente para la consola. Además, agregar o quitar fichas en donde sea necesario, y claramente lograr representar una lista que guarde qué ficha está en qué lugar, de manera gráfica. El único atributo que tiene esta clase es __columnas__. Es una lista con 26 diccionarios dentro. Cada diccionario representa una columna del tablero. Y dentro de cada diccionario hay ‘atributos’ (si es que los podemos llamar así) de cada columna. Para los primeros 24 dic, que representan las 24 columnas o ‘triángulos’ del tablero, podemos ver las keys ‘checker’ (string con la ficha que ocupa ese lugar) y ‘quantity’ (int que representa la cantidad de fichas). Los últimos 2 dic representan las barras de los jugadores, donde se guardan los ‘atributos’ de las barras de cada jugador. En este caso, la primera barra siempre pertenece al jugador uno (x) y la segunda al jugador dos (o). Además, tienen una key ‘bar’ con valor bool que más que nada sirve para distinguirlos de los primeros 24 diccionarios.  
#### Checker  
La clase Checker es un objeto bastante estático. Dependiendo del tipo (1 o 2) que le demos, va a devolver el símbolo correspondiente. Tiene los atributos __type__: int, __symbol_1__: str y __symbol_2__: str.  
#### Player  
La clase player es más importante porque define a cada uno de los dos jugadores, y se usa, por ejemplo, en los métodos de turnos en la clase Game, de manera clave para definir a qué lado van las fichas, qué barra usar, etc. Tiene los atributos __name__: str, __checker_type__: int y __bar_index__: int. Este último define cuál es el índice de la barra del jugador en el atributo __columnas__ de Board.  
#### Dice  
Dice también es interesante porque simula un par de dados, además cumpliendo la regla de dobles directamente en la clase. Sus atributos son __die_1__:int y __die_2__: int. El getter de esta clase devuelve cuatro dados en el caso de que los dos dados sean iguales en valor.  
#### Game  
La clase Game maneja la lógica del juego, incluido el método turn y además todos los métodos que verifican condiciones que se deben ir cumpliendo o no para lograr determinadas acciones. Como atributo tiene objetos de todas las clases anteriormente mencionadas. __board__: Board, __dice__: Dice, __checker_1__: Checker, __checker_2__: Checker, __player_1__: Player, __player_2__: Player.  
#### Redis Store
Es la capa de acceso a datos. Se eligió para lograr la comunicación con la base de datos Redis. Se encarga de serializar (a JSON) y deserializar el estado de las columnas del juego.

### Decisiones de diseño relevantes
1. Modelo Acoplado a la Vista (Consola): Una decision importante fue mezclar la lógica de UI (print/input) dentro de los métodos del Game (ej. turn_normal, turn_fichas_barra). Hizo mas facil el desarrollo de la CLI, pero tarde me di cuenta que complicaria la implementacion de la interfaz grafica.

Modelo Acoplado a la base de datos (Redis): La segunda decisión más importante fue que las clases Game, Board, y Player instancian directamente RedisStore. Esto acopla fuertemente el modelo a una implementación de base de datos específica (Redis).

Lógica de Turnos Secuencial: El método Game.turn() implementa un bucle for que itera sobre la cantidad de dados. Dentro de este bucle, se consulta el estado (has_checkers_in_bar) y se llama al sub-método apropiado (turn_fichas_barra, turn_normal, etc.). Este diseño secuencial funciona perfectamente para una CLI, pero es incompatible con una UI basada en eventos (como Pygame). Por eso se tuvo que desarrollar adaptadores en el controlador de la interfaz grafica.
### Estrategias de tests  
Para todas las clases, elegí hacer los tests de todos sus métodos, a excepción de los getters y setters, dada su simplicidad. Ademas para algunos métodos mas complejos, varios tests que testean distintos caminos.

## Excepciones
Como excepciones solo encontramos InputError, que se usa para manejar los casos en los que el usuario no ingresa un entero, cuando se le pide el numero de columna o de dado.

## Interfaz Grafica
El diseño general de la aplicación sigue una arquitectura inspirada en el patrón Model-View-Controller (MVC), adaptado a las características de Pygame.

Model: Representado por el core/ (Game, Board, Player, Dice). Estas clases encapsulan las reglas, el estado y la lógica del Backgammon, sin tener conocimiento de la interfaz gráfica.

View: Representada principalmente por la clase UI y los métodos draw del Controller. Se encarga de inicializar la ventana, dibujar el estado actual del juego (tablero, fichas, dados) en la pantalla (__screen__) y gestionar el bucle principal.

Controller: Representado por la clase Controller. Actúa como el intermediario principal. Recibe eventos de la Vista (clics del usuario), los traduce a acciones, actualiza el Modelo (Game) y gestiona el estado interno de la UI (qué ficha se seleccionó, qué movimientos son posibles).

El flujo de ejecución es el siguiente:

1- La UI inicia el bucle y dibuja el estado inicial.

2- El usuario hace clic. El bucle de UI detecta el MOUSEBUTTONDOWN.

3- La UI pasa la posición del clic al Controller (handle_click).

4- El Controller usa HitMap para identificar qué se clickeó.

5- El Controller actualiza su estado interno y la lógica del Game a través de métodos como movement y change_turn.

6- En el siguiente fotograma del bucle, la UI le pide al Controller que dibuje (draw) el nuevo estado del Modelo.

### Clases elegidas
Las clases principales de la interfaz gráfica se eligieron para separar responsabilidades clave:

UI:

Responsabilidad: Punto de entrada. Su única responsabilidad es manejar la instancia de Pygame: inicializar la ventana (__screen__), el reloj (__clock__), cargar el fondo estático, y ejecutar el bucle principal (run). Delega toda la lógica de juego y dibujado al Controller.

Controller:

Responsabilidad: Es el cerebro de la interfaz. Fue elegida para centralizar toda la lógica interactiva entre la interfaz y el modelo del juego. Sus responsabilidades incluyen:

Manejo de Estado de UI: Almacenar qué ficha se seleccionó (fro), qué destinos son válidos (destinos), y qué dados se han usado (useddice).

Manejo de Eventos: Traducir los clicks (handle_click) en acciones de juego.

Lógica de Dibujado: Contener todos los métodos draw que saben cómo renderizar los elementos dinámicos del juego (fichas, dados, flechas, mensajes).

Gestión de Lógica: Adaptar la lógica del core (como check_state, destinos_disponibles) a un entorno basado en eventos.

HitMap:

Responsabilidad: Es una clase especializada. Su única responsabilidad es la traducción de coordenadas. Recibe una tupla (x, y) de un click y devuelve qué elemento del juego fue clickeado. Se creó para aislar esta lógica matemática compleja (geometría de polígonos) y mantener el Controller limpio.

### Atributos
#### UI:

__screen__: Atributo principal de Pygame; es la superficie de la ventana donde se dibuja todo.

__board_background__: Una pygame.Surface que almacena el tablero estático pre-renderizado.

__game__, __controller__, __hitmap__: Instancias de las clases principales.

#### Controller:

__game__: Una referencia al Modelo (Game) para poder leer su estado (ej. get_board()) y modificarlo (ej. movement()).

__assets__: Una tupla que almacena todas las imágenes (PNGs) y dados cargados en memoria (pygame.Surface). Se justifica para evitar la carga de archivos desde el disco en cada fotograma, lo cual sería muy lento.

__fonts__: Almacena las instancias pygame.font.Font cargadas, por la misma razón de rendimiento que __assets__.

__fro_to_destinos_dicecount_useddice_turntype_msg__: Este es el atributo de estado del Controller. Es una lista que funciona como un log de estado. Almacena:

[0] (fro): La ficha de origen seleccionada.

[1] (to): El destino de la ficha.

[2] (destinos): La lista de movimientos válidos desde fro.

[3] (dicecount): Contador de dados ya utilizados, para tener en cuenta cuando pasar al proximo turno.

[4] (useddice): Qué dados ya se usaron en este turno.

[5] (turntype): El estado actual del turno ('normal', 'bar', 'win1', 'win2').

[6] (msg): El mensaje de error/estado a mostrar.

__msgduration_msgstart__: Atributos de estado ([int, int]) necesarios para implementar el temporizador de mensajes en pantalla.

### Decisiones de diseño relevantes

1. Optimización del Fondo Estático: En app.py, el método background() dibuja todos los polígonos, líneas y colores del tablero una sola vez en una Surface al inicio. El bucle run nada mas "blitea" esta imagen en cada fotograma, en lugar de redibujar todos los polígonos 60 veces por segundo. Esta es la decisión de diseño más importante para garantizar el alto rendimiento del juego.

2. Delegación del Dibujado: La UI (app.py) no sabe cómo dibujar una ficha. Simplemente llama a self.__controller__.draw(...). Es el Controller quien contiene la lógica para iterar sobre el tablero, traducir posiciones (get_checker_position) y "blitear" los __assets__ correctos.

3. Abstracción de Clics (HitMap): En lugar de tener una lógica if/elif masiva en handle_click para comprobar coordenadas (x, y), se abstrajo toda esa matemática en HitMap. El Controller solo pregunta: clicked_info = hitmap.hit_test(click_pos). Esto hace el handle_click mucho más legible.

4. Refactorización de Lógica del core: El core original (visto en game.py) estaba diseñado para una CLI (con print/input). Esto es incompatible con una UI de eventos. Por lo tanto, se tomó la decisión de reescribir/adaptar la lógica de turnos (ej. destinos_disponibles, check_state, movement) dentro del Controller para que funcionara de forma reactiva (respondiendo a clics) en lugar de secuencial (esperando input).

5. Manejo de Estado Explícito: Se utiliza la lista __fro_to_...__ como la fuente para el estado de la UI. Todos los métodos (handle_click, check_state, change_turn) leen y escriben en esta lista. 