from pygeo import add_float

def test_1():
    assert add_float(0.1 + 0.2, 0.3) is True

def test_2():
    assert add_float(0.1 + 0.2, 0.4) is False

def test_3():
    assert add_float(1 + 2, 3) is True