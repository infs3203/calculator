import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Fixture to create a Calculator instance for each test."""
    return Calculator()

def test_addition(calc):
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtraction(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(0, 0) == 0

def test_multiplication(calc):
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

def test_division(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3

def test_division_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_modulo(calc):
    assert calc.modulo(7, 3) == 1
    assert calc.modulo(15, 4) == 3
    assert calc.modulo(5, 5) == 0

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(2, -1) == 0.5

def test_square_root(calc):
    assert calc.square_root(9) == 3.0
    assert calc.square_root(2) == pytest.approx(1.4142, rel=1e-4)
    
def test_square_root_negative(calc):
    with pytest.raises(ValueError):
        calc.square_root(-1)

# Example of parameterized testing in pytest
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (10, -5, 5),
])
def test_add_parameters(calc, a, b, expected):
    """Demonstrates parameterized testing - a powerful pytest feature"""
    assert calc.add(a, b) == expected

# Example of testing multiple related conditions
def test_arithmetic_relationships(calc):
    """Demonstrates testing mathematical relationships"""
    x, y = 10, 5
    # Testing that (x + y) - y = x
    assert calc.subtract(calc.add(x, y), y) == x
    # Testing that x * y = y * x (multiplication is commutative)
    assert calc.multiply(x, y) == calc.multiply(y, x) 