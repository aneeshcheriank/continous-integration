from hello import add

def test_add():
    assert 5 == add(2, 3)

def test_add_1():
    assert -1 == add(-3, 2)