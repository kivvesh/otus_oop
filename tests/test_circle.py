import pytest

from src.circle import Circle


@pytest.mark.circle
@pytest.mark.parametrize("r,result",[
    ('a', 'ERROR: value not int'),
    (-100, 'ERROR: value not > 0'),
    (None, 'ERROR: value not int')
], ids = ['ValueError, r is str','ValueError, r < 0 ','ValueError, r is None', ])
def test_negative_initialization_circle(r, result):
    """Тест для проверки инициализации объектов класса Circle"""
    with pytest.raises(ValueError, match=result):
        test_circle = Circle(r)


@pytest.mark.circle
@pytest.mark.parametrize('r,area',[
    (1,3.14),
    (10,314.16),
    (15,706.86),
], ids = ['r = 1, area = 3.14', 'r = 10, area = 314.16',  'r = 15, area = 706.86'])
def test_get_area(r, area):
    """Тест для проверки вычисления площади круга"""
    test_circle = Circle(r)
    assert test_circle.get_area == area


@pytest.mark.circle
@pytest.mark.parametrize('r,perimeter',[
    (1, 6.28),
    (10, 62.83),
    (15, 94.25),
], ids = ['r = 1, perimeter = 6.28', 'r = 10, perimeter = 62.83',  'r = 15, perimeter = 94.25'])
def test_get_perimeter(r, perimeter):
    test_circle = Circle(r)
    assert test_circle.get_perimeter == perimeter
