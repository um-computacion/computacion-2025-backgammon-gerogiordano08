import pygame
from core.game import Game
from core.player import Player
from core.redis_store import RedisStore
from pygame_ui.hitmap import HitMap
class Controller:
    def __init__(self, game:Game) -> None:
        self.__game__ = game
        self.__redis_store__ = RedisStore()
        #pngs de checkers, dados y flechas, en ese orden
        self.__assets__= self.load_pngs()
        self.__font__ = pygame.font.Font(None, 40)
        self.__font_smaller__ = pygame.font.Font(None, 30)
        self.__fro_to_destinos_dicecount_useddice__ = [None, None, [], 0, []]
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
    def draw(self, surface:pygame.Surface, fro:int|None, destinos:list):
        """Dibuja las fichas, los dados y el nombre del jugador."""
        for i, x in enumerate(self.__game__.get_board().get_columnas()):
            for a in range(x['quantity']):
                start_point = self.get_checker_position(i, a)
                if a < 4:
                    if x['checker'] == 'x':
                        if type(self.__assets__[0]) == pygame.Surface:
                            surface.blit(self.__assets__[0], start_point)

                    if x['checker'] == 'o':
                        if type(self.__assets__[1]) == pygame.Surface:
                            surface.blit(self.__assets__[1], start_point)
                else:
                    text_quantity = self.__font__.render(str(x['quantity']), True, (0, 0, 0))
                    text_quantity_point = (start_point[0] + 22, start_point[1] + 80) if i < 12 else (start_point[0] + 22, start_point[1] - 40)
                    surface.blit(text_quantity, text_quantity_point)
                    break
        player_name = ''
        text_turn_point = (100, 300)
        if self.__game__.get_actual_player_turn() == 1:
            player_name = self.__game__.get_player_1().get_name()
        if self.__game__.get_actual_player_turn() == 2:
            player_name = self.__game__.get_player_2().get_name()
        text_turn = self.__font__.render(f'Turno de {player_name}', True, (0, 0, 0))
        surface.blit(text_turn, text_turn_point)
        dice_dict = {0:self.__font__.render('Dado', True, (0, 0, 0)),
                    1:self.__assets__[2],
                    2:self.__assets__[3],
                    3:self.__assets__[4],
                    4:self.__assets__[5],
                    5:self.__assets__[6],
                    6:self.__assets__[7]}
        dice_a, dice_b = self.__game__.get_dice().get_dice_results()[0], self.__game__.get_dice().get_dice_results()[1]
        dice_a_point = (600, 300)
        dice_b_point = (670, 300)
        surface.blit(dice_dict[dice_a], dice_a_point)
        surface.blit(dice_dict[dice_b], dice_b_point)
        if fro is not None:
            self.draw_arrow(surface, fro, True)
        for dest in destinos:
            self.draw_arrow(surface, dest, False)
    def load_pngs(self):
        """Carga los pngs de las fichas."""
        checker_size = (60, 60)
        arrow_size = (30, 30)
        dark_checker, light_checker = None, None
        try:
            dark = pygame.image.load("assets/images/checker_dark1.png").convert_alpha()
            light = pygame.image.load("assets/images/checker_light1.png").convert_alpha()
            dark_checker = pygame.transform.scale(dark, checker_size)
            light_checker = pygame.transform.scale(light, checker_size)
            dice_1a = pygame.image.load('assets/images/dado_1.png').convert_alpha()
            dice_2a = pygame.image.load('assets/images/dado_2.png').convert_alpha()
            dice_3a = pygame.image.load('assets/images/dado_3.png').convert_alpha()
            dice_4a = pygame.image.load('assets/images/dado_4.png').convert_alpha()
            dice_5a = pygame.image.load('assets/images/dado_5.png').convert_alpha()
            dice_6a = pygame.image.load('assets/images/dado_6.png').convert_alpha()
            dice_1 = pygame.transform.scale(dice_1a, checker_size)
            dice_2 = pygame.transform.scale(dice_2a, checker_size)
            dice_3 = pygame.transform.scale(dice_3a, checker_size)
            dice_4 = pygame.transform.scale(dice_4a, checker_size)
            dice_5 = pygame.transform.scale(dice_5a, checker_size)
            dice_6 = pygame.transform.scale(dice_6a, checker_size)
            from_arrow_a = pygame.image.load('assets/images/from_arrow.png').convert_alpha()
            to_arrow_a = pygame.image.load('assets/images/to_arrow.png').convert_alpha()
            from_arrow = pygame.transform.scale(from_arrow_a, arrow_size)
            to_arrow = pygame.transform.scale(to_arrow_a, arrow_size)

        except pygame.error as e:
            print(f"Error al cargal las imagenes {e}")
        return dark_checker, light_checker, dice_1, dice_2, dice_3, dice_4, dice_5, dice_6, from_arrow, to_arrow

    def draw_winner_message(self, winner:Player, surface:pygame.Surface):
        rect_surface = pygame.Surface((600, 60), pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, (210, 230, 185), rect_surface.get_rect(), border_radius=10)
        winner_message = self.__font_smaller__.render((f'Felicidades {winner.get_name()}! Ganaste el juego.'), True, (0, 0, 0))
        winner_message2 = self.__font_smaller__.render('Puedes salir del juego para iniciar una nueva partida.', True, (0, 0, 0))
        rect_surface.blit(winner_message, (10,10))
        rect_surface.blit(winner_message2, (10, 35))
        rect_pos = rect_surface.get_rect(center=(500, 375))
        surface.blit(rect_surface, rect_pos)
    def draw_arrow(self, surface:pygame.Surface, triangle:int, fro:bool):
        initial_pos = self.get_checker_position(triangle, 4)
        if triangle > 12:
            dest_point = (initial_pos[0] + 10, initial_pos[1] + 10)
            if fro is True:
                surface.blit(self.__assets__[9], dest_point)
            else:
                surface.blit(self.__assets__[8], dest_point)
        else:
            dest_point = (initial_pos[0] + 15, initial_pos[1])
            if fro is True:
                surface.blit(self.__assets__[8], dest_point)
            else:
                surface.blit(self.__assets__[9], dest_point)
    def change_turn(self):
        if self.__game__.get_actual_player_turn() == 1:
            self.__game__.set_actual_player_turn(2)
        else:
            self.__game__.set_actual_player_turn(1)

    def handle_click(self,click_pos, hitmap:HitMap):
        info_list = self.__fro_to_destinos_dicecount_useddice__
        g:Game = self.__game__
        clicked_info = hitmap.hit_test(click_pos)
        cols = self.__game__.get_board().get_columnas()
        turn_player = g.get_player_1() if g.get_actual_player_turn() == 1 else g.get_player_2()
        turn_player_checker = 'x' if turn_player.get_checker_type() == 1 else 'o'
        #clickea un triangulo para seleccionarlo como origen
        if type(clicked_info['index']) is int:
            if (cols[clicked_info['index'] -1]['checker'] == turn_player_checker
            and cols[clicked_info['index'] -1]['quantity'] > 0
            and clicked_info['index'] -1 not in info_list[2]):
                selected_triangle = clicked_info['index'] - 1
                info_list[0] = selected_triangle
                info_list[2] = []
                available_dice = []
                if self.__game__.get_dice().get_dice_results()[0] == self.__game__.get_dice().get_dice_results()[1]:
                    for _ in range(len(self.__game__.get_dice().get_dice_results()) - len(info_list[4])):
                        available_dice.append(self.__game__.get_dice().get_dice_results()[0])
                else:
                    available_dice = [x for x in self.__game__.get_dice().get_dice_results() if x not in info_list[4]]
                print(self.__game__.get_dice().get_dice_results(), info_list[4], available_dice)
                for di in available_dice:
                    if turn_player.get_checker_type() == 1:
                        if self.__game__.available_move(selected_triangle, selected_triangle + di):
                            info_list[2].append(selected_triangle+di)
                    else:
                            if self.__game__.available_move(selected_triangle, selected_triangle - di):
                                info_list[2].append(selected_triangle-di)
        #clickea un triangulo para seleccionarlo como destino
        if type(clicked_info['index']) is int:
            if (info_list[0] is not None
                and clicked_info['index'] -1 in info_list[2]):
                selected_triangle = clicked_info['index'] - 1
                info_list[1] = selected_triangle
                used_die = abs(info_list[1] - info_list[0])
                info_list[4].append(used_die)
                self.__game__.move_checker(info_list[0], info_list[1])
                info_list[0] = None
                info_list[1] = None
                info_list[2] = []
                info_list[3] += 1


                
    def set_game(self, new_game):
        self.__game__ = new_game
    def get_game(self):
        return self.__game__
    def get_fro_to_destinos_dicecount_dice(self):
        return self.__fro_to_destinos_dicecount_useddice__
    def set_fro_to_destinos_dicecount_dice(self, index:int ,new:int|list):
        self.__fro_to_destinos_dicecount_useddice__[index] = new
        