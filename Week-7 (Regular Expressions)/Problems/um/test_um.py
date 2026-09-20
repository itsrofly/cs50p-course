from um import count

def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("yumy") == 0
    assert count("um,") == 1
    assert count("um, um, um") == 3
    assert count("good") == 0