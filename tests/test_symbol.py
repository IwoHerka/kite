from archaeopteryx.symbol import *


def test_symbol_uniqueness():
    t = Symbol('t')
    f = Symbol('f')

    assert not (t is f)
    assert t != f
    assert t == Symbol('t')
    assert t is Symbol('t')
