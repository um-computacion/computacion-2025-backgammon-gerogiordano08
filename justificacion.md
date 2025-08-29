### Clase Board

La clase board consta de un atributo __columnas__(lista) que contiene 24 diccionarios que a su vez contienen cual ficha ocupa esa columna y que cantidad de fichas tiene. 
El método checker(column, level) es basicamente un espacio del tablero. Cada espacio del tablero tiene este método que consulta que ficha esta en esa columna y siguiendo una simple lógica, si la cantidad de fichas en esa columna supera el 'nivel' de ese espacio, el método imprime la ficha. Si la cantidad de fichas supera los 5 espacios, el tablero muestra el número de fichas en el nivel 5. 
El método show_board() imprime varios strings que juntos representan correctamente el tablero. para mostrar las fichas de manera adecuada uso un loop para que cada espacio del tablero tenga una funcion checker() junto con su coordenada.  
El método add_checker(column) simplemente aumenta la cantidad de fichas en una columna por 1 unidad. 
El método remove_checker(column) resta una ficha de la cantidad de una columna. 
El método put_checker(column, checker) agrega una ficha a una columna donde previamente no habia ninguna, por lo que hay que darle como argumento la ficha a agregar. 