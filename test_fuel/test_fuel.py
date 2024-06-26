import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_value():
    with pytest.raises(ValueError):
        convert("5/1")
