from src.rectangle import Rectangle


class Square(Rectangle):
    """Square сlass"""
    def __init__(self, a: int):
        if (isinstance(a, int) or isinstance(a, float)):
            print(1)
            if a > 0:
                super().__init__(a, a)
            else:
                raise ValueError('ERROR: value not > 0')
        else:
            raise ValueError('ERROR: value not int')

    def __str__(self):
        return f"object of the Square class: a = {self.a}"
