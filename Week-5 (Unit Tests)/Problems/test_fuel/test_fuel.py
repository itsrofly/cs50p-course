from fuel import convert, gauge
import pytest

def test_zerodivision():
    with pytest.raises(ZeroDivisionError): # Para o pytest
        convert("4/0")

def test_valueError():
    with pytest.raises(ValueError): # Para o pytest
        convert("cs/50")

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"