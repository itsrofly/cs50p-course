from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar.capacity = 50
    assert jar.capacity == 50
    with pytest.raises(ValueError):
        jar.capacity = -12
    with pytest.raises(ValueError):
        jar.capacity = 7.7


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(12)
    assert jar.capacity == 0
    jar.withdraw(2)
    assert jar.capacity == 2
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(10)


test_str()