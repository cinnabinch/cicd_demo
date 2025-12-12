import sys
from pathlib import Path
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide,
    log, square, sin, cos, sqrt, percentage
)

def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_log():
    assert log(1) == 0


def test_square():
    assert square(4) == 16


def test_sin():
    assert sin(0) == 0


def test_cos():
    assert cos(0) == 1


def test_sqrt():
    assert sqrt(9) == 3


def test_percentage():
    assert percentage(50, 10) == 5