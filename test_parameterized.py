import pytest


@pytest.mark.parametrize("a,b,c",[(1,2,3),(4,7,6)])
def test_functionAdd(a,b,c):
    assert a+b == c

@pytest.mark.parametrize("a,b,c",[(3,2,1),(6,2,4)])
def test_functionSub(a,b,c):
    assert a-b == c

@pytest.mark.parametrize("a,b,c",[(1,2,2),(4,5,6)])
ef test_functionMul(a,b,c):
    assert a*b == c