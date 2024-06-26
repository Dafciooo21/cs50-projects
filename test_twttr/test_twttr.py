from twttr import shorten

def test_check():
    assert shorten("Twitter test") == "Twttr tst"
    assert shorten("TWITTER TEST") == "TWTTR TST"
    assert shorten("te$t 123") == "t$t 123"
    assert shorten("t$st!") == "t$st!"
