from otus_oop.src.rectangle import Rectangle


class Square(Rectangle):
    """Square сlass"""
    def __init__(self, a: int):
        if a > 0 and isinstance(a, int):
            super().__init__(a, a)
        else:
            raise ValueError('ERROR: value of the side of the square is not correct')

    def __str__(self):
        return f"object of the Square class: a = {self.a}"
