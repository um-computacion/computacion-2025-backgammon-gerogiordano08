import pygame
from core.game import Game
class Controller:
    def __init__(self, game:Game) -> None:
        self.__game__ = game
        self.__dark_checker__, self.__light_checker__ = self.load_checkers_png()
        self.__font__ = pygame.font.Font(None, 40)
    def get_checker_position(self, index:int, stack_position:int):
        """Traduce la posicion de una ficha, desde el atributo
        columnas de Board, a una posicion de pixeles en el tablero."""
        # x agrega el ancho de la barra (92)
        ancho_barra = 92 if 6 <= index < 12 or 17 < index else 0

        if index < 12:
            #pixel_pos x_coord = screen_width - margin - index*triangle_width - checker_width (para conseguir esquina izquierda)
            x = 970 - ancho_barra - index * 72 - 60
            #pixel_pos y_coord = screen_height - margin - (stack_position) * checker_height - checker_height (para conseguir esquina izquierda)

            y = 730 - stack_position * 60 - 60
        else:
            x = 30 + ancho_barra + (index -12)* 72

            y = 20 + stack_position * 60

        return x, y
    def draw(self, surface:pygame.Surface):
        for i, x in enumerate(self.__game__.get_board().get_columnas()):
            for a in range(x['quantity']):
                start_point = self.get_checker_position(i, a)
                if a < 4:
                    if x['checker'] == 'x':
                        if type(self.__dark_checker__) == pygame.Surface:
                            surface.blit(self.__dark_checker__, start_point)

                    if x['checker'] == 'o':
                        if type(self.__light_checker__) == pygame.Surface:
                            surface.blit(self.__light_checker__, start_point)
                else:
                    text_quantity = self.__font__.render(str(x['quantity']), True, (0, 0, 0))
                    text_point = (start_point[0] + 22, start_point[1] + 80) if i < 12 else (start_point[0] + 22, start_point[1] - 40)
                    surface.blit(text_quantity, text_point)
                    break
    def load_checkers_png(self) -> tuple[pygame.Surface| None, pygame.Surface | None]:
        """Carga los pngs de las fichas."""
        checker_size = (60, 60)
        dark_checker, light_checker = None, None
        try:
            dark = pygame.image.load("assets/images/checker_dark1.png").convert_alpha()
            light = pygame.image.load("assets/images/checker_light1.png").convert_alpha()
            dark_checker = pygame.transform.scale(dark, checker_size)
            light_checker = pygame.transform.scale(light, checker_size)
        except pygame.error as e:
            print(f"Error al cargal las imagenes de las fichas{e}")
        return dark_checker, light_checker