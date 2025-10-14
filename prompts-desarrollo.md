PROMPTS USADOS EN EL DESARROLLO
Todos los prompts de ChatGPT fueron hechos en el mismo chat, por lo que ya tenian contexto, por ejemplo, del lenguaje que he estado usando
- ChatGPT 5:
        -Input: "me podrías proporcionar el dibujo de una tabla de backgammon hecha con caracteres de teclado, que pueda imprimir en una consola?"
        -Output: 
                " ¡claro! aquí tienes un tablero de backgammon en ASCII puro (solo caracteres de teclado), listo para pegar en una consola e imprimir. Está vacío para que coloques tus fichas con X y O. Incluye 24 puntos numerados, la barra al centro y espacio para apilar hasta 6 fichas por punto (si hay más, puedes escribir un número entre paréntesis en la fila superior o inferior).
                                        TABLERO DE BACKGAMMON (vacío)
                        24  23  22  21  20  19   |BAR|   18  17  16  15  14  13
                        +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
                Fila 6   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 5   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 4   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 3   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 2   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 1   | v | v | v | v | v | v |  |   |  | v | v | v | v | v | v |
                        +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
                        +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
                Fila 1   | ^ | ^ | ^ | ^ | ^ | ^ |  |   |  | ^ | ^ | ^ | ^ | ^ | ^ |
                Fila 2   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 3   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 4   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 5   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                Fila 6   |   |   |   |   |   |   |  |   |  |   |   |   |   |   |   |
                        +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+
                        1   2   3   4   5   6    |BAR|    7   8   9  10  11  12

                Leyenda:
                - Números superiores (24→13) van de izquierda a derecha. Números inferiores (1→12) de izquierda a derecha.
                - `v` indica los puntos “hacia abajo” (triángulos superiores). `^` indica los puntos “hacia arriba” (triángulos inferiores).
                - Coloca fichas con `X` o `O` en las celdas de cada columna. Ej.: sustituir un espacio por `X`.
                - La columna central es la **BAR** (barra) para fichas comidas.
                - Si un punto tiene >6 fichas, usa algo como `(7)` en la fila 6 o 1 para indicar el total.
                Mini versión (más compacta)
                Si prefieres algo todavía más pequeño (sin filas para apilar), aquí va un marcador rápido:
                24 23 22 21 20 19 |BAR| 18 17 16 15 14 13
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                v  v  v  v  v  v  |    | v  v  v  v  v  v
                ^  ^  ^  ^  ^  ^  |    | ^  ^  ^  ^  ^  ^
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                -- -- -- -- -- -- |    | -- -- -- -- -- --
                1  2  3  4  5  6  |BAR| 7  8  9 10 11 12
                ¿Quieres que te lo entregue ya con la posición inicial puesta (X y O) para imprimir y jugar? "
        -Uso: Actualmente estoy utilizando la respuesta que me pudo dar la IA, principalmente el tablero hecho en ASCII (la version mas completa). Tambien estoy usando algunas de las leyendas que proporciono, si bien estas las voy a alterar seguramente con el desarrollo. Esto fue utilizado en core/board.py
- Github Copilot:
        - Input: "can you insert {c(x, y)} in each space in the backgammon board. for every space, x should be the column and y the row(1 to 5). the fstring should be between 2 spaces between each two bars"
        - Output: 
                    def show_board_with_coords(self):
        print("TABLERO DE BACKGAMMON")
        print("   24  23  22  21  20  19   |BAR|   18  17  16  15  14  13")
        print(" +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        for y in range(1, 6):
            left = '  '.join([f"{{c({x},{y})}}" for x in range(24, 18, -1)])
            right = '  '.join([f"{{c({x},{y})}}" for x in range(18, 12, -1)])
            print(f"Fila {y}   | {left} |  |   |  | {right} |")
        print(" +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print(" +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        for y in range(5, 0, -1):
            left = '  '.join([f"{{c({x},{y})}}" for x in range(1, 7)])
            right = '  '.join([f"{{c({x},{y})}}" for x in range(7, 13)])
            print(f"Fila {y}   | {left} |  |   |  | {right} |")
        print(" +---+---+---+---+---+---+  |   |  +---+---+---+---+---+---+")
        print("   1   2   3   4   5   6    |BAR|    7   8   9  10  11  12")
        - Uso: Le pedi al asistente integrado de github en VS Code que ingrese las coordenadas de cada lugar del tablero al tablero que tenia diseñado para imprimir. Decidio hacer otro método para esto. Saque de ese método la logica y la implementé en el método que ya existía. Fue utilizado en core/board.py. 
- ChatGPT 5:
        - Input: 
                "tengo un bucle for, que itera sobre una lista que contiene diccionarios. El bucle verifica si el diccionario x cumple determinada condicion y, si es asi, debe agregar el indice de ese diccionario a una lista. Para esto uso list.index(x). El problema es que este metodo me devuelve el indice de el primer diccionario que encuentre igual a x, no necesariamente sobre el que estoy iterando. De que otra forma puedo lograr esto?"
        - Output:
                "¡Exacto! Lo que notaste es totalmente cierto 👌.
                🔎 Qué pasa con list.index(x)
                list.index(x) siempre devuelve el índice de la primera coincidencia en la lista, no el de la iteración actual.
                Como tus diccionarios pueden repetirse (o al menos compararse iguales), te devuelve siempre el primero.
                ✅ La forma correcta: usar enumerate
                enumerate te da tanto el índice como el elemento mientras iterás:
                lista = [
                {"a": 1, "b": 2},
                {"a": 3, "b": 4},
                {"a": 1, "b": 5},
                ]

                indices = []
                for i, dic in enumerate(lista):
                if dic["a"] == 1:   # condición de ejemplo
                        indices.append(i)

                print(indices)  # [0, 2]
                De esta forma i es siempre el índice real del diccionario que estás recorriendo.
                🔧 Si querés hacerlo en una sola línea (list comprehension):
                indices = [i for i, dic in enumerate(lista) if dic["a"] == 1]
                👉 Resumen: no uses .index(x) mientras iterás. Usá enumerate para tener siempre el índice actual.
                ¿Querés que te muestre cómo aplicar esto directamente sobre tu caso del tablero de backgammon (las columnas con checker y quantity)?"
        - Uso: La informacion que GPT me brindo fue implementada en un loop del metodo turn_normal() de la clase Game
- ChatGPT 5:
        - Input:
                "Para un if, si tengo dos condiciones distintas que si se cumplen resultan en lo mismo, que puedo hacer en vez de usar or, ya que no quiero pasar los 100 caracteres por linea?"
        - Output:
                "¡Muy buena! 👌 El problema no es el or, sino que tu condición se hace larga y poco legible. Hay varias formas de mantener el código claro sin romper el límite de 100 caracteres por línea.
                🔹 1. Usar paréntesis y dividir en varias líneas
                Python permite dividir expresiones lógicas con () y saltos de línea:
                if (
                condicion_larga_1
                or condicion_larga_2
                ):
                hacer_algo()
                Esto es totalmente válido y PEP 8-friendly.
                🔹 2. Guardar condiciones en variables con nombre claro
                Así mejoras legibilidad y evitas repetir:
                es_valido = condicion_larga_1 or condicion_larga_2
                if es_valido:
                hacer_algo()
                🔹 3. Usar in cuando aplican varias opciones
                En lugar de x == "a" or x == "b":
                if x in ("a", "b"):
                hacer_algo()
                Esto es más corto y legible.
                🔹 4. Factorizar en una función auxiliar
                Si la lógica es muy repetitiva, la escondés detrás de una función descriptiva:
                def es_jugada_valida(x):
                return condicion_larga_1 or condicion_larga_2

                if es_jugada_valida(jugada):
                hacer_algo()
                ✅ Resumiendo:
                Usá paréntesis y salto de línea si solo es cuestión de ancho.
                Si querés más legibilidad, factorizar en variables, sets o funciones auxiliares."
        - Uso: La informacion me sirve y sera implementada para dejar codigo mas limpio.
- ChatGPT 5:
        - Input: 
                "como puedo remover varios indices de una lista de otra?"
        - Output:
                "Muy buena 👌. Tenés varias formas de hacerlo en Python. La idea es: tenés una lista L y otra lista indices con las posiciones a eliminar.
                🔹 1. Con list comprehension (lo más limpio)
                L = ["a", "b", "c", "d", "e"]
                indices = [1, 3]   # quiero borrar posiciones 1 y 3 → "b" y "d"

                result = [x for i, x in enumerate(L) if i not in indices]
                print(result)  # ['a', 'c', 'e']
                🔹 2. Eliminando en orden inverso
                Si sí o sí querés modificar la lista original, borrá desde el índice más grande hacia abajo (para que no cambien las posiciones de los que faltan):
                L = ["a", "b", "c", "d", "e"]
                indices = [1, 3]

                for i in sorted(indices, reverse=True):
                L.pop(i)

                print(L)  # ['a', 'c', 'e']
                🔹 3. Usando numpy (si trabajás con arrays numéricos)
                import numpy as np

                arr = np.array([10, 20, 30, 40, 50])
                indices = [1, 3]

                result = np.delete(arr, indices)
                print(result)  # [10 30 50]
                ✅ En general, si lo que querés es construir una nueva lista filtrada, la opción con list comprehension (1) es la más clara y Pythonic.
                Si necesitás modificar la lista en el lugar, usá la opción (2) borrando en orden inverso.
                👉 ¿Querés que te arme un ejemplo aplicado directamente a tu caso del backgammon, donde required_dice tiene que eliminar varias posiciones a la vez?"
        - Uso: Use la segunda sugerencia, en el metodo turn_finalizar_fichas() en game.py
- Gemini 2.5 Pro:
        - Input: Entonces, como hago una función que detecte si un punto dado esta dentro de un triangulo dado?
        - Output:
                ¡Claro! Te explico cómo se construye, paso a paso, la función que has seleccionado. El método que utiliza es el más robusto y común en gráficos por computadora, conocido como coordenadas baricéntricas.

                La idea es tratar tu punto P como una "mezcla" de los tres vértices del triángulo (A, B y C). Si la mezcla requiere cantidades positivas de los tres vértices, entonces el punto está dentro.

                Aquí tienes los pasos para crear la función:

                Paso 1: Definir las Entradas de la Función

                La función necesita dos cosas:

                El punto que quieres comprobar, por ejemplo pt = (px, py).

                Los tres vértices que definen el triángulo, por ejemplo triangle = [A, B, C], donde A, B y C son tuplas de coordenadas como (ax, ay).

                Python
                def is_point_in_triangle(pt, triangle):
                # ... aquí irá la lógica ...
                Paso 2: La Lógica Matemática (El Corazón de la Función)

                Este es el cálculo central. Se basa en resolver un pequeño sistema de ecuaciones de álgebra lineal para encontrar unos "pesos" (s y t).

                Desglosar las coordenadas: Primero, para que sea más fácil de leer, asignas todas las coordenadas x e y a variables separadas.

                Python
                (p_x, p_y) = pt
                (v1_x, v1_y) = triangle[0] # Vértice A
                (v2_x, v2_y) = triangle[1] # Vértice B
                (v3_x, v3_y) = triangle[2] # Vértice C
                Calcular el Denominador (d): Se calcula un valor d que es proporcional al área del triángulo. Este valor es crucial porque si es 0, significa que los tres vértices están en una línea recta y no forman un triángulo real.

                Python
                d = (v2_y - v3_y) * (v1_x - v3_x) + (v3_x - v2_x) * (v1_y - v3_y)
                if d == 0:
                return False # No es un triángulo, así que el punto no puede estar dentro
                Calcular los Pesos (s y t): Luego, usas dos fórmulas similares para calcular los dos pesos principales. Estos pesos te dicen dónde está el punto P en relación con los lados del triángulo.

                Python
                s = (v2_y - v3_y) * (p_x - v3_x) + (v3_x - v2_x) * (p_y - v3_y)
                t = (v3_y - v1_y) * (p_x - v3_x) + (v1_x - v3_x) * (p_y - v3_y)
                Normalizar los Pesos: Finalmente, divides s y t por el denominador d que calculaste antes. Esto los pone en la escala correcta (de 0 a 1).

                Python
                s /= d
                t /= d
                Paso 3: La Comprobación Final

                Esta es la parte más fácil e intuitiva. Un punto está dentro del triángulo si y solo si se cumplen estas tres condiciones:

                El primer peso s es positivo (s > 0).

                El segundo peso t es positivo (t > 0).

                La suma de ambos pesos es menor que 1 (s + t < 1). Esta última condición asegura implícitamente que el tercer peso también es positivo.

                Python
                return s > 0 and t > 0 and (s + t) < 1
        - Uso: Esta funcion es clave para detectar cuanto el jugador toca en un triangulo del tablero para mover una ficha. La voy a implementar en la clase HitMap.