import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle
from src.base.figure import Figure


@pytest.mark.parametrize(
    'a,error',
    [
        (-2, 'ERROR: value not > 0'),
        (0, 'ERROR: value not > 0'),
        (None, 'ERROR: value not int'),
        ([], 'ERROR: value not int'),
    ]
)
@pytest.mark.square
@pytest.mark.smoke
def test_negative_initialization_square(a,error):
    with pytest.raises(ValueError, match = error):
        Square(a)


@pytest.mark.parametrize(
    'a,area',
    [
        (2,4),
        (10,100),
        (1.5,2.25),
    ]
)
@pytest.mark.square
@pytest.mark.smoke
def test_get_area(a,area):
    test_square = Square(a)
    assert test_square.get_area == area


@pytest.mark.parametrize(
    'a,perimeter',
    [
        (2,8),
        (10,40),
        (1.5,6),
    ]
)
@pytest.mark.square
@pytest.mark.smoke
def test_get_perimeter(a,perimeter):
    test_square = Square(a)
    assert test_square.get_perimeter == perimeter


@pytest.mark.parametrize(
    'a,figure,result',
    [
        (2,Rectangle(2,6),16),
        (4,Circle(2),28.57),
        (3,Triangle(5,5,3),16.15),
    ], ids=['2- Rectangle','4 - Circle','3 - Triangle']
)
@pytest.mark.square
@pytest.mark.smoke
def test_add_area(a, figure,result):
    test_square = Square(a)
    assert test_square.add_area(figure) == result
