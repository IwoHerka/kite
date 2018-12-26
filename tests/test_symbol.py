import pytest

from hypothesis import given
from hypothesis.strategies import *

from kite.symbol import Symbol, T, F, NIL
from kite.list import List

from .util import anything_except_string, two_different_names


@given(lists(text(), min_size=1))
def test_cannot_construct_symbol_with_more_than_one_argument(args):
    with pytest.raises(TypeError):
        Symbol(str(), *args)


@given(anything_except_string())
def test_symbol_name_must_be_string(name):
    with pytest.raises(TypeError):
        Symbol(name)


@given(text())
def test_two_symbols_with_same_names_are_the_same(name):
    assert Symbol(name) == Symbol(name)
    assert Symbol(name) is Symbol(name)
    assert hash(Symbol(name)) == hash(Symbol(name))


@given(two_different_names())
def test_two_symbols_with_different_names_are_different(names):
    first, second = names
    assert Symbol(first) != Symbol(second)
    assert not Symbol(first) is Symbol(second)
    assert hash(Symbol(first)) != hash(Symbol(second))


def test_T_is_a_symbol():
    assert T == Symbol('t')


def test_F_is_empty_list():
    assert F == List()


def test_NIL_is_a_symbol():
    assert NIL == Symbol('NIL')
