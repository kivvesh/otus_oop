from otus_oop.src.base.figure import Figure


class Rectangle(Figure):
    """Rectangle сlass"""
    def __init__(self, a: int, b: int):
        if (a > 0 and b > 0
            and isinstance(a, int) and isinstance(b, int)
        ):
            self.a = a
            self.b = b
        else:
            raise ValueError('ERROR: value of the side of the rectangle is not correct')

    @property
    def get_area(self):
        return self.a * self.b

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2
