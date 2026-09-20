from twttr import shorten

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_mix():
    assert shorten("TwiTTer") == "TwTTr"

def test_number():
    assert shorten("Tw1TTer") == "Tw1TTr"

def test_pontuation():
    assert shorten("Tw?TTer") == "Tw?TTr"