from bank import value

def test_hello():
    assert value("Hello") == 0

def test_startwithh():
    assert value("h") == 20

def test_bye():
    assert value("What's up") == 100

def test_helloclient():
    assert value("Hello client") == 0
