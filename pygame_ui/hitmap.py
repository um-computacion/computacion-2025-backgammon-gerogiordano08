"""Modulo hitmap. Define la clase HitMap"""
from typing import Tuple, Dict
import pygame
class HitMap:
    """La clase HitMap define la logica para identificar donde clickeo el usuario."""
    def __init__(self, poly_width:int, poly_height:int, height:int, margin:int) -> None:
        self.__points__ = []
        self.__poly_width__ = poly_width
        self.__poly_height__ = poly_height
        self.__height__ = height
        self.__margin__ = margin
        self.__bar_rect__ = None
    def build(self) -> None:
        """Construye las siluetas de los triangulos y la barra para poder mapear un click."""
        #poligonos superiores (13...24)
        for i in range(12):
            # x agrega el ancho de la barra (poly_width)
            # la adicion de 20 se refiere al ancho de las lineas de la barra
            x = self.__poly_width__ + 20 if i >= 6 else 0
            poly = [(x + self.__margin__ + self.__poly_width__*i,
                     self.__margin__),
                    (x + self.__margin__ + self.__poly_width__ + self.__poly_width__*i,
                     self.__margin__),
                    (x + self.__margin__ + self.__poly_width__/2 + self.__poly_width__*i,
                     self.__poly_height__ + self.__margin__)]
            rect = pygame.Rect(x + self.__margin__+self.__poly_width__*i,
                               self.__margin__,
                               self.__poly_width__,
                               self.__poly_height__)
            self.__points__.append({"poly":poly, "rect":rect, "index": 13 + i})
        #poligonos inferiores (12...1)
        for i in range(12):
            # x agrega el ancho de la barra (poly_width)
            # la adicion de 20 se refiere al ancho de las lineas de la barra
            x = self.__poly_width__ + 20 if i >= 6 else 0
            # 750 se refiere al alto de la pantalla
            poly = [(x + self.__margin__ + self.__poly_width__*i,
                     750 - self.__margin__),
                    (x + self.__margin__ + self.__poly_width__ + self.__poly_width__*i,
                     750 - self.__margin__),
                    (x + self.__margin__ + self.__poly_width__/2 + self.__poly_width__*i,
                     750 - self.__poly_height__ - self.__margin__)]
            rect = pygame.Rect(x + self.__margin__+self.__poly_width__*i,
                               750 - self.__margin__ - self.__poly_height__,
                               self.__poly_width__,
                               self.__poly_height__)
            self.__points__.append({"poly":poly, "rect":rect, "index": 12 - i})
        self.__bar_rect__ = pygame.Rect(self.__margin__ + self.__poly_width__*6,
                                        self.__margin__,
                                        self.__poly_width__ + self.__margin__,
                                        750 - self.__margin__*2)
    def hit_test(self, pos: Tuple[int, int]) -> Dict[str, str|int|None]:
        """Recibe la posicion (x, y) en la que el usuario clickeo y devuelve si
        fue en la barra o en un triangulo. Si fue en un triangulo, tambien devuelve
        que numero de triangulo es."""
        x, y = pos
        if self.__bar_rect__ is not None:
            if self.__bar_rect__.collidepoint(x, y):
                return {"type": "bar", "index": None}
        for p in self.__points__:
            if p["rect"].collidepoint(x, y):
                if self.is_point_in_triangle((x, y), p["poly"]):
                    return {"type": "triangulo", "index": p["index"]}

        return {"type": None, "index": None}

    def is_point_in_triangle(self, pt: Tuple[int, int], triangle: list[Tuple[int, int]]) -> bool:
        """Detecta si un punto dado (pt) esta dentro de un triangulo (triangle).
        Usa matematicamente las coordenadas baricentricas."""
        (p_x, p_y) = pt
        (v1_x, v1_y) = triangle[0]
        (v2_x, v2_y) = triangle[1]
        (v3_x, v3_y) = triangle[2]

        d = (v2_y - v3_y) * (v1_x - v3_x) + (v3_x - v2_x) * (v1_y - v3_y)
        if d == 0:
            return False # Triángulo degenerado

        s = (v2_y - v3_y) * (p_x - v3_x) + (v3_x - v2_x) * (p_y - v3_y)
        t = (v3_y - v1_y) * (p_x - v3_x) + (v1_x - v3_x) * (p_y - v3_y)

        s /= d
        t /= d

        return s > 0 and t > 0 and (s + t) < 1
