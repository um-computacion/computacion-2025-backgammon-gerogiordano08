# Backgammon
## Computacion 2025
### Por Gerónimo Giordano

## Descripción
Ahora puedes jugar al backgammon con mi aplicacion, completamente diseñada por mi. Si antes quieres leer las reglas, te dejo el link de las reglas que use para diseñar el juego. [Reglas](https://www.ludoteka.com/clasika/backgammon-es.html).

## Ayuda para iniciar el juego
Antes que nada debes descargar todas las dependencias o requisitos necesarios (Habiendo ya instalado python en tu computadora). Esto lo puedes hacer con el comando `pip install -r requirements.txt`
Para iniciar el juego debes ingresar en el repositorio con la terminal de tu computadora e ingresar el comando  `python3 main.py`. Asi se va a abrir la linea de comando del juego, con varias opciones que puedes consultar ingresando el comando `ayuda`. Puedes, por ejemplo, ver las reglas, iniciar el juego o salir. Es muy importante que el comando `start` solamente inicia el juego. Ya iniciado debes ingresar `play` en cada turno. Dentro del juego la interfaz es bastante intuitiva y te ayuda en todo momento.

## Interfaz gráfica
Si prefieres usar la interfaz grafica, puedes ingresar el comando `interfaz`, que abre la interfaz diseñada con pygame. Para cerrar la interfaz debes cerrar la ventana y dirigirte a la terminal para continuar.

## Guardado de progreso
El juego incluye guardado de progreso automatico con Redis, por lo que aunque cierres la aplicacion, vas a poder continuar con tu partida mas tarde. Si quieres reiniciar el progreso, ingresa `start` para un juego nuevo. Para que funcione el auto guardado, debe estar inicializado Redis en tu computadora. Para esto debes seguir instrucciones especificas de tu sistema operativo para instalarlo. Ya instalado, puedes iniciar el servidor con: `brew services start redis` (en el caso de MacOS).

## Parte tecnica
# Tests
La aplicacion cuenta con un 90% de covertura. Para ver el reporte de covertura, en la terminal debes ingresar los comandos `coverage run -m unittest discover` para que corra los tests, y `coverage report` para ver el reporte de covertura
Si estas interesado en testear algun modulo especifico (board, checker, cli, dice, game, player), puedes ingresar el comando `python3 -m unittest tests.test_modulo -v`, reemplazando la palabra modulo por alguno de los anteriormente mencionados.
