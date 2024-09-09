from src.rectangle import Rectangle


class Square(Rectangle):
    """Square сlass"""
    def __init__(self, a: int):
        if isinstance(a, int):
            if a >0:
                super().__init__(a, a)
            else:
                ValueError('ERROR: value !> 0')
        else:
            raise ValueError('ERROR: value not int')

    def __str__(self):
        return f"object of the Square class: a = {self.a}"
