from src.base.figure import Figure


class Rectangle(Figure):
    """Rectangle сlass"""
    def __init__(self, a: int, b: int):
        if ((isinstance(a, int) and isinstance(b, int))
                or
            (isinstance(a, float) or isinstance(b, float))):
            if a > 0 and b > 0:
                self.a = a
                self.b = b
            else:
                raise ValueError('ERROR: value not > 0')
        else:
            raise ValueError('ERROR: value not int')

    def __str__(self):
        return f"object of the Rectangle class: a = {self.a}, b = {self.b}"

    @property
    def get_area(self):
        return self.a * self.b

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2
