from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi you") == 20

def test_other():
    assert value("what's up") == 100

def test_case_intesitivity():
    assert value("HELLO") == 0
