import sys
import pygame
class UI:
    def __init__(self) -> None:
        self.__width__ = 1000
        self.__height__ = 750
        self.__screen__ = pygame.display.set_mode((self.__width__, self.__height__))
        self.__clock__ = pygame.time.Clock()
        self.board_background = self.background()
    def run(self):
        pygame.init()
        pygame.display.set_caption('| Backgammon -+- Gerónimo Giordano |')
        run = True
        while run:
            dt = self.__clock__.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.__screen__.blit(self.board_background, (0, 0))
            pygame.display.flip()
        pygame.quit()
    def background(self):
        W, H = self.__screen__.get_size()
        bg = pygame.Surface((W, H)).convert()
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
            pygame.draw.polygon(bg, (157, 94, 55), ((545+ancho*2*i, 730), (619+ancho*2*i,730), (580.5+ancho*2*i, 545)))
            pygame.draw.polygon(bg, (15, 9, 2), ((617+ancho*2*i, 730), (691+ancho*2*i,730), (652.5+ancho*2*i, 545)))
        #cuadrante2
        for i in range(3):
            pygame.draw.polygon(bg, (157, 94, 55), ((21+ancho*2*i, 730), (98+ancho*2*i,730), (58+ancho*2*i, 545)))
            pygame.draw.polygon(bg, (15, 9, 2), ((93+ancho*2*i, 730), (170+ancho*i*2,730), (130+ancho*i*2, 545)))
        #cuadrante3
        for i in range(3):
            pygame.draw.polygon(bg, (157, 94, 55), ((21+ancho*2*i, 20), (98+ancho*2*i,20), (58+ancho*2*i, 205)))
            pygame.draw.polygon(bg, (15, 9, 2), ((93+ancho*2*i, 20), (170+ancho*i*2,20), (130+ancho*i*2, 205)))
        #cuadrante4
        for i in range(3):
            pygame.draw.polygon(bg, (157, 94, 55), ((545+ancho*2*i, 20), (619+ancho*2*i,20), (580.5+ancho*2*i, 205)))
            pygame.draw.polygon(bg, (15, 9, 2), ((617+ancho*2*i, 20), (691+ancho*2*i,20), (652.5+ancho*2*i, 205)))

        return bg

ui = UI()
ui.run()