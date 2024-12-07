import pytest
from jar import Jar

def test_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(8)
    assert jar.capacity == 8
    assert jar.size == 0

    # Invalid capacity (negative number)
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer."):
        Jar(-1)

    # Invalid capacity (not an integer)
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer."):
        Jar("ten")

def test_str():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    # deposit exceeding capacity
    with pytest.raises(ValueError, match="Not enough space in the jar for that many cookies."):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)

    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError, match="Not enough cookies in the jar to withdraw."):
        jar.withdraw(3)

def test_edge_cases():
    jar = Jar(3)
    # Deposit exactly to capacity
    jar.deposit(3)
    assert jar.size == 3

    # Withdraw all cookies
    jar.withdraw(3)
    assert jar.size == 0

    # Deposit zero cookies
    jar.deposit(0)
    assert jar.size == 0

    # Withdraw zero cookies
    jar.withdraw(0)
    assert jar.size == 0
