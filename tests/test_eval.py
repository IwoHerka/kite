import pytest

from kite import lisp
from kite.symbol import Symbol, T, F, NIL
from kite.env import Environment
from kite.symbol import Symbol as S
from kite.list import List

env = None

def setup_function():
    global env
    env = lisp.get_environment()


def test_eval_symbol():
    t = S('t').eval(env)
    assert t != None
    assert str(t) == 't'


def test_eval_cannot_apply_to_symbol():
    with pytest.raises(TypeError):
        List(T, F, NIL).eval(env)


def test_eval_quoted_list():
    l = List(S('quote'), List(T, F, NIL)).eval(env)

    assert type(l) is List
    assert str(l) == '(t () NIL)'


def test_atom():
    assert List(S('atom'), S('t')).eval(env) == T
    assert List(S('atom'), S('f')).eval(env) == T
    assert List(S('atom'), S('nil')).eval(env) == T

    assert List(S('atom'), List(S('quote'), List(S('t')))).eval(env) == F
    assert List(S('atom'), List(S('quote'), List(S('atom')))).eval(env) == F


def test_eq():
    assert List(S('eq'), S('t'), S('t')).eval(env) == T
    assert List(S('eq'), S('t'), S('f')).eval(env) == F
    assert List(S('eq'), S('t'), List(S('quote'), S('f'))).eval(env) == F


def test_car():
    '(car (t f t f f))'

    assert List(S('car'), List(S('quote'), List(S('t'), S('f')))).eval(env) == S('t')

    with pytest.raises(TypeError):
        List(S('car'), List(S('t'), S('f'))).eval(env)


def test_cdr():
    pass


def test_cons():
    assert List(
        S('cons'),
        S('t'),
        List(
            S('quote'),
            List(
                S('t'),
                S('f')
            )
        )
    ).eval(env)
