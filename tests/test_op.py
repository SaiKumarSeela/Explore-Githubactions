from src.math_op import add, sub, mul, div


def test_add():
    assert add(2,3)==5
    assert add(5,2)==7

def test_sub():
    assert sub(5,2)==3
    assert sub(2,5)==-3

def test_mul():
    assert mul(2,3)==6
    assert mul(1,0)==0

def test_div():
    assert div(4,2)==2
    assert div(9,3)==3

