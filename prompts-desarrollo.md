PROMPTS USADOS EN EL DESARROLLO
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