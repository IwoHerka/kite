from archaeopteryx.symbol import T, F, NIL, Symbol as S
from archaeopteryx.parser import Parser
from archaeopteryx.list import List as L


def parse(string):
    return Parser().parse(string)


def test_parser_0():
    assert parse('(atom t)') == L(S('atom'), S('t'))


def test_parser_1():
    assert parse('(atom ())') == L(S('atom'), L())


def test_parser_2():
    assert parse(
        '(atom (quote (t f t)))'
    ) == (
        L(S('atom'), L(S('quote'), L(S('t'), S('f'), S('t'))))
    )


def test_parser_3():
    assert parse(
        '(quote () ((1 2)) (atom (t (t f))))'
    ) == (
        L(S('quote'), L(), L(L(S('1'), S('2'))), L(S('atom'), L(S('t'), L(S('t'), S('f')))))
    )


def test_parser_4():
    assert parse(
        '((()) (() () ((()))) ())'
    ) == (
        L(L(L()), L(L(), L(), L(L(L()))), L())
    )


def test_parser_5():
    assert parse('()') == L()


def test_parser_6():
    assert parse('t') == S('t')


def test_parser_7():
    assert parse('') == None
