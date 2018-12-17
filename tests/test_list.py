from archaeopteryx.list import List


def test_list_len():
    assert len(List(1, 2, 3).data) == 3


def test_list_car():
    assert List(1, 2, 3).car() == 1


def test_list_cdr():
    assert List(1, 2, 3).cdr() == List(2, 3)


def test_list_eval():
    pass
