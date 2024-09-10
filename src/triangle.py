from src.base.figure import Figure


class Triangle(Figure):
    """Triangle сlass"""
    def __init__(self, a: int, b: int, c: int):
        if ((isinstance(a, int) or isinstance(a, float))
                and
                (isinstance(b, int)  or isinstance(b, float))
                and
                isinstance(c, int) or isinstance(c, float)):
            if (a > 0 and b > 0 and c > 0 and a < (b + c) and
            b < a + c and c < a + b):
                self.a = a
                self.b = b
                self.c = c
            else:
                raise ValueError('ERROR: value not > 0')
        else:
            raise ValueError('ERROR: value not int')

    def __str__(self):
        return f"object of the Triangle class: a = {self.a}, b = {self.b}, c = {self.c}"

    @property
    def get_area(self):
        p = self.get_perimeter / 2
        return round((p*(p-self.a)*(p-self.b)*(p-self.c)) ** 0.5,2)

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c
