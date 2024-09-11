import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle

@pytest.mark.parametrize(
    'a,b,error',
    [
        (-1,2,'ERROR: value not > 0'),
        (-1, -100, 'ERROR: value not > 0'),
        ('123', 12, 'ERROR: value not int'),
        ('AbC', None, 'ERROR: value not int'),
    ]
)
@pytest.mark.rectangle
@pytest.mark.smoke
def test_negative_initialization_rectangle(a,b,error):
    with pytest.raises(ValueError,match=error):
        Rectangle(a,b)


@pytest.mark.parametrize(
    'a,b,area',
    [
        (2,2,4),
        (10,2,20),
        (1.5,2.5,3.75),
    ]
)
@pytest.mark.rectangle
@pytest.mark.smoke
def test_get_area(a,b,area):
    test_rectangle = Rectangle(a,b)
    assert test_rectangle.get_area == area


@pytest.mark.parametrize(
    'a,b,perimeter',
    [
        (2,2,8),
        (10,2,24),
        (1.5,2,7),
    ]
)
@pytest.mark.rectangle
@pytest.mark.smoke
def test_get_perimeter(a,b,perimeter):
    test_rectangle = Rectangle(a,b)
    assert test_rectangle.get_perimeter == perimeter


@pytest.mark.parametrize(
    'a,b,figure,result',
    [
        (1,4,Circle(2),16.57),
        (1,4,Triangle(2,2,3),5.98),
        (1,4,Square(5),29),
    ], ids=['1,4 - Circle','1,4 - Triangle','1,4 - Square']
)
@pytest.mark.rectangle
@pytest.mark.smoke
def test_add_area(a,b,figure,result):
    test_rectangle = Rectangle(a,b)
    assert test_rectangle.add_area(figure) == result
