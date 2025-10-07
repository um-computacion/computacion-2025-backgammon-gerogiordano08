"""Modulo Excepciones. Contiene la definicion de las excepciones."""
class GameError(Exception):
    """Excepcion base"""
class InputError(Exception):
    """Excepcion para un input incorrecto."""
    def __init__(self):
        super().__init__("Debes ingresar un número!")
