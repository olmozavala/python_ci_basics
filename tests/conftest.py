import pytest

@pytest.fixture()
def myfixture():
    yield 4, 8