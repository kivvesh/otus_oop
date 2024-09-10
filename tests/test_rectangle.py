import pytest

from src.rectangle import Rectangle


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
