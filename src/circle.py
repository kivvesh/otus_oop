import math

from otus_oop.src.base.figure import Figure


class Circle(Figure):
    """Circle сlass"""
    def __init__(self, r: int):
        if r > 0 and isinstance(r, int):
            self.r = r
        else:
            raise ValueError('ERROR: value of the side of the circle is not correct')

    def __str__(self):
        return f"object of the Circle class: r = {self.r}"

    @property
    def get_area(self):
        return math.pi * (self.r ** 2)

    @property
    def get_perimeter(self):
        return 2 * self.r * math.pi
