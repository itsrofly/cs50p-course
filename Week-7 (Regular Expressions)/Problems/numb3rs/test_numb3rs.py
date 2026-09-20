import pytest
from numb3rs import validate

def test_ip():
  assert validate("255.255.255.255") == True
  assert validate("255") == False
  assert validate("1.1.1.1.1") == False
  assert validate("192.168.1.1") == True
  assert validate("292.168.1.1") == False
  assert validate("0.666.666.666") == False