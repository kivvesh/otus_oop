import pytest
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def start_tests():
    print('\nStart tests')
    start = datetime.now()
    yield
    stop = datetime.now()
    print(f'\nTests finish, time - {(stop - start).seconds}')