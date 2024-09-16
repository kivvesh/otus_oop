import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle
from src.base.figure import Figure


@pytest.mark.parametrize(
    'a,b,c,error',
    [
        (1,2,-1,'ERROR: value not > 0'),
        (1,10,None, 'ERROR: value not int'),
        (1,120,2, 'ERROR: value not > 0'),
        (1,120,'120', 'ERROR: value not int')
    ]
)
@pytest.mark.triangle
@pytest.mark.smoke
def test_nagative_initialization_triangle(a,b,c,error):
    with pytest.raises(ValueError, match=error):
        Triangle(a,b,c)


@pytest.mark.parametrize(
    'a,b,c,area',
    [
        (1,2,2,0.97),
        (10,15,15,70.71),
        (120,130,200,7490.62),
    ]
)
@pytest.mark.triangle
@pytest.mark.smoke
def test_get_area(a,b,c,area):
    triangle_test = Triangle(a,b,c)
    assert triangle_test.get_area == area


@pytest.mark.parametrize(
    'a,b,c,perimeter',
    [
        (1,2,2,5),
        (10,15,15,40),
        (120,130,200,450),
    ]
)
@pytest.mark.triangle
@pytest.mark.smoke
def test_get_perimeter(a,b,c,perimeter):
    triangle_test = Triangle(a,b,c)
    assert triangle_test.get_perimeter == perimeter


@pytest.mark.parametrize(
    'a,b,c,figure,result',
    [
        (2,3,4,Rectangle(2,6),14.9),
        (4,4,5,Circle(2),20.38),
        (3,5,7,Square(5),31.5 ),
    ], ids=['2,3,4 - Rectangle','4,5,5 - Circle','3,5,7 - Square']
)
@pytest.mark.triangle
@pytest.mark.smoke
def test_add_area(a,b,c, figure,result):
    triangle_test = Triangle(a,b,c)
    assert triangle_test.add_area(figure) == result
