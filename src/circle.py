import math

from src.base.figure import Figure


class Circle(Figure):
    """Circle сlass"""
    def __init__(self, r: int):
        if isinstance(r, int):
            if r > 0:
                self.r = r
            else:
                raise ValueError('ERROR: value not > 0')
        else:
            raise ValueError('ERROR: value not int')

    def __str__(self):
        return f"object of the Circle class: r = {self.r}"

    @property
    def get_area(self):
        return round(math.pi * (self.r ** 2),2)

    @property
    def get_perimeter(self):
        return round(2 * self.r * math.pi, 2)
