import sys
import pygame
class UI:
    def __init__(self) -> None:
        self.__width__ = 1000
        self.__height__ = 750
        self.__background_color__ = (222, 206, 173)
        self.__screen__ = pygame.display.set_mode((self.__width__, self.__height__))
        self.__clock__ = pygame.time.Clock()
    def run(self):
        pygame.init()
        pygame.display.set_caption('| Backgammon -+- Gerónimo Giordano |')
        run = True
        while run:
            dt = self.__clock__.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.__screen__.fill(self.__background_color__)
            pygame.display.flip()
        pygame.quit()

ui = UI()
ui.run()