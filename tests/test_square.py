import pytest

from src.square import Square


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
