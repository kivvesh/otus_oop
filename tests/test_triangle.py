import pytest

from src.triangle import Triangle


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
