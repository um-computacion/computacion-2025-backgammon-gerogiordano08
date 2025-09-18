-ChatGPT 5: 
    - Input: "por que pylint me dice missing module docstring en linea 1,  si claramente esta ahi?" (se adjuntó imagen del archivo player.py)
    - Output: 
    "Muy buena observación 👌. Lo que tenés en tu código es un docstring de clase, no un docstring de módulo.
    Diferencia
    Docstring de módulo: es el que va en la primera línea del archivo, antes de cualquier import o definición de clase/función. Sirve para describir el archivo completo.
    Docstring de clase: es el que pusiste justo después de class Player:. Ese está bien, pero no cumple la “regla” de pylint sobre el módulo."
    -Uso: La consulta me vino util para conocer que se debe agregar un docstring tambien a cada archivo en sí.