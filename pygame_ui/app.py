"""Modulo app. Define la clase UI."""
from pygame_ui.hitmap import HitMap
from pygame_ui.controller import Controller
from core.game import Game
import pygame
class UI:
    """La clase UI se encarga de manejar la interfaz grafica con pygame."""
    def __init__(self, game:Game) -> None:
        pygame.init()
        self.__width__ = 1000
        self.__height__ = 750
        self.__screen__ = pygame.display.set_mode((self.__width__, self.__height__))
        self.__clock__ = pygame.time.Clock()
        self.__board_background__ = self.background()
        self.__game__: Game = game
        self.__hitmap__ = HitMap(72, 229, 72, 21)
        self.__controller__ = Controller(self.__game__)
        self.__hitmap__.build()
    def run(self):
        """Inicia la interfaz grafica."""
        g:Game = self.__game__
        pygame.display.set_caption('| Backgammon -+- Gerónimo Giordano |')
        run = True

        self.__game__.roll_dice()
        turn_player = g.get_player_1() if g.get_actual_player_turn() == 1 else g.get_player_2()
        turn_player_checker = 'x' if turn_player.get_checker_type() == 1 else 'o'
        self.__controller__.check_state()
        while run:
            self.__game__ = self.__controller__.get_game()
            if self.__controller__.get_fro_to_destinos_dicecount_dice()[3] == len(self.__game__.get_dice().get_dice_results()):

                self.__controller__.change_turn()
            self.__controller__.set_game(self.__game__)
            dt = self.__clock__.tick(60) / 1000.0
            
            if self.__game__.no_available_moves(self.__game__.get_dice().get_dice_results(),
                                                turn_player):
                self.__controller__.change_turn()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__controller__.handle_click(event.pos, self.__hitmap__)

            self.__screen__.blit(self.__board_background__, (0, 0))
            self.__controller__.draw(self.__screen__, self.__controller__.get_fro_to_destinos_dicecount_dice()[0], self.__controller__.get_fro_to_destinos_dicecount_dice()[2])
            pygame.display.flip()
        pygame.quit()
    def background(self):
        """Configura la parte estatica de la pantalla,
        como los triangulos, el fondo, los margenes, etc."""
        bg = pygame.Surface((1000, 750)).convert()
        bg.fill((222, 206, 173))
        pygame.draw.line(bg, (0, 0, 0), (15, 15), (15, 735), 10)
        pygame.draw.line(bg, (0, 0, 0), (11, 15), (990, 15), 10)
        pygame.draw.line(bg, (0, 0, 0), (11, 735), (990, 735), 10)
        pygame.draw.line(bg, (0, 0, 0), (985, 15), (985, 735), 10)
        ancho = 72
        #barra
        pygame.draw.line(bg, (0,0,0), (462, 20), (462, 730), 10)
        pygame.draw.line(bg, (0,0,0), (539, 20), (539, 730), 10)
        #cuadrante1
        for i in range(3):
            pygame.draw.polygon(bg, (157, 94, 55),
                                ((545+ancho*2*i, 730),
                                 (619+ancho*2*i,730),
                                 (580.5+ancho*2*i, 500)))
            pygame.draw.polygon(bg, (15, 9, 2),
                                ((617+ancho*2*i, 730),
                                 (691+ancho*2*i,730),
                                 (652.5+ancho*2*i, 500)))
        #cuadrante2
            pygame.draw.polygon(bg, (157, 94, 55),
                                ((21+ancho*2*i, 730),
                                 (98+ancho*2*i,730),
                                 (58+ancho*2*i, 500)))
            pygame.draw.polygon(bg, (15, 9, 2),
                                ((93+ancho*2*i, 730),
                                 (170+ancho*i*2,730),
                                 (130+ancho*i*2, 500)))
        #cuadrante3
            pygame.draw.polygon(bg, (157, 94, 55),
                                ((21+ancho*2*i, 20),
                                 (98+ancho*2*i,20),
                                 (58+ancho*2*i, 250)))
            pygame.draw.polygon(bg, (15, 9, 2),
                                ((93+ancho*2*i, 20),
                                 (170+ancho*i*2,20),
                                 (130+ancho*i*2, 250)))
        #cuadrante4
            pygame.draw.polygon(bg, (157, 94, 55),
                                ((545+ancho*2*i, 20),
                                 (619+ancho*2*i,20),
                                 (580.5+ancho*2*i, 250)))
            pygame.draw.polygon(bg, (15, 9, 2),
                                ((617+ancho*2*i, 20),
                                 (691+ancho*2*i,20),
                                 (652.5+ancho*2*i, 250)))

        return bg
