from plates import is_valid

def test_twoletters():
    assert is_valid("EB") == True
    assert is_valid("10") == False
    assert is_valid("E1") == False
    assert is_valid("1") == False

def test_length():
    assert is_valid("EBE12") == True
    assert is_valid("EB") == True
    assert is_valid("EBE1234567") == False

def test_numbers():
    assert is_valid("EBE123") == True
    assert is_valid("EBE12E") == False
    assert is_valid("EBE012") == False

def test_punctuation():
    assert is_valid("EBE12!") == False
