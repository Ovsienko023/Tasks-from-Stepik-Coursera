from src.prog_logic.main import Temp
import pytest

@pytest.fixture()
def f():
    print(1)


@pytest.mark.usefixtures('f')
def test_success():
    assert True


@pytest.mark.parametrize('res', [
    len('Temperature in Moscow, today: 0.00\u2103')
])
def test_today(res):
    t = Temp()
    assert len(t.today()) == res
