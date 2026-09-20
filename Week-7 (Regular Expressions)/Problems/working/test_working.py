from working import convert
import pytest

def test_ValueError():
    with pytest.raises(ValueError):
        convert("50 AM to 50 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 1:89 PM")
    with pytest.raises(ValueError):
        convert("CS50 to CS50")
    with pytest.raises(ValueError):
        convert("12:36 AM 12:36 PM")
    with pytest.raises(ValueError):
        convert("12:37 - 12:37 PM")
    with pytest.raises(ValueError):
        convert("dog to cat")
    with pytest.raises(ValueError):
        convert("12:38 to - 12:38")

def test_time():
    assert convert("7:00 AM to 8:00 PM") == "07:00 to 20:00"
    assert convert("7 AM to 8 PM") == "07:00 to 20:00"
    assert convert("7:30 PM to 8:30 AM") == "19:30 to 08:30"